import streamlit as st
from PIL import Image
from datetime import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

# --- Page configuration ---
st.set_page_config(
    page_title="AI Robot Homework Helper",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .stButton>button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white; font-size: 18px; font-weight: bold;
        padding: 15px 30px; border-radius: 10px; border: none; width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
        transform: scale(1.05);
    }
    h1, h2, h3 { color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stNumberInput>div>div>input {
        border-radius: 10px; border: 2px solid #667eea;
    }
    .code-output {
        background-color: #1e1e1e; color: #d4d4d4;
        padding: 15px; border-radius: 10px;
        font-family: 'Courier New', monospace;
        margin: 10px 0;
    }
    .success-output { background-color: #1a472a; color: #7ee081; }
    .error-output { background-color: #5a1a1a; color: #ff6b6b; }
</style>
""", unsafe_allow_html=True)

# --- Initialize session state ---
for key, default in {
    "code_output": "",
    "code_error": "",
    "user_code": '''# My First AI Robot!
print("🤖 ROBOT: Hello! I am a simple AI robot.")
print("🤖 ROBOT: Ask me something or say hi!")

while True:
    user_input = input("\\n👤 YOU: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("🤖 ROBOT: Hi there! Nice to meet you!")
    
    elif "bye" in user_input:
        print("🤖 ROBOT: Goodbye! 👋")
        break
    
    else:
        print("🤖 ROBOT: I don't understand that yet!")

print("\\n🤖 ROBOT: [Powering down...] zzz...")'''
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

if "uploaded_drawing" not in st.session_state:
    st.session_state.uploaded_drawing = None

# --- Header ---
st.title("🤖 AI Robot Homework Helper")
st.subheader("✨ Lesson 1: What is AI? - Interactive Coding & Drawing")

# --- Student Info ---
st.markdown("---")
st.header("📝 Student Information")
col1, col2, col3 = st.columns(3)
student_name = col1.text_input("👤 Your Name:", placeholder="Enter your name...")
student_age = col2.number_input("🎂 Your Age:", min_value=10, max_value=16, value=12)
homework_date = col3.date_input("📅 Date:", datetime.now())

# --- Option Selection ---
st.markdown("---")
st.header("🎯 Choose Your Homework Option")
option = st.radio(
    "Select ONE option (or do both for extra credit! 🌟)",
    ["💻 Option 1: Improve Your Robot (Coding)",
     "🎨 Option 2: Design Your Dream Robot (Creative)",
     "🚀 Both Options!"]
)

coding_responses = {}
creative_responses = {}

# --- Option 1: Coding ---
if option in ["💻 Option 1: Improve Your Robot (Coding)", "🚀 Both Options!"]:
    st.markdown("---")
    st.header("💻 Option 1: Improve Your Robot")

    user_code = st.text_area("Python Code Editor:",
                             value=st.session_state.user_code,
                             height=400)
    st.session_state.user_code = user_code

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("▶️ Run Code"):
            st.session_state.code_output, st.session_state.code_error = "", ""
            try:
                compile(user_code, "<string>", "exec", dont_inherit=True)
                st.session_state.code_output = "✅ Code syntax is correct!\n\n"

                elif_count = user_code.count("elif")
                if_count = user_code.count("if ")
                print_count = user_code.count("print(")

                st.session_state.code_output += (
                    f"📊 Code Analysis:\n"
                    f"• Found {if_count} 'if' statement(s)\n"
                    f"• Found {elif_count} 'elif' statement(s)\n"
                    f"• Print statements: {print_count}\n\n"
                )

                if elif_count >= 5:
                    st.session_state.code_output += "🌟 Great job! You've added many responses!\n"
                elif elif_count >= 3:
                    st.session_state.code_output += "👍 Good start! Try adding a few more!\n"
                else:
                    st.session_state.code_output += "💡 Add at least 2 more 'elif' statements!\n"

            except SyntaxError as e:
                st.session_state.code_error = f"❌ Syntax Error at line {e.lineno}: {e}\n"
            except Exception as e:
                st.session_state.code_error = f"❌ Error: {str(e)}"

    with col2:
        if st.button("🔄 Reset Code"):
            st.session_state.user_code = st.session_state.user_code.split("\n")[0]  # reset basic version
            st.experimental_rerun()

    with col3:
        if st.button("💡 Show Example"):
            st.session_state.user_code = """# My Improved AI Robot!
print("🤖 ROBOT: Hello! I am RoboBot 3000!")
print("🤖 ROBOT: Ask me anything!")
"""
            st.experimental_rerun()

    # Display results
    if st.session_state.code_output:
        st.markdown("### 📤 Output:")
        st.markdown(f"<div class='code-output success-output'>{st.session_state.code_output}</div>", unsafe_allow_html=True)
    if st.session_state.code_error:
        st.markdown("### ❌ Error:")
        st.markdown(f"<div class='code-output error-output'>{st.session_state.code_error}</div>", unsafe_allow_html=True)

# --- PDF Export ---
st.markdown("---")
st.header("📥 Generate Your Homework PDF")

if st.button("📄 Create My Homework PDF!"):
    if not student_name:
        st.error("⚠️ Please enter your name first!")
    else:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "CustomTitle", parent=styles["Heading1"],
            fontSize=24, textColor=colors.HexColor("#667eea"),
            alignment=TA_CENTER, fontName="Helvetica-Bold"
        )

        story.append(Paragraph("🤖 AI ROBOT HOMEWORK", title_style))
        story.append(Spacer(1, 0.2 * inch))
        story.append(Paragraph(f"👤 Student: {student_name}", styles["Normal"]))
        story.append(Paragraph(f"🎂 Age: {student_age}", styles["Normal"]))
        story.append(Paragraph(f"📅 Date: {homework_date}", styles["Normal"]))

        story.append(Spacer(1, 0.3 * inch))
        story.append(Paragraph("💻 Code Snippet:", styles["Heading2"]))

        for line in st.session_state.user_code.split("\n")[:30]:
            safe_line = (line.replace("&", "&amp;")
                             .replace("<", "&lt;")
                             .replace(">", "&gt;"))
            story.append(Paragraph(safe_line, ParagraphStyle("Code", fontName="Courier", fontSize=9)))

        doc.build(story)
        buffer.seek(0)
        st.download_button(
            "💾 Download Your Homework PDF",
            data=buffer,
            file_name=f"AI_Homework_{student_name.replace(' ', '_')}.pdf",
            mime="application/pdf"
        )
        st.success("✅ PDF Created Successfully!")
