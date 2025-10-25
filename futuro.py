import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Python Quiz - Futuro AI", page_icon="🎓", layout="centered")

# --- HEADER ---
st.title("🎓 Python Quiz - Futuro School")
st.subheader("Created by Teacher: Hadjar Naila")

st.markdown("---")

# --- QUIZ CREATION FORM ---
st.write("### 🧠 Create Your Quiz")

title = st.text_input("Enter Quiz Title (e.g., Python Basics Test)")
teacher = st.text_input("Teacher Name", value="Hadjar Naila")
school = st.text_input("School Name", value="Futuro School")
quiz_date = st.date_input("Date", value=datetime.today())

st.write("Enter your questions and answers below (one per block):")
st.info("Format: Write the question, then the correct answer below it.")

# Input area for questions
num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=5)
questions = []

for i in range(num_questions):
    q = st.text_area(f"Question {i+1}", placeholder="Write your question here")
    a = st.text_input(f"Correct answer for Q{i+1}", placeholder="Write the correct answer here")
    questions.append({"question": q, "answer": a})

# --- PDF GENERATION FUNCTION ---
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, self.title, 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def generate_pdf(title, teacher, school, quiz_date, questions):
    pdf = PDF()
    pdf.title = title
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"School: {school}", ln=True)
    pdf.cell(0, 10, f"Teacher: {teacher}", ln=True)
    pdf.cell(0, 10, f"Date: {quiz_date.strftime('%d/%m/%Y')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Quiz Questions:", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    for i, item in enumerate(questions, 1):
        if item["question"]:
            pdf.multi_cell(0, 10, f"Q{i}: {item['question']}")
            pdf.multi_cell(0, 10, f"Answer: {item['answer']}")
            pdf.ln(5)

    file_name = "Python_Quiz.pdf"
    pdf.output(file_name)
    return file_name

# --- BUTTON TO GENERATE PDF ---
if st.button("📄 Generate PDF"):
    if title.strip() == "" or not any(q["question"].strip() for q in questions):
        st.warning("⚠️ Please enter a title and at least one question.")
    else:
        pdf_file = generate_pdf(title, teacher, school, quiz_date, questions)
        st.success("✅ PDF generated successfully!")
        with open(pdf_file, "rb") as f:
            st.download_button(
                "⬇️ Download Quiz PDF",
                f,
                file_name=pdf_file,
                mime="application/pdf"
            )

st.markdown("---")
st.caption("Made with ❤️ by Hadjar Naila | Futuro AI")
