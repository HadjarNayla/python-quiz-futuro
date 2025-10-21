import streamlit as st
import pandas as pd
import sys
from io import StringIO

# --- Page config ---
st.set_page_config(page_title="Python Quiz - Futuro AI (Bilingual)", page_icon="🎓", layout="centered")

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
        return True, "Perfect! Your code produces the correct output.\nممتاز! الكود الخاص بك ينتج المخرجات الصحيحة."
    else:
        # Provide helpful feedback
        output_lines = output.strip().split("\n") if output.strip() else []
        expected_lines = expected_string.strip().split("\n")
        
        if len(output_lines) != 100:
            return False, f"Your code printed {len(output_lines)} lines, but should print 100 lines.\nالكود الخاص بك طبع {len(output_lines)} سطرًا، بينما يجب أن يطبع 100 سطر."
        
        # Find first mismatch
        for i, (out, exp) in enumerate(zip(output_lines, expected_lines)):
            if out != exp:
                return False, f"Line {i+1} is incorrect. Expected '{exp}' but got '{out}'.\nالسطر {i+1} غير صحيح. المتوقع '{exp}' لكن تم الحصول على '{out}'."
        
        return False, "Output doesn't match expected result.\nالمخرجات لا تتطابق مع النتيجة المتوقعة."

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
role = st.radio("Select your role: / اختر دورك:", ["Student / طالب", "Teacher / معلم"])

