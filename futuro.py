import streamlit as st
import pandas as pd

# --- Page config ---
st.set_page_config(page_title="Python Quiz - Futuro AI", page_icon="🎓", layout="centered")

# --- School Header ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/AI_logo.svg/1200px-AI_logo.svg.png", width=120)
st.title("🏫 School of Futuro AI")
st.subheader("Python Basics Quiz by Hadjar Naila 💻")

st.write("---")

# --- Student Info Section ---
st.header("👩‍🎓 Student Information")

name = st.text_input("Enter your full name:")
age = st.number_input("Enter your age:", min_value=5, max_value=100, step=1)

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if name and age and not st.session_state.quiz_started:
    if st.button("Start the Test"):
        st.session_state.quiz_started = True
        st.session_state.score = 0
        st.session_state.answers = {}
        st.session_state.name = name
        st.session_state.age = age

# --- Quiz Questions ---
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

        # Save student result
        if "results" not in st.session_state:
            st.session_state.results = pd.DataFrame(columns=["Name", "Age", "Score"])

        new_row = {"Name": st.session_state.name, "Age": st.session_state.age, "Score": score}
        st.session_state.results = pd.concat([st.session_state.results, pd.DataFrame([new_row])], ignore_index=True)

        st.success(f"🎉 {st.session_state.name}, your score is {score}/5")

# --- Results Table ---
if "results" in st.session_state and not st.session_state.quiz_started:
    st.write("---")
    st.header("📊 Students Results")
    st.dataframe(st.session_state.results)

    # Option to download results
    csv = st.session_state.results.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Results (CSV)", csv, "quiz_results.csv", "text/csv")

st.write("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI School")
