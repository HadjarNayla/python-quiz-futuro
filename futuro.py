import streamlit as st
import pandas as pd

# --- Page config ---
st.set_page_config(page_title="Python Quiz - Futuro AI", page_icon="🎓", layout="centered")

# --- Initialize session data ---
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(columns=["Name", "Age", "Score", "Can_Retake"])

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "role" not in st.session_state:
    st.session_state.role = None

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
    st.session_state.role = "Student"
    st.header("👩‍🎓 Student Access")

    name = st.text_input("Enter your full name:")
    age = st.number_input("Enter your age:", min_value=5, max_value=100, step=1)

    # Check if student already took the quiz
    if name:
        existing = st.session_state.results[st.session_state.results["Name"] == name]

        if not existing.empty and not existing["Can_Retake"].values[0]:
            st.warning(f"⚠️ You already took the test, {name}. Wait for your teacher to allow a retake.")
            st.info(f"Your last score: {existing['Score'].values[0]}/20")
        else:
            if st.button("Start the Test"):
                st.session_state.quiz_started = True
                st.session_state.score = 0
                st.session_state.answers = {}
                st.session_state.name = name
                st.session_state.age = age

    # --- Quiz Section ---
    if st.session_state.quiz_started:
        st.write("---")
        st.header("🧠 Python Basics Test")

        questions = [
            ("What is the output of print(3 + 4 * 2)?", "ما ناتج الكود print(3 + 4 * 2)؟", ["14", "11", "7", "Error"]),
            ("Which of the following is a valid variable name?", "أي من الأسماء التالية صالح كمتغير؟", ["2name", "first_name", "my-name", "class"]),
            ("Which function is used to get input from the user?", "ما الدالة التي تُستخدم لإدخال البيانات من المستخدم؟", ["get()", "input()", "scan()", "read()"]),
            ("What is the correct file extension for Python files?", "ما هو الامتداد الصحيح لملفات بايثون؟", [".pt", ".py", ".pyt", ".txt"]),
            ("Which symbol is used for comments in Python?", "ما الرمز المستخدم للتعليقات في بايثون؟", ["//", "#", "/* */", "<!-- -->"]),
            ("What data type is the value: 3.14?", "ما نوع البيانات للقيمة 3.14؟", ["int", "float", "str", "bool"]),
            ("Which function checks the type of a variable?", "ما الدالة التي تُستخدم لمعرفة نوع المتغير؟", ["typeof()", "type()", "check()", "dataType()"]),
            ("What is the output of len('Python')?", "ما ناتج الدالة len('Python')؟", ["6", "5", "7", "Error"]),
            ("What will print(10 // 3) output?", "ما ناتج print(10 // 3)؟", ["3.33", "3", "4", "Error"]),
            ("Which operator is used for exponentiation (power)?", "ما العامل المستخدم لرفع الأس (القوة)؟", ["^", "**", "%", "//"]),
            ("What keyword is used for a condition?", "ما الكلمة المفتاحية المستخدمة لكتابة شرط؟", ["when", "if", "else", "loop"]),
            ("Which of the following evaluates to True?", "أي من العبارات التالية نتيجتها True؟", ["5 > 10", "10 == 10", "3 != 3", "7 < 5"]),
            ("Which keyword starts a for loop?", "ما الكلمة المفتاحية التي تبدأ بها حلقة for؟", ["loop", "iterate", "for", "repeat"]),
            ("What is the output of: for i in range(3): print(i)?", "ما ناتج الكود: for i in range(3): print(i)؟", ["0 1 2", "1 2 3", "0 1 2 3", "Error"]),
            ("Which statement stops a loop early?", "ما الجملة التي تُستخدم لإيقاف الحلقة مبكرًا؟", ["exit", "stop", "break", "return"]),
            ("How do you access the first element of a list named fruits?", "كيف نصل إلى أول عنصر في قائمة اسمها fruits؟", ["fruits[0]", "fruits(0)", "fruits{0}", "first(fruits)"]),
            ("What does mylist.append('x') do?", "ماذا تفعل الدالة mylist.append('x')؟", ["Deletes x", "Adds x to the list", "Sorts list", "Creates a copy"]),
            ("Which keyword defines a function in Python?", "ما الكلمة المفتاحية التي تُستخدم لتعريف دالة؟", ["function", "def", "define", "lambda"]),
            ("What will the following code print?\n\ndef add(a,b):\n\treturn a+b\nprint(add(2,3))", "ماذا سيطبع هذا الكود؟", ["5", "23", "Error", "a+b"]),
            ("What is the output of bool(0)?", "ما ناتج الدالة bool(0)؟", ["True", "False", "0", "None"])
        ]

        answers = [
            "11", "first_name", "input()", ".py", "#",
            "float", "type()", "6", "3", "**",
            "if", "10 == 10", "for", "0 1 2", "break",
            "fruits[0]", "Adds x to the list", "def", "5", "False"
        ]

        for i, (q_en, q_ar, opts) in enumerate(questions):
            st.write(f"**Q{i+1}. {q_en}**")
            st.write(f"{q_ar}")
            choice = st.radio("", opts, key=f"q{i}")
            st.session_state.answers[i] = choice

        if st.button("✅ Submit Answers"):
            score = 0
            for i, ans in enumerate(answers):
                if st.session_state.answers.get(i) == ans:
                    score += 1
            st.session_state.score = score
            st.session_state.quiz_started = False

            # Save or update student result
            results = st.session_state.results
            if name in results["Name"].values:
                results.loc[results["Name"] == name, ["Age", "Score", "Can_Retake"]] = [age, score, False]
            else:
                new_row = {"Name": name, "Age": age, "Score": score, "Can_Retake": False}
                results = pd.concat([results, pd.DataFrame([new_row])], ignore_index=True)
            st.session_state.results = results

            st.success(f"🎉 {name}, your score is {score}/20")

# =====================================================================
# 👩‍🏫 TEACHER SIDE
# =====================================================================
elif role == "Teacher":
    st.session_state.role = "Teacher"
    st.header("👩‍🏫 Teacher Access")

    password = st.text_input("Enter password:", type="password")

    if password == "admin123":  # You can change this password
        st.success("✅ Access granted")

        st.subheader("📊 Students Results")
        st.dataframe(st.session_state.results)

        # --- Allow student to retake test ---
        students = list(st.session_state.results["Name"])
        if students:
            selected_student = st.selectbox("Select student to allow retake:", students)
            if st.button("Allow Retake"):
                st.session_state.results.loc[
                    st.session_state.results["Name"] == selected_student, "Can_Retake"
                ] = True
                st.success(f"{selected_student} can now retake the quiz!")

        # --- Download results ---
        csv = st.session_state.results.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Results (CSV)", csv, "quiz_results.csv", "text/csv")
    elif password:
        st.error("❌ Wrong password. Try again.")

st.write("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI School")
