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
def execute_student_code(code):
    """
    Execute student code and return output and any errors
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
        
        return True, output, None
        
    except Exception as e:
        sys.stdout = old_stdout
        return False, "", str(e)

def check_programming_challenge(code, output):
    """
    Check if the student's code solves the programming challenge correctly
    Challenge: Print numbers 1-100, but for multiples of 3 print "Fizz", 
    for multiples of 5 print "Buzz", for both print "FizzBuzz"
    """
    expected_output = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            expected_output.append("FizzBuzz")
        elif i % 3 == 0:
            expected_output.append("Fizz")
        elif i % 5 == 0:
            expected_output.append("Buzz")
        else:
            expected_output.append(str(i))
    
    expected_string = "\n".join(expected_output)
    
    # Compare output (strip whitespace)
    if output.strip() == expected_string.strip():
        return True, "Perfect! Your code produces the correct output."
    else:
        # Provide helpful feedback
        output_lines = output.strip().split("\n")
        expected_lines = expected_string.strip().split("\n")
        
        if len(output_lines) != 100:
            return False, f"Your code printed {len(output_lines)} lines, but should print 100 lines."
        
        # Find first mismatch
        for i, (out, exp) in enumerate(zip(output_lines, expected_lines)):
            if out != exp:
                return False, f"Line {i+1} is incorrect. Expected '{exp}' but got '{out}'"
        
        return False, "Output doesn't match expected result."

# --- Initialize session data ---
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(columns=["Name", "Age", "Score", "Can_Retake"])

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "part3_code" not in st.session_state:
    st.session_state.part3_code = ""

if "execution_history" not in st.session_state:
    st.session_state.execution_history = []

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
            st.info(f"Your last score: {existing['Score'].values[0]}/31")
            can_take_quiz = False

    if name and can_take_quiz:
        if st.button("🚀 Start the Test"):
            st.session_state.quiz_started = True
            st.session_state.student_name = name
            st.session_state.student_age = age
            st.session_state.part3_code = ""
            st.session_state.execution_history = []

    # --- Quiz Section ---
    if st.session_state.get("quiz_started", False):
        st.write("---")
        st.header("🧠 Python Basics Test - Complete Version")
        st.info("📝 This test has 31 questions: 20 Multiple Choice + 10 Code Output + 1 Programming Challenge")

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

            submitted = st.form_submit_button("✅ Submit Parts 1 & 2", type="primary")

        if submitted:
            # Calculate score for parts 1 and 2
            part1_score = sum(1 for i, (_, _, _, c) in enumerate(mc_questions) if mc_answers[i] == c)
            part2_score = sum(1 for i, (_, _, _, c) in enumerate(code_output_questions) if co_answers[i] == c)
            
            # Store partial scores
            st.session_state.part1_score = part1_score
            st.session_state.part2_score = part2_score
            st.session_state.mc_answers = mc_answers
            st.session_state.co_answers = co_answers
            
            st.success(f"✅ Parts 1 & 2 submitted! Score so far: {part1_score + part2_score}/30")
            st.info("📝 Now complete Part 3: Programming Challenge below")

        # --- Part 3: Programming Challenge (Outside the form) ---
        st.write("---")
        st.subheader("✍️ Part 3: Programming Challenge (10 points)")
        
        st.markdown("""
        **Q31. FizzBuzz Challenge:**
        
        Write a program that prints numbers from 1 to 100, but:
        - For multiples of 3, print "Fizz" instead of the number
        - For multiples of 5, print "Buzz" instead of the number
        - For multiples of both 3 and 5, print "FizzBuzz"
        - For other numbers, print the number itself
        
        **Example output (first 15 lines):**
        ```
        1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
        ```
        """)
        
        st.markdown("<p dir='rtl'><strong>تحدي FizzBuzz:</strong><br/>اكتب برنامجًا يطبع الأرقام من 1 إلى 100، ولكن:<br/>- لمضاعفات 3، اطبع 'Fizz' بدلاً من الرقم<br/>- لمضاعفات 5، اطبع 'Buzz' بدلاً من الرقم<br/>- لمضاعفات 3 و 5 معًا، اطبع 'FizzBuzz'<br/>- للأرقام الأخرى، اطبع الرقم نفسه</p>", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        
        with col1:
            student_code = st.text_area(
                "Write your code here:",
                value=st.session_state.part3_code,
                height=300,
                placeholder="for i in range(1, 101):\n    # Your code here...",
                key="code_editor"
            )
            
            st.session_state.part3_code = student_code
            
            col_test, col_submit = st.columns(2)
            
            with col_test:
                if st.button("🧪 Test Run", type="secondary", use_container_width=True):
                    if student_code.strip():
                        success, output, error = execute_student_code(student_code)
                        
                        # Add to execution history
                        st.session_state.execution_history.append({
                            "code": student_code,
                            "success": success,
                            "output": output,
                            "error": error
                        })
                        
                        st.rerun()
                    else:
                        st.warning("⚠️ Please write some code first!")
            
            with col_submit:
                if st.button("✅ Submit Final Answer", type="primary", use_container_width=True):
                    if student_code.strip():
                        # Check if parts 1 and 2 were submitted
                        if "part1_score" not in st.session_state:
                            st.error("❌ Please submit Parts 1 & 2 first!")
                        else:
                            success, output, error = execute_student_code(student_code)
                            
                            part3_score = 0
                            if success:
                                is_correct, feedback = check_programming_challenge(student_code, output)
                                if is_correct:
                                    part3_score = 10
                                    st.success(f"🎉 {feedback}")
                                else:
                                    st.error(f"❌ {feedback}")
                            else:
                                st.error(f"❌ Error in your code: {error}")
                            
                            # Calculate final score
                            total_score = st.session_state.part1_score + st.session_state.part2_score + part3_score
                            
                            # Save results
                            student_name = st.session_state.get("student_name", name)
                            student_age = st.session_state.get("student_age", age)
                            results = st.session_state.results

                            if student_name in results["Name"].values:
                                results.loc[results["Name"] == student_name, ["Age", "Score", "Can_Retake"]] = [student_age, total_score, False]
                            else:
                                new_row = pd.DataFrame([{"Name": student_name, "Age": student_age, "Score": total_score, "Can_Retake": False}])
                                results = pd.concat([results, new_row], ignore_index=True)

                            st.session_state.results = results
                            
                            st.balloons()
                            st.success(f"🎉 {student_name}, your final score is **{total_score}/31**")
                            st.info(f"Part 1 (MC): {st.session_state.part1_score}/20 | "
                                   f"Part 2 (Output): {st.session_state.part2_score}/10 | "
                                   f"Part 3 (Challenge): {part3_score}/10")

                            if total_score >= 28:
                                st.success("🌟 **Excellent!** You've mastered Python basics!")
                            elif total_score >= 23:
                                st.info("👏 **Great job!** Keep practicing.")
                            elif total_score >= 18:
                                st.warning("👍 **Good start!** Review the material.")
                            else:
                                st.error("📚 **Keep learning!** Practice more.")

                            st.info("Your teacher can see your results. Wait for approval if you want to retake the test.")
                            
                            # Clear the quiz
                            st.session_state.quiz_started = False
                            st.session_state.execution_history = []
                    else:
                        st.warning("⚠️ Please write some code first!")
        
        with col2:
            st.markdown("### 🔍 Test Results")
            
            if st.session_state.execution_history:
                latest = st.session_state.execution_history[-1]
                
                if latest["success"]:
                    st.success("✅ Code executed successfully!")
                    
                    # Show first 20 lines of output
                    output_lines = latest["output"].strip().split("\n")
                    preview_lines = output_lines[:20]
                    
                    st.text("Output (first 20 lines):")
                    st.code("\n".join(preview_lines), language="text")
                    
                    if len(output_lines) > 20:
                        st.caption(f"... and {len(output_lines) - 20} more lines")
                    
                    st.info(f"Total lines printed: {len(output_lines)}")
                else:
                    st.error("❌ Error in code:")
                    st.code(latest["error"], language="text")
                
                st.caption(f"Total test runs: {len(st.session_state.execution_history)}")
            else:
                st.info("👈 Click 'Test Run' to see your code output here")



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

