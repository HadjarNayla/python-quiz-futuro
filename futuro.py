import streamlit as st
import pandas as pd
import sys
from io import StringIO

# --- Page config ---
st.set_page_config(page_title="Python Quiz - Futuro AI", page_icon="🎓", layout="centered")

# --- Global Arabic Style ---
st.markdown("""
<style>
p[dir='rtl'] {
    font-family: "Amiri", "Scheherazade", "Arial", sans-serif;
    direction: rtl;
    text-align: right;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# --- Safe Code Execution Function ---
def execute_code_safely(code, test_cases):
    """
    Execute student code and check against test cases
    Returns: (is_correct, output, error_message)
    """
    try:
        # Create a clean namespace for execution
        namespace = {}
        
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Execute the code
        exec(code, namespace)
        
        # Get the output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        # Check against test cases
        for test_case in test_cases:
            if test_case['type'] == 'variable':
                # Check if variable exists and has correct value
                var_name = test_case['var_name']
                expected = test_case['expected']
                if var_name in namespace:
                    actual = namespace[var_name]
                    if actual == expected or str(actual) == str(expected):
                        return True, output, None
                    else:
                        return False, output, f"Variable '{var_name}' has wrong value"
                else:
                    return False, output, f"Variable '{var_name}' not found"
            
            elif test_case['type'] == 'function':
                # Check if function exists and works correctly
                func_name = test_case['func_name']
                if func_name in namespace and callable(namespace[func_name]):
                    func = namespace[func_name]
                    # Test with provided inputs
                    for inp, expected_output in test_case['tests']:
                        try:
                            result = func(*inp) if isinstance(inp, tuple) else func(inp)
                            if result != expected_output:
                                return False, output, f"Function returned {result}, expected {expected_output}"
                        except Exception as e:
                            return False, output, f"Function error: {str(e)}"
                    return True, output, None
                else:
                    return False, output, f"Function '{func_name}' not found or not callable"
            
            elif test_case['type'] == 'output':
                # Check printed output
                expected_output = test_case['expected']
                if expected_output in output or output.strip() == expected_output.strip():
                    return True, output, None
                else:
                    return False, output, f"Output doesn't match expected"
            
            elif test_case['type'] == 'list_comprehension':
                # Check if specific variable contains correct list
                var_name = test_case['var_name']
                expected = test_case['expected']
                if var_name in namespace:
                    if namespace[var_name] == expected:
                        return True, output, None
                    else:
                        return False, output, f"List '{var_name}' has wrong values"
                else:
                    return False, output, f"Variable '{var_name}' not found"
        
        return False, output, "No test cases matched"
        
    except Exception as e:
        sys.stdout = old_stdout
        return False, "", f"Error: {str(e)}"

# --- Initialize session data ---
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(columns=["Name", "Age", "Score", "Can_Retake"])

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# --- School Header ---
st.title("🏫 School of Futuro AI")
st.subheader("Python Basics Quiz (English & Arabic) by Hadjar Naila 💻")
st.write("---")

# --- Choose Role ---
role = st.radio("Select your role:", ["Student", "Teacher"])

# =====================================================================
# 👩‍🎓 STUDENT SIDE
# =====================================================================
if role == "Student":
    st.header("👩‍🎓 Student Access")

    name = st.text_input("Enter your full name:")
    age = st.number_input("Enter your age:", min_value=5, max_value=100, step=1, value=10)

    # Check if student already took the quiz
    can_take_quiz = True
    if name and not st.session_state.results.empty:
        existing = st.session_state.results[st.session_state.results["Name"] == name]
        if not existing.empty and not existing["Can_Retake"].values[0]:
            st.warning(f"⚠️ You already took the test, {name}. Wait for your teacher to allow a retake.")
            st.info(f"Your last score: {existing['Score'].values[0]}/40")
            can_take_quiz = False

    if name and can_take_quiz:
        if st.button("🚀 Start the Test"):
            st.session_state.quiz_started = True
            st.session_state.student_name = name
            st.session_state.student_age = age

    # --- Quiz Section ---
    if st.session_state.get("quiz_started", False):
        st.write("---")
        st.header("🧠 Python Basics Test - Complete Version")
        st.info("📝 This test has 40 questions: 20 Multiple Choice + 10 Code Output + 10 Code Writing")

        # Define all questions and answers
        mc_questions = [
            ("What is the correct way to create a list in Python?", 
             "ما الطريقة الصحيحة لإنشاء قائمة في بايثون؟",
             ["list = (1, 2, 3)", "list = [1, 2, 3]", "list = {1, 2, 3}", "list = <1, 2, 3>"],
             "list = [1, 2, 3]"),
            
            ("How do you access the last item in a list called bikes?",
             "كيف تصل إلى آخر عنصر في قائمة تسمى bikes؟",
             ["bikes[0]", "bikes[-1]", "bikes[last]", "bikes.last()"],
             "bikes[-1]"),
            
            ("What does this code print? print(5 % 2)",
             "ماذا يطبع هذا الكود؟ print(5 % 2)",
             ["2.5", "2", "1", "0"],
             "1"),
            
            ("Which statement correctly checks if a variable age is 18 or greater?",
             "أي عبارة تفحص بشكل صحيح إذا كان المتغير age يساوي 18 أو أكبر؟",
             ["if age = 18:", "if age == 18:", "if age >= 18:", "if age => 18:"],
             "if age >= 18:"),
            
            ("What is the difference between a tuple and a list?",
             "ما الفرق بين tuple و list؟",
             ["Tuples use () and lists use []", "Tuples are immutable, lists are mutable", "Both a and b", "There is no difference"],
             "Both a and b"),
            
            ("How do you add an item to the end of a list?",
             "كيف تضيف عنصرًا في نهاية القائمة؟",
             ["list.add(item)", "list.append(item)", "list.insert(item)", "list.push(item)"],
             "list.append(item)"),
            
            ("What does this code do? bikes = bikes[:]",
             "ماذا يفعل هذا الكود؟ bikes = bikes[:]",
             ["Deletes the list", "Creates a copy of the list", "Reverses the list", "Sorts the list"],
             "Creates a copy of the list"),
            
            ("In a dictionary, what is 'color' in this code? alien = {'color': 'green'}",
             "في القاموس، ما هو 'color' في هذا الكود؟",
             ["A value", "A key", "A method", "A function"],
             "A key"),
            
            ("What does the input() function return?",
             "ما الذي تُرجعه دالة input()؟",
             ["An integer", "A float", "A string", "A boolean"],
             "A string"),
            
            ("How do you convert user input to an integer?",
             "كيف تحول إدخال المستخدم إلى عدد صحيح؟",
             ["int(input())", "input(int)", "integer(input())", "input().int()"],
             "int(input())"),
            
            ("What will range(1, 5) produce?",
             "ماذا ستنتج range(1, 5)؟",
             ["1, 2, 3, 4, 5", "1, 2, 3, 4", "0, 1, 2, 3, 4", "2, 3, 4, 5"],
             "1, 2, 3, 4"),
            
            ("Which loop is best for iterating through a list?",
             "أي حلقة هي الأفضل للتكرار عبر قائمة؟",
             ["while loop", "for loop", "do-while loop", "repeat loop"],
             "for loop"),
            
            ("What does break do in a loop?",
             "ماذا يفعل break في الحلقة؟",
             ["Pauses the loop", "Exits the loop completely", "Skips to the next iteration", "Restarts the loop"],
             "Exits the loop completely"),
            
            ("How do you define a function in Python?",
             "كيف تُعرّف دالة في بايثون؟",
             ["function myFunc():", "def myFunc():", "create myFunc():", "func myFunc():"],
             "def myFunc():"),
            
            ("What is a parameter in a function?",
             "ما هو المعامل (parameter) في الدالة؟",
             ["Information passed to the function", "Information received by the function", "The function's name", "The return value"],
             "Information received by the function"),
            
            ("What does this list comprehension do? squares = [x**2 for x in range(1, 11)]",
             "ماذا يفعل هذا الـ list comprehension؟",
             ["Creates a list of numbers 1-10", "Creates a list of squares from 1-100", "Squares each number in a list", "Creates 10 squared values"],
             "Creates 10 squared values"),
            
            ("How do you access a value in a dictionary?",
             "كيف تصل إلى قيمة في القاموس؟",
             ["dict.get(key)", "dict[key]", "Both a and b", "dict(key)"],
             "Both a and b"),
            
            ("What does elif stand for?",
             "ماذا تعني elif؟",
             ["Else if case", "Else if", "Electronic if", "End if"],
             "Else if"),
            
            ("Which operator checks if two values are NOT equal?",
             "أي عامل يفحص إذا كانت قيمتان غير متساويتين؟",
             ["<>", "!=", "!==", "not="],
             "!="),
            
            ("What does continue do in a loop?",
             "ماذا يفعل continue في الحلقة؟",
             ["Exits the loop", "Pauses the loop", "Skips to the next iteration", "Restarts the entire program"],
             "Skips to the next iteration")
        ]

        code_output_questions = [
            ("numbers = [1, 2, 3, 4, 5]\nprint(numbers[2])", "ما الناتج؟",
             ["1", "2", "3", "4"], "3"),
            ("name = 'alice'\nprint(name.upper())", "ما الناتج؟",
             ["alice", "ALICE", "Alice", "aLICE"], "ALICE"),
            ("for i in range(3):\n    print(i)", "ما الناتج؟",
             ["0 1 2", "1 2 3", "0 1 2 3", "1 2"], "0 1 2"),
            ("age = 17\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')", "ما الناتج؟",
             ["Adult", "Minor", "17", "Error"], "Minor"),
            ("bike = {'brand': 'trek', 'year': 2020}\nprint(bike['brand'])", "ما الناتج؟",
             ["trek", "year", "2020", "brand"], "trek"),
            ("numbers = [1, 2, 3]\nnumbers.append(4)\nprint(len(numbers))", "ما الناتج؟",
             ["3", "4", "5", "Error"], "4"),
            ("x = 10\ny = 5\nprint(x > y and y > 3)", "ما الناتج؟",
             ["True", "False", "10", "5"], "True"),
            ("names = ['amy', 'bob', 'carl']\nprint(names[-1])", "ما الناتج؟",
             ["amy", "bob", "carl", "-1"], "carl"),
            ("def greet(name):\n    return 'Hello, ' + name\nprint(greet('Alice'))", "ما الناتج؟",
             ["Hello, Alice", "Alice", "Hello,", "greet"], "Hello, Alice"),
            ("squares = [x**2 for x in range(1, 4)]\nprint(squares)", "ما الناتج؟",
             ["[1, 2, 3]", "[1, 4, 9]", "[2, 4, 6]", "[1, 4, 9, 16]"], "[1, 4, 9]")
        ]

        # NEW: Code writing questions with test cases
        code_writing_questions = [
            {
                "question_en": "Create a list called colors with three color names (e.g., 'red', 'blue', 'green')",
                "question_ar": "أنشئ قائمة اسمها colors بها ثلاثة أسماء ألوان",
                "test_cases": [{
                    "type": "variable",
                    "var_name": "colors",
                    "expected": lambda x: isinstance(x, list) and len(x) == 3
                }],
                "hint": "colors = ['red', 'blue', 'green']"
            },
            {
                "question_en": "Write a for loop that prints numbers 1 through 5",
                "question_ar": "اكتب حلقة for تطبع الأرقام من 1 إلى 5",
                "test_cases": [{
                    "type": "output",
                    "expected": "1\n2\n3\n4\n5"
                }],
                "hint": "for i in range(1, 6):\n    print(i)"
            },
            {
                "question_en": "Create a dictionary called person with keys 'name' and 'age' (any values)",
                "question_ar": "أنشئ قاموسًا اسمه person بمفاتيح 'name' و 'age'",
                "test_cases": [{
                    "type": "variable",
                    "var_name": "person",
                    "expected": lambda x: isinstance(x, dict) and 'name' in x and 'age' in x
                }],
                "hint": "person = {'name': 'Ali', 'age': 25}"
            },
            {
                "question_en": "Create a variable score = 95, then write an if statement that prints 'Passed' if score > 90",
                "question_ar": "أنشئ متغير score = 95، ثم اكتب عبارة if تطبع 'Passed' إذا كان score > 90",
                "test_cases": [{
                    "type": "output",
                    "expected": "Passed"
                }],
                "hint": "score = 95\nif score > 90:\n    print('Passed')"
            },
            {
                "question_en": "Write a function called add_numbers that takes two parameters and returns their sum",
                "question_ar": "اكتب دالة اسمها add_numbers تأخذ معاملين وتُرجع مجموعهما",
                "test_cases": [{
                    "type": "function",
                    "func_name": "add_numbers",
                    "tests": [((3, 5), 8), ((10, 20), 30), ((0, 0), 0)]
                }],
                "hint": "def add_numbers(a, b):\n    return a + b"
            },
            {
                "question_en": "Create a list comprehension called squares that generates squares of numbers 1-5",
                "question_ar": "أنشئ list comprehension اسمه squares يولد مربعات الأرقام من 1 إلى 5",
                "test_cases": [{
                    "type": "list_comprehension",
                    "var_name": "squares",
                    "expected": [1, 4, 9, 16, 25]
                }],
                "hint": "squares = [x**2 for x in range(1, 6)]"
            },
            {
                "question_en": "Write a while loop that prints numbers 1, 2, 3",
                "question_ar": "اكتب حلقة while تطبع الأرقام 1، 2، 3",
                "test_cases": [{
                    "type": "output",
                    "expected": "1\n2\n3"
                }],
                "hint": "i = 1\nwhile i <= 3:\n    print(i)\n    i += 1"
            },
            {
                "question_en": "Create a list fruits = ['apple', 'banana', 'orange'], then print the first element",
                "question_ar": "أنشئ قائمة fruits = ['apple', 'banana', 'orange']، ثم اطبع العنصر الأول",
                "test_cases": [{
                    "type": "output",
                    "expected": "apple"
                }],
                "hint": "fruits = ['apple', 'banana', 'orange']\nprint(fruits[0])"
            },
            {
                "question_en": "Create a dictionary car = {'brand': 'Toyota'}, then add key 'color' with value 'red'",
                "question_ar": "أنشئ قاموس car = {'brand': 'Toyota'}، ثم أضف مفتاح 'color' بقيمة 'red'",
                "test_cases": [{
                    "type": "variable",
                    "var_name": "car",
                    "expected": lambda x: isinstance(x, dict) and x.get('color') == 'red' and x.get('brand') == 'Toyota'
                }],
                "hint": "car = {'brand': 'Toyota'}\ncar['color'] = 'red'"
            },
            {
                "question_en": "Write code to create a variable name = 'Ahmed' (no input needed)",
                "question_ar": "اكتب كودًا لإنشاء متغير name = 'Ahmed'",
                "test_cases": [{
                    "type": "variable",
                    "var_name": "name",
                    "expected": lambda x: isinstance(x, str) and len(x) > 0
                }],
                "hint": "name = 'Ahmed'"
            }
        ]

        with st.form("quiz_form"):
            st.subheader("📚 Part 1: Multiple Choice (20 questions)")
            mc_answers = []
            for i, (q_en, q_ar, opts, correct) in enumerate(mc_questions):
                st.write(f"**Q{i+1}. {q_en}**")
                st.markdown(f"<p dir='rtl'>{q_ar}</p>", unsafe_allow_html=True)
                answer = st.radio("Select your answer:", opts, key=f"mc_{i}", index=None)
                mc_answers.append(answer)

            st.write("---")
            st.subheader("💻 Part 2: Code Output (10 questions)")
            co_answers = []
            for i, (code, q_ar, opts, correct) in enumerate(code_output_questions):
                st.write(f"**Q{i+21}.**")
                st.code(code, language="python")
                st.markdown(f"<p dir='rtl'>{q_ar}</p>", unsafe_allow_html=True)
                answer = st.radio("Select your answer:", opts, key=f"co_{i}", index=None)
                co_answers.append(answer)

            st.write("---")
            st.subheader("✍️ Part 3: Code Writing (10 questions)")
            st.info("⚡ Your code will be executed and tested automatically!")
            cw_answers = []
            for i, q_data in enumerate(code_writing_questions):
                st.write(f"**Q{i+31}. {q_data['question_en']}**")
                st.markdown(f"<p dir='rtl'>{q_data['question_ar']}</p>", unsafe_allow_html=True)
                answer = st.text_area("Your code:", key=f"cw_{i}", height=100, 
                                     placeholder=f"Example: {q_data['hint']}")
                cw_answers.append(answer)

            submitted = st.form_submit_button("✅ Submit All Answers", type="primary")

        if submitted:
            score = 0
            
            # Grade Part 1: Multiple Choice
            for i, (_, _, _, correct) in enumerate(mc_questions):
                if mc_answers[i] == correct:
                    score += 1
            
            # Grade Part 2: Code Output
            for i, (_, _, _, correct) in enumerate(code_output_questions):
                if co_answers[i] == correct:
                    score += 1
            
            # Grade Part 3: Code Writing (with execution)
            st.write("---")
            st.subheader("🔍 Part 3 Detailed Results:")
            cw_score = 0
            for i, q_data in enumerate(code_writing_questions):
                student_code = cw_answers[i]
                
                if not student_code.strip():
                    st.warning(f"❌ Q{i+31}: No code submitted")
                    continue
                
                # Execute and test the code
                is_correct, output, error = execute_code_safely(student_code, q_data['test_cases'])
                
                if is_correct:
                    cw_score += 1
                    st.success(f"✅ Q{i+31}: Correct!")
                else:
                    st.error(f"❌ Q{i+31}: {error if error else 'Incorrect'}")
                    if output:
                        st.code(f"Output: {output}", language="text")
            
            score += cw_score

            student_name = st.session_state.get("student_name", name)
            student_age = st.session_state.get("student_age", age)
            results = st.session_state.results

            if student_name in results["Name"].values:
                results.loc[results["Name"] == student_name, ["Age", "Score", "Can_Retake"]] = [student_age, score, False]
            else:
                new_row = pd.DataFrame([{"Name": student_name, "Age": student_age, "Score": score, "Can_Retake": False}])
                results = pd.concat([results, new_row], ignore_index=True)

            st.session_state.results = results
            st.session_state.quiz_started = False

            st.balloons()
            st.success(f"🎉 {student_name}, your score is **{score}/40**")
            st.info(f"Part 1 (MC): {sum(1 for i, (_, _, _, c) in enumerate(mc_questions) if mc_answers[i] == c)}/20 | "
                   f"Part 2 (Output): {sum(1 for i, (_, _, _, c) in enumerate(code_output_questions) if co_answers[i] == c)}/10 | "
                   f"Part 3 (Writing): {cw_score}/10")

            if score >= 36:
                st.success("🌟 **Excellent!** You've mastered the basics!")
            elif score >= 30:
                st.info("👏 **Great job!** Review a few concepts.")
            elif score >= 24:
                st.warning("👍 **Good start!** Keep practicing.")
            else:
                st.error("📚 **Review the material and try again.**")

            st.info("Your teacher can see your results. Wait for approval if you want to retake the test.")

# =====================================================================
# 👩‍🏫 TEACHER SIDE
# =====================================================================
elif role == "Teacher":
    st.header("👩‍🏫 Teacher Access")

    password = st.text_input("Enter password:", type="password")

    if password == "admin123":
        st.success("✅ Access granted")
        st.subheader("📊 Students Results")

        if st.session_state.results.empty:
            st.info("No students have taken the quiz yet.")
        else:
            st.dataframe(st.session_state.results, use_container_width=True)

            students = list(st.session_state.results["Name"])
            if students:
                st.write("---")
                st.subheader("🔄 Allow Retake")
                selected_student = st.selectbox("Select student to allow retake:", students)
                if st.button("Allow Retake"):
                    st.session_state.results.loc[
                        st.session_state.results["Name"] == selected_student, "Can_Retake"
                    ] = True
                    st.success(f"✅ {selected_student} can now retake the quiz!")

            st.write("---")
            csv = st.session_state.results.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results (CSV)",
                data=csv,
                file_name="quiz_results.csv",
                mime="text/csv"
            )
    elif password:
        st.error("❌ Wrong password. Try again.")

st.write("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI School")
