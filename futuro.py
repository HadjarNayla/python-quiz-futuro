import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Python Quiz Results").sheet1
    return sheet

# ============================================================
# 🔐 Connect to Google Sheets
# ============================================================
def connect_to_gsheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Python Quiz Results").sheet1  # Your Google Sheet name
    return sheet


# ============================================================
# 🎨 Streamlit Config
# ============================================================
st.set_page_config(page_title="Python Quiz - Futuro AI", page_icon="🎓", layout="centered")

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

# ============================================================
# 🏫 App Header
# ============================================================
st.title("🏫 School of Futuro AI")
st.subheader("Python Basics Quiz (English & Arabic) by Hadjar Naila 💻")
st.write("---")

# ============================================================
# 🎭 Choose Role
# ============================================================
role = st.radio("Select your role:", ["Student", "Teacher"])

# ============================================================
# 👩‍🎓 STUDENT SIDE
# ============================================================
if role == "Student":
    st.header("👩‍🎓 Student Access")

    name = st.text_input("Enter your full name:")
    age = st.number_input("Enter your age:", min_value=5, max_value=100, step=1, value=10)

    # Connect to Google Sheet
    sheet = connect_to_gsheet()
    data = sheet.get_all_records()
    results = pd.DataFrame(data)

    # Check if student can take quiz
    can_take_quiz = True
    if name and not results.empty:
        existing = results[results["Name"] == name]
        if not existing.empty and not existing["Can_Retake"].values[0]:
            st.warning(f"⚠️ You already took the test, {name}. Wait for your teacher to allow a retake.")
            st.info(f"Your last score: {existing['Score'].values[0]}/40")
            can_take_quiz = False

    if name and can_take_quiz:
        if st.button("🚀 Start the Test"):
            st.session_state.quiz_started = True
            st.session_state.student_name = name
            st.session_state.student_age = age

    # ============================================================
    # 🧠 Quiz Section
    # ============================================================
    if st.session_state.get("quiz_started", False):
        st.write("---")
        st.header("🧠 Python Basics Test - Complete Version")
        st.info("📝 This test has 40 questions: 20 MCQs + 10 Code Output + 10 Code Writing")

        # ===================== MULTIPLE CHOICE =====================
        mc_questions = [
            ("What is the correct way to create a list in Python?", "ما الطريقة الصحيحة لإنشاء قائمة في بايثون؟",
             ["list = (1, 2, 3)", "list = [1, 2, 3]", "list = {1, 2, 3}", "list = <1, 2, 3>"], "list = [1, 2, 3]"),
            ("How do you access the last item in a list called bikes?",
             "كيف تصل إلى آخر عنصر في قائمة تسمى bikes؟",
             ["bikes[0]", "bikes[-1]", "bikes[last]", "bikes.last()"], "bikes[-1]"),
            ("What does this code print? print(5 % 2)", "ماذا يطبع هذا الكود؟ print(5 % 2)",
             ["2.5", "2", "1", "0"], "1"),
            ("Which statement checks if variable age ≥ 18?",
             "أي عبارة تفحص إذا كان المتغير age يساوي أو أكبر من 18؟",
             ["if age = 18:", "if age == 18:", "if age >= 18:", "if age => 18:"], "if age >= 18:"),
            ("What is the difference between tuple and list?",
             "ما الفرق بين tuple و list؟",
             ["Tuples use () and lists use []", "Tuples are immutable, lists are mutable", "Both a and b", "No difference"], "Both a and b"),
            ("How to add an item to the end of a list?", "كيف تضيف عنصرًا في نهاية القائمة؟",
             ["list.add(item)", "list.append(item)", "list.insert(item)", "list.push(item)"], "list.append(item)"),
            ("What does bikes = bikes[:] do?", "ماذا يفعل هذا الكود؟ bikes = bikes[:]",
             ["Deletes the list", "Copies the list", "Reverses list", "Sorts list"], "Copies the list"),
            ("In {'color': 'green'}, what is 'color'?", "في {'color': 'green'}، ما هو 'color'؟",
             ["Value", "Key", "Method", "Function"], "Key"),
            ("What does input() return?", "ما الذي تُرجعه input()؟",
             ["int", "float", "string", "bool"], "string"),
            ("Convert input to int:", "حوّل إدخال المستخدم إلى int:",
             ["int(input())", "input(int)", "integer(input())", "input().int()"], "int(input())"),
            ("What will range(1,5) produce?", "ماذا تنتج range(1,5)؟",
             ["1,2,3,4,5", "1,2,3,4", "0,1,2,3,4", "2,3,4,5"], "1,2,3,4"),
            ("Best loop for list iteration?", "أفضل حلقة للتكرار عبر قائمة؟",
             ["while", "for", "do-while", "repeat"], "for"),
            ("What does break do?", "ماذا يفعل break؟",
             ["Pause", "Exit loop", "Skip", "Restart"], "Exit loop"),
            ("Define a function:", "كيف تُعرّف دالة؟",
             ["function myFunc():", "def myFunc():", "create myFunc():", "func myFunc():"], "def myFunc():"),
            ("Parameter in function?", "ما هو المعامل في الدالة؟",
             ["Passed info", "Received info", "Function name", "Return value"], "Received info"),
            ("squares = [x**2 for x in range(1,11)] does what?", "ماذا يفعل هذا؟",
             ["List 1–10", "Squares 1–100", "Squares 1–10", "10 squared"], "Squares 1–10"),
            ("Access dict value?", "كيف تصل إلى قيمة في القاموس؟",
             ["dict.get(key)", "dict[key]", "Both", "dict(key)"], "Both"),
            ("elif means?", "ماذا تعني elif؟",
             ["Else if", "End if", "Else case", "Error"], "Else if"),
            ("Operator for not equal?", "العامل لعدم المساواة؟",
             ["<>", "!=", "!==", "not="], "!="),
            ("continue does what?", "ماذا يفعل continue؟",
             ["Exit", "Pause", "Skip iteration", "Restart"], "Skip iteration")
        ]

        # ===================== CODE OUTPUT =====================
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

        # ===================== CODE WRITING =====================
        code_writing_questions = [
            ("Create a list called colors with three color names.", "أنشئ قائمة اسمها colors بها ثلاثة أسماء ألوان.", ["colors", "=", "["]),
            ("Write a for loop that prints numbers 1–5.", "اكتب حلقة for تطبع الأرقام من 1 إلى 5.", ["for", "range", "1", "6"]),
            ("Create a dictionary called person with keys 'name' and 'age'.", "أنشئ قاموسًا اسمه person بمفاتيح 'name' و 'age'.", ["person", "=", "{", "name", "age"]),
            ("if statement checking score > 90.", "اكتب if تفحص إذا كان score > 90.", ["if", "score", ">", "90"]),
            ("Function add_numbers with 2 params returning sum.", "دالة add_numbers تأخذ معاملين وتُرجع مجموعهما.", ["def", "add_numbers", "return"]),
            ("List comprehension for squares 1–10.", "list comprehension لمربعات الأرقام من 1 إلى 10.", ["**2", "for", "range", "1", "11"]),
            ("While loop counting 1–3.", "حلقة while تعد من 1 إلى 3.", ["while", "<=", "3"]),
            ("Access first element of fruits.", "الوصول إلى أول عنصر في fruits.", ["fruits[0]"]),
            ("Add key='color', value='red' to dict car.", "أضف مفتاح 'color' بقيمة 'red' إلى car.", ["car", "color", "red"]),
            ("Get user input in variable name.", "أدخل المستخدم في متغير اسمه name.", ["name", "=", "input"])
        ]

        # ===================== FORM =====================
        with st.form("quiz_form"):
            st.subheader("📚 Part 1: Multiple Choice (20 questions)")
            mc_answers = []
            for i, (q_en, q_ar, opts, correct) in enumerate(mc_questions):
                st.write(f"**Q{i+1}. {q_en}**")
                st.markdown(f"<p dir='rtl'>{q_ar}</p>", unsafe_allow_html=True)
                mc_answers.append(st.radio("Answer:", opts, key=f"mc_{i}", index=None))

            st.write("---")
            st.subheader("💻 Part 2: Code Output (10 questions)")
            co_answers = []
            for i, (code, q_ar, opts, correct) in enumerate(code_output_questions):
                st.code(code, language="python")
                st.markdown(f"<p dir='rtl'>{q_ar}</p>", unsafe_allow_html=True)
                co_answers.append(st.radio("Answer:", opts, key=f"co_{i}", index=None))

            st.write("---")
            st.subheader("✍️ Part 3: Code Writing (10 questions)")
            cw_answers = []
            for i, (q_en, q_ar, keywords) in enumerate(code_writing_questions):
                st.write(f"**Q{i+31}. {q_en}**")
                st.markdown(f"<p dir='rtl'>{q_ar}</p>", unsafe_allow_html=True)
                cw_answers.append(st.text_area("Your code:", key=f"cw_{i}", height=80))

            submitted = st.form_submit_button("✅ Submit All Answers")

        if submitted:
            score = 0
            for i, (_, _, _, correct) in enumerate(mc_questions):
                if mc_answers[i] == correct: score += 1
            for i, (_, _, _, correct) in enumerate(code_output_questions):
                if co_answers[i] == correct: score += 1
            for i, (_, _, keywords) in enumerate(code_writing_questions):
                if all(kw.lower() in cw_answers[i].lower() for kw in keywords): score += 1

            st.balloons()
            st.success(f"🎉 {name}, your score is **{score}/40**")

            sheet.append_row([name, age, score, False])
            st.info("✅ Result saved to Google Sheets")

# ============================================================
# 👩‍🏫 TEACHER SIDE
# ============================================================
elif role == "Teacher":
    st.header("👩‍🏫 Teacher Access")
    password = st.text_input("Enter password:", type="password")

    if password == "admin123":
        st.success("✅ Access granted")
        sheet = connect_to_gsheet()
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No students yet.")
        else:
            st.dataframe(df, use_container_width=True)
    elif password:
        st.error("❌ Wrong password.")

st.write("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI School")


