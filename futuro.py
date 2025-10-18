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
st.subheader("Python Basics Quiz by Hadjar Naila 💻")
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
            st.info(f"Your last score: {existing['Score'].values[0]}/5")
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

        questions = {
            "What is the output of print(2 + 3 * 4)?": ["14", "20", "24", "Error"],
            "Which of these is a valid variable name?": ["2var", "my-var", "_value", "class"],
            "What keyword is used to define a function?": ["func", "define", "def", "lambda"],
            "What does len([1,2,3]) return?": ["3", "2", "4", "Error"],
            "What is the output of print('Python'[::-1])?": ["nohtyP", "Python", "Error", "nothyP"]
        }
        answers = ["14", "_value", "def", "3", "nohtyP"]

        for i, (q, opts) in enumerate(questions.items()):
            st.write(f"**Q{i+1}. {q}**")
            choice = st.radio("", opts, key=f"q{i}")
            st.session_state.answers[i] = choice

        if st.button("✅ Submit Answers"):
            score = 0
            for i, ans in enumerate(answers):
                if st.session_state.answers[i] == ans:
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

            st.success(f"🎉 {name}, your score is {score}/5")

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