# =====================================================================
# 👩‍🎓 STUDENT SIDE
# =====================================================================
if role.startswith("Student"):
    st.header("👩‍🎓 Student Access / وصول الطالب")

    name = st.text_input("Enter your full name: / أدخل اسمك الكامل:")
    age = st.number_input("Enter your age: / أدخل عمرك:", min_value=5, max_value=100, step=1, value=10)

    # Check if student already took the quiz
    can_take_quiz = True
    if name and not st.session_state.results.empty:
        existing = st.session_state.results[st.session_state.results["Name"] == name]
        if not existing.empty and not existing["Can_Retake"].values[0]:
            st.warning(f"⚠️ You already took the test, {name}. Wait for your teacher to allow a retake.\n⚠️ لقد اجتزت الاختبار بالفعل، {name}. انتظر إذن المعلم لإعادة الاختبار.")
            st.info(f"Your last score: {existing['Score'].values[0]}/31\nدرجتك الأخيرة: {existing['Score'].values[0]}/31")
            can_take_quiz = False

    if name and can_take_quiz:
        if st.button("🚀 Start the Test / ابدأ الاختبار"):
            st.session_state.quiz_started = True
            st.session_state.student_name = name
            st.session_state.student_age = age
            st.session_state.part3_code = ""
            st.session_state.execution_history = []

    # --- Quiz Section ---
    if st.session_state.get("quiz_started", False):
        st.write("---")
        st.header("🧠 Python Basics Test - Complete Version / اختبار أساسيات بايثون - النسخة الكاملة")
        st.info("📝 This test has 31 questions: 20 Multiple Choice + 10 Code Output + 1 Programming Challenge\n\n📝 يتكون هذا الاختبار من 31 سؤالًا: 20 اختيار من متعدد + 10 مخرجات كود + 1 تحدي برمجي")

        # Define all questions and answers (each option has English and Arabic text)
        mc_questions = [
            {
                "en": "What is the correct way to create a list in Python?",
                "ar": "ما الطريقة الصحيحة لإنشاء قائمة في بايثون؟",
                "opts": [
                    ("list = (1, 2, 3)", "القائمة = (1، 2، 3)"),
                    ("list = [1, 2, 3]", "القائمة = [1، 2، 3]"),
                    ("list = {1, 2, 3}", "القائمة = {1، 2، 3}"),
                    ("list = <1, 2, 3>", "القائمة = <1، 2، 3>")
                ],
                "answer_index": 1
            },
            {
                "en": "How do you access the last item in a list called bikes?",
                "ar": "كيف تصل إلى آخر عنصر في قائمة تسمى bikes؟",
                "opts": [
                    ("bikes[0]", "bikes[0]"),
                    ("bikes[-1]", "bikes[-1]"),
                    ("bikes[last]", "bikes[last]"),
                    ("bikes.last()", "bikes.last()")
                ],
                "answer_index": 1
            },
            {
                "en": "What does this code print? print(5 % 2)",
                "ar": "ماذا يطبع هذا الكود؟ print(5 % 2)",
                "opts": [
                    ("2.5", "2.5"),
                    ("2", "2"),
                    ("1", "1"),
                    ("0", "0")
                ],
                "answer_index": 2
            },
            {
                "en": "Which statement correctly checks if a variable age is 18 or greater?",
                "ar": "أي عبارة تفحص بشكل صحيح إذا كان المتغير age يساوي 18 أو أكبر؟",
                "opts": [
                    ("if age = 18:", "if age = 18:"),
                    ("if age == 18:", "if age == 18:"),
                    ("if age >= 18:", "if age >= 18:"),
                    ("if age => 18:", "if age => 18:")
                ],
                "answer_index": 2
            },
            {
                "en": "What is the difference between a tuple and a list?",
                "ar": "ما الفرق بين tuple و list؟",
                "opts": [
                    ("Tuples use () and lists use []", "Tuples تستخدم () و lists تستخدم []"),
                    ("Tuples are immutable, lists are mutable", "Tuples غير قابلة للتغيير، lists قابلة للتغيير"),
                    ("Both a and b", "كلا الخيارين a و b"),
                    ("There is no difference", "لا يوجد فرق")
                ],
                "answer_index": 2
            },
            {
                "en": "How do you add an item to the end of a list?",
                "ar": "كيف تضيف عنصرًا في نهاية القائمة؟",
                "opts": [
                    ("list.add(item)", "list.add(item)"),
                    ("list.append(item)", "list.append(item)"),
                    ("list.insert(item)", "list.insert(item)"),
                    ("list.push(item)", "list.push(item)")
                ],
                "answer_index": 1
            },
            {
                "en": "What does this code do? bikes = bikes[:]",
                "ar": "ماذا يفعل هذا الكود؟ bikes = bikes[:]",
                "opts": [
                    ("Deletes the list", "يحذف القائمة"),
                    ("Creates a copy of the list", "يُنشئ نسخة من القائمة"),
                    ("Reverses the list", "يعكس القائمة"),
                    ("Sorts the list", "يرتب القائمة")
                ],
                "answer_index": 1
            },
            {
                "en": "In a dictionary, what is 'color' in this code? alien = {'color': 'green'}",
                "ar": "في القاموس، ما هو 'color' في هذا الكود؟",
                "opts": [
                    ("A value", "قيمة"),
                    ("A key", "مفتاح"),
                    ("A method", "دالة"),
                    ("A function", "دالة (Function)")
                ],
                "answer_index": 1
            },
            {
                "en": "What does the input() function return?",
                "ar": "ما الذي تُرجعه دالة input()؟",
                "opts": [
                    ("An integer", "عدد صحيح"),
                    ("A float", "عدد عشري"),
                    ("A string", "نص (String)"),
                    ("A boolean", "قيمة منطقية (Boolean)")
                ],
                "answer_index": 2
            },
            {
                "en": "How do you convert user input to an integer?",
                "ar": "كيف تحول إدخال المستخدم إلى عدد صحيح؟",
                "opts": [
                    ("int(input())", "int(input())"),
                    ("input(int)", "input(int)"),
                    ("integer(input())", "integer(input())"),
                    ("input().int()", "input().int()")
                ],
                "answer_index": 0
            },
            {
                "en": "What will range(1, 5) produce?",
                "ar": "ماذا ستنتج range(1, 5)؟",
                "opts": [
                    ("1, 2, 3, 4, 5", "1، 2، 3، 4، 5"),
                    ("1, 2, 3, 4", "1، 2، 3، 4"),
                    ("0, 1, 2, 3, 4", "0، 1، 2، 3، 4"),
                    ("2, 3, 4, 5", "2، 3، 4، 5")
                ],
                "answer_index": 1
            },
            {
                "en": "Which loop is best for iterating through a list?",
                "ar": "أي حلقة هي الأفضل للتكرار عبر قائمة؟",
                "opts": [
                    ("while loop", "حلقة while"),
                    ("for loop", "حلقة for"),
                    ("do-while loop", "حلقة do-while"),
                    ("repeat loop", "حلقة repeat")
                ],
                "answer_index": 1
            },
            {
                "en": "What does break do in a loop?",
                "ar": "ماذا يفعل break في الحلقة؟",
                "opts": [
                    ("Pauses the loop", "يوقف الحلقة مؤقتًا"),
                    ("Exits the loop completely", "يخرج من الحلقة تمامًا"),
                    ("Skips to the next iteration", "يتخطى إلى التكرار التالي"),
                    ("Restarts the loop", "يعيد تشغيل الحلقة")
                ],
                "answer_index": 1
            },
            {
                "en": "How do you define a function in Python?",
                "ar": "كيف تُعرّف دالة في بايثون؟",
                "opts": [
                    ("function myFunc():", "function myFunc():"),
                    ("def myFunc():", "def myFunc():"),
                    ("create myFunc():", "create myFunc():"),
                    ("func myFunc():", "func myFunc():")
                ],
                "answer_index": 1
            },
            {
                "en": "What is a parameter in a function?",
                "ar": "ما هو المعامل (parameter) في الدالة؟",
                "opts": [
                    ("Information passed to the function", "معلومات تُمرَّر إلى الدالة"),
                    ("Information received by the function", "معلومات تستقبلها الدالة"),
                    ("The function's name", "اسم الدالة"),
                    ("The return value", "قيمة الإرجاع")
                ],
                "answer_index": 0
            },
            {
                "en": "What does this list comprehension do? squares = [x**2 for x in range(1, 11)]",
                "ar": "ماذا يفعل هذا الـ list comprehension؟",
                "opts": [
                    ("Creates a list of numbers 1-10", "ينشئ قائمة بالأعداد 1-10"),
                    ("Creates a list of squares from 1-100", "ينشئ قائمة بالمربعات من 1-100"),
                    ("Squares each number in a list", "يربع كل رقم في القائمة"),
                    ("Creates 10 squared values", "ينشئ 10 قيم مربعة")
                ],
                "answer_index": 3
            },
            {
                "en": "How do you access a value in a dictionary?",
                "ar": "كيف تصل إلى قيمة في القاموس؟",
                "opts": [
                    ("dict.get(key)", "dict.get(key)"),
                    ("dict[key]", "dict[key]"),
                    ("Both a and b", "كلا الخيارين a و b"),
                    ("dict(key)", "dict(key)")
                ],
                "answer_index": 2
            },
            {
                "en": "What does elif stand for?",
                "ar": "ماذا تعني elif؟",
                "opts": [
                    ("Else if case", "حالة else if"),
                    ("Else if", "else if"),
                    ("Electronic if", "Electronic if"),
                    ("End if", "End if")
                ],
                "answer_index": 1
            },
            {
                "en": "Which operator checks if two values are NOT equal?",
                "ar": "أي عامل يفحص إذا كانت قيمتان غير متساويتين؟",
                "opts": [
                    ("<>", "<>") ,
                    ("!=", "!="),
                    ("!==", "!=="),
                    ("not=", "not=")
                ],
                "answer_index": 1
            },
            {
                "en": "What does continue do in a loop?",
                "ar": "ماذا يفعل continue في الحلقة؟",
                "opts": [
                    ("Exits the loop", "يخرج من الحلقة"),
                    ("Pauses the loop", "يوقف الحلقة مؤقتًا"),
                    ("Skips to the next iteration", "يتخطى إلى التكرار التالي"),
                    ("Restarts the entire program", "يعيد تشغيل البرنامج بأكمله")
                ],
                "answer_index": 2
            }
        ]

        code_output_questions = [
            {
                "code": "numbers = [1, 2, 3, 4, 5]\nprint(numbers[2])",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                "answer_index": 2
            },
            {
                "code": "name = 'alice'\nprint(name.upper())",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("alice", "alice"), ("ALICE", "ALICE"), ("Alice", "Alice"), ("aLICE", "aLICE")],
                "answer_index": 1
            },
            {
                "code": "for i in range(3):\n    print(i)",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("0 1 2", "0 1 2"), ("1 2 3", "1 2 3"), ("0 1 2 3", "0 1 2 3"), ("1 2", "1 2")],
                "answer_index": 0
            },
            {
                "code": "age = 17\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("Adult", "Adult"), ("Minor", "Minor"), ("17", "17"), ("Error", "خطأ")],
                "answer_index": 1
            },
            {
                "code": "bike = {'brand': 'trek', 'year': 2020}\nprint(bike['brand'])",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("trek", "trek"), ("year", "year"), ("2020", "2020"), ("brand", "brand")],
                "answer_index": 0
            },
            {
                "code": "numbers = [1, 2, 3]\nnumbers.append(4)\nprint(len(numbers))",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("3", "3"), ("4", "4"), ("5", "5"), ("Error", "خطأ")],
                "answer_index": 1
            },
            {
                "code": "x = 10\ny = 5\nprint(x > y and y > 3)",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("True", "True"), ("False", "False"), ("10", "10"), ("5", "5")],
                "answer_index": 0
            },
            {
                "code": "names = ['amy', 'bob', 'carl']\nprint(names[-1])",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("amy", "amy"), ("bob", "bob"), ("carl", "carl"), ("-1", "-1")],
                "answer_index": 2
            },
            {
                "code": "def greet(name):\n    return 'Hello, ' + name\nprint(greet('Alice'))",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("Hello, Alice", "Hello, Alice"), ("Alice", "Alice"), ("Hello,", "Hello,"), ("greet", "greet")],
                "answer_index": 0
            },
            {
                "code": "squares = [x**2 for x in range(1, 4)]\nprint(squares)",
                "en_q": "What is the output?",
                "ar_q": "ما الناتج؟",
                "opts": [("[1, 2, 3]", "[1, 2, 3]"), ("[1, 4, 9]", "[1, 4, 9]"), ("[2, 4, 6]", "[2, 4, 6]"), ("[1, 4, 9, 16]", "[1, 4, 9, 16]")],
                "answer_index": 1
            }
        ]

        # Render form for parts 1 & 2
        with st.form("quiz_form"):
            st.subheader("📚 Part 1: Multiple Choice (20 questions) / الجزء الأول: اختيار من متعدد (20 سؤالًا)")
            mc_answers = []
            for i, q in enumerate(mc_questions):
                st.write(f"**Q{i+1}. {q['en']}**")
                st.markdown(f"<p dir='rtl'>{q['ar']}</p>", unsafe_allow_html=True)

                # Prepare options: we will show each option on two lines (English then Arabic)
                opts = q['opts']
                def format_opt(idx, opts=opts):
                    en_opt, ar_opt = opts[idx]
                    return f"{en_opt}\n{ar_opt}"

                choice_index = st.radio(
                    "Select your answer: / اختر إجابتك:",
                    options=list(range(len(opts))),
                    format_func=lambda x, opts=opts: format_opt(x),
                    key=f"mc_{i}",
                    index=None
                )
                mc_answers.append(choice_index)

            st.write("---")
            st.subheader("💻 Part 2: Code Output (10 questions) / الجزء الثاني: مخرجات الكود (10 أسئلة)")
            co_answers = []
            for i, q in enumerate(code_output_questions):
                st.write(f"**Q{i+21}. {q['en_q']}**")
                st.markdown(f"<p dir='rtl'>{q['ar_q']}</p>", unsafe_allow_html=True)
                st.code(q['code'], language="python")

                opts = q['opts']
                def format_co_opt(idx, opts=opts):
                    en_opt, ar_opt = opts[idx]
                    return f"{en_opt}\n{ar_opt}"

                choice_index = st.radio(
                    "Select your answer: / اختر إجابتك:",
                    options=list(range(len(opts))),
                    format_func=lambda x, opts=opts: format_co_opt(x),
                    key=f"co_{i}",
                    index=None
                )
                co_answers.append(choice_index)

            submitted = st.form_submit_button("✅ Submit Parts 1 & 2 / إرسال الجزئين 1 و 2")

        if submitted:
            # Calculate score for parts 1 and 2
            part1_score = 0
            for i, q in enumerate(mc_questions):
                if mc_answers[i] == q['answer_index']:
                    part1_score += 1
            part2_score = 0
            for i, q in enumerate(code_output_questions):
                if co_answers[i] == q['answer_index']:
                    part2_score += 1
            
            # Store partial scores
            st.session_state.part1_score = part1_score
            st.session_state.part2_score = part2_score
            st.session_state.mc_answers = mc_answers
            st.session_state.co_answers = co_answers
            
            st.success(f"✅ Parts 1 & 2 submitted! Score so far: {part1_score + part2_score}/30\n✅ تم إرسال الجزئين 1 و 2! مجموع النقاط حتى الآن: {part1_score + part2_score}/30")
            st.info("📝 Now complete Part 3: Programming Challenge below / الآن أكمِل الجزء 3: التحدي البرمجي أدناه")

        # --- Part 3: Programming Challenge (Outside the form) ---
        st.write("---")
        st.subheader("✍️ Part 3: Programming Challenge (10 points) / الجزء الثالث: التحدي البرمجي (10 نقاط)")
        
        st.markdown("""
        **Q31. FizzBuzz Challenge:**
        
        Write a program that prints numbers from 1 to 100, but:
        - For multiples of 3, print "Fizz" instead of the number
        - For multiples of 5, print "Buzz" instead of the number
        - For multiples of both 3 and 5, print "FizzBuzz"
        - For other numbers, print the number itself
        """)
        
        st.markdown("<p dir='rtl'><strong>تحدي FizzBuzz:</strong><br/>اكتب برنامجًا يطبع الأرقام من 1 إلى 100، ولكن:<br/>- لمضاعفات 3، اطبع 'Fizz' بدلاً من الرقم<br/>- لمضاعفات 5، اطبع 'Buzz' بدلاً من الرقم<br/>- لمضاعفات 3 و 5 معًا، اطبع 'FizzBuzz'<br/>- للأرقام الأخرى، اطبع الرقم نفسه</p>", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        
        with col1:
            student_code = st.text_area(
                "Write your code here: / اكتب كودك هنا:",
                value=st.session_state.part3_code,
                height=300,
                placeholder="for i in range(1, 101):\n    # Your code here...\n# for example: ...",
                key="code_editor"
            )
            
            st.session_state.part3_code = student_code
            
            col_test, col_submit = st.columns(2)
            
            with col_test:
                if st.button("🧪 Test Run / تجربة تشغيل", type="secondary", use_container_width=True):
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
                        st.warning("⚠️ Please write some code first! / الرجاء كتابة الكود أولًا!")
            
            with col_submit:
                if st.button("✅ Submit Final Answer / إرسال الإجابة النهائية", type="primary", use_container_width=True):
                    if student_code.strip():
                        # Check if parts 1 and 2 were submitted
                        if "part1_score" not in st.session_state:
                            st.error("❌ Please submit Parts 1 & 2 first! / الرجاء إرسال الجزئين 1 و 2 أولًا!")
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
                                st.error(f"❌ Error in your code: {error} / خطأ في الكود: {error}")
                            
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
                            st.success(f"🎉 {student_name}, your final score is **{total_score}/31**\n🎉 {student_name}، درجتك النهائية هي **{total_score}/31**")
                            st.info(f"Part 1 (MC): {st.session_state.part1_score}/20 | Part 2 (Output): {st.session_state.part2_score}/10 | Part 3 (Challenge): {part3_score}/10\nالجزء 1 (اختيار من متعدد): {st.session_state.part1_score}/20 | الجزء 2 (مخرجات): {st.session_state.part2_score}/10 | الجزء 3 (تحدي): {part3_score}/10")

                            if total_score >= 28:
                                st.success("🌟 Excellent! You've mastered Python basics!\n🌟 ممتاز! لقد أتقنت أساسيات بايثون!")
                            elif total_score >= 23:
                                st.info("👏 Great job! Keep practicing.\n👏 عمل رائع! استمر في التدريب.")
                            elif total_score >= 18:
                                st.warning("👍 Good start! Review the material.\n👍 بداية جيدة! راجع المادة.")
                            else:
                                st.error("📚 Keep learning! Practice more.\n📚 استمر في التعلم! مارس أكثر.")

                            st.info("Your teacher can see your results. Wait for approval if you want to retake the test.\nيمكن لمعلمك رؤية نتائجك. انتظر الموافقة إذا رغبت في إعادة الاختبار.")
                            
                            # Clear the quiz
                            st.session_state.quiz_started = False
                            st.session_state.execution_history = []
                    else:
                        st.warning("⚠️ Please write some code first! / الرجاء كتابة الكود أولًا!")
        
        with col2:
            st.markdown("### 🔍 Test Results / نتائج التشغيل")
            
            if st.session_state.execution_history:
                latest = st.session_state.execution_history[-1]
                
                if latest["success"]:
                    st.success("✅ Code executed successfully! / ✅ تم تنفيذ الكود بنجاح!")
                    
                    # Show first 20 lines of output
                    output_lines = latest["output"].strip().split("\n") if latest["output"].strip() else []
                    preview_lines = output_lines[:20]
                    
                    st.text("Output (first 20 lines): / المخرجات (أول 20 سطر):")
                    st.code("\n".join(preview_lines), language="text")
                    
                    if len(output_lines) > 20:
                        st.caption(f"... and {len(output_lines) - 20} more lines / ... و {len(output_lines) - 20} أسطر أخرى")
                    
                    st.info(f"Total lines printed: {len(output_lines)} / إجمالي الأسطر المطبوعة: {len(output_lines)}")
                else:
                    st.error("❌ Error in code: / ❌ خطأ في الكود:")
                    st.code(latest["error"], language="text")
                
                st.caption(f"Total test runs: {len(st.session_state.execution_history)} / إجمالي محاولات التشغيل: {len(st.session_state.execution_history)}")
            else:
                st.info("👈 Click 'Test Run' to see your code output here / اضغط 'تجربة تشغيل' لرؤية مخرجات كودك هنا")
                st.markdown("""
                **Tips / نصائح:**
                - Use a for loop with range(1, 101) / استخدم حلقة for مع range(1, 101)
                - Check divisibility with % operator / افحص القابلية للقسمة باستخدام العامل %
                - Use if/elif/else statements / استخدم if/elif/else
                - Print each result on a new line / اطبع كل نتيجة في سطر جديد
                """)

# =====================================================================
# 👩‍🏫 TEACHER SIDE
# =====================================================================
elif role.startswith("Teacher"):
    st.header("👩‍🏫 Teacher Access / وصول المعلم")

    password = st.text_input("Enter password: / أدخل كلمة المرور:", type="password")

    if password == "admin123":
        st.success("✅ Access granted / ✅ تم منح الوصول")
        st.subheader("📊 Students Results / نتائج الطلاب")

        if st.session_state.results.empty:
            st.info("No students have taken the quiz yet. / لم يأخذ أي طالب الاختبار بعد.")
        else:
            st.dataframe(st.session_state.results, use_container_width=True)

            students = list(st.session_state.results["Name"])
            if students:
                st.write("---")
                st.subheader("🔄 Allow Retake / السماح بإعادة الاختبار")
                selected_student = st.selectbox("Select student to allow retake: / اختر طالبًا للسماح له بإعادة الاختبار:", students)
                if st.button("Allow Retake / السماح بإعادة الاختبار"):
                    st.session_state.results.loc[
                        st.session_state.results["Name"] == selected_student, "Can_Retake"
                    ] = True
                    st.success(f"✅ {selected_student} can now retake the quiz! / يمكن الآن لـ {selected_student} إعادة الاختبار!")

            st.write("---")
            csv = st.session_state.results.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results (CSV) / تنزيل النتائج (CSV)",
                data=csv,
                file_name="quiz_results.csv",
                mime="text/csv"
            )
    elif password:
        st.error("❌ Wrong password. Try again. / كلمة المرور خاطئة. حاول مرة أخرى.")

st.write("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI School / صنع بحب بواسطة حاجة نايلة | مدرسة فيوتشرو AI")
