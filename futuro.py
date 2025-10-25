import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
import sys
from io import StringIO
import traceback
import base64

# Page configuration
st.set_page_config(
    page_title="AI Robot Homework Helper",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
        transform: scale(1.05);
    }
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    .code-output {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 15px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        margin: 10px 0;
    }
    .success-output {
        background-color: #1a472a;
        color: #7ee081;
    }
    .error-output {
        background-color: #5a1a1a;
        color: #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'code_output' not in st.session_state:
    st.session_state.code_output = ""
if 'code_error' not in st.session_state:
    st.session_state.code_error = ""
if 'user_code' not in st.session_state:
    st.session_state.user_code = '''# My First AI Robot!
print("🤖 ROBOT: Hello! I am a simple AI robot.")
print("🤖 ROBOT: Ask me something or say hi!")

while True:
    user_input = input("\\n👤 YOU: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("🤖 ROBOT: Hi there! Nice to meet you!")
    
    elif "how are you" in user_input:
        print("🤖 ROBOT: I'm great! Always charged up! ⚡")
    
    elif "name" in user_input:
        print("🤖 ROBOT: My name is RoboBot 3000!")
    
    elif "bye" in user_input:
        print("🤖 ROBOT: Goodbye! 👋")
        break
    
    elif "joke" in user_input:
        print("🤖 ROBOT: Why did the robot go on a diet?")
        print("         Because it had too many bytes! 😄")
    
    else:
        print("🤖 ROBOT: I don't understand that yet!")

print("\\n🤖 ROBOT: [Powering down...] zzz...")
'''

if 'uploaded_drawing' not in st.session_state:
    st.session_state.uploaded_drawing = None

# Header
st.title("🤖 AI Robot Homework Helper")
st.subheader("✨ Lesson 1: What is AI? - Interactive Coding & Drawing")

# Student Information
st.markdown("---")
st.header("📝 Student Information")
col1, col2, col3 = st.columns(3)

with col1:
    student_name = st.text_input("👤 Your Name:", placeholder="Enter your name...")
with col2:
    student_age = st.number_input("🎂 Your Age:", min_value=10, max_value=16, value=12)
with col3:
    homework_date = st.date_input("📅 Date:", datetime.now())

# Option Selection
st.markdown("---")
st.header("🎯 Choose Your Homework Option")
option = st.radio(
    "Select ONE option (or do both for extra credit! 🌟)",
    ["💻 Option 1: Improve Your Robot (Coding)", "🎨 Option 2: Design Your Dream Robot (Creative)", "🚀 Both Options!"],
    horizontal=False
)

# Store data for PDF
coding_responses = {}
creative_responses = {}
canvas_image = None

# Option 1: Coding with Live Execution
if option in ["💻 Option 1: Improve Your Robot (Coding)", "🚀 Both Options!"]:
    st.markdown("---")
    st.header("💻 Option 1: Improve Your Robot - Live Coding Environment")
    
    st.write("**✏️ Write your robot code below and test it live!**")
    
    # Code editor
    user_code = st.text_area(
        "Python Code Editor:",
        value=st.session_state.user_code,
        height=400,
        help="Write your Python code here. Add new elif statements for new responses!"
    )
    st.session_state.user_code = user_code
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("▶️ Run Code", type="primary"):
            st.session_state.code_output = ""
            st.session_state.code_error = ""
            
            st.info("📝 Analyzing your code structure...")
            
            try:
                # Check for syntax errors
                compile(user_code, '<string>', 'exec')
                st.session_state.code_output = "✅ Code syntax is correct!\n\n"
                
                # Count the number of elif statements
                elif_count = user_code.count("elif")
                if_count = user_code.count("if ")
                print_count = user_code.count("print(")
                
                st.session_state.code_output += f"📊 Code Analysis:\n"
                st.session_state.code_output += f"  • Found {if_count} 'if' statement(s)\n"
                st.session_state.code_output += f"  • Found {elif_count} 'elif' statement(s)\n"
                st.session_state.code_output += f"  • Print statements: {print_count}\n\n"
                
                if elif_count >= 5:
                    st.session_state.code_output += "🌟 Great job! You've added new responses!\n"
                elif elif_count >= 3:
                    st.session_state.code_output += "👍 Good start! Try adding 1-2 more responses!\n"
                else:
                    st.session_state.code_output += "💡 Try adding at least 2 more 'elif' statements for new responses!\n"
                
                # Check for specific keywords
                keywords = ["food", "fact", "subject", "joke", "color", "hobby", "age", "sport"]
                found_keywords = [kw for kw in keywords if kw in user_code.lower()]
                
                if found_keywords:
                    st.session_state.code_output += f"\n✨ Detected new topics: {', '.join(found_keywords)}\n"
                
                # Check for bonus features
                if "import random" in user_code or "random." in user_code:
                    st.session_state.code_output += "\n🎲 BONUS: Random responses detected!\n"
                
                if "user_name" in user_code or "name =" in user_code:
                    st.session_state.code_output += "🎯 BONUS: Name remembering detected!\n"
                
                st.session_state.code_output += "\n✅ Your code is ready to use!"
                
            except SyntaxError as e:
                st.session_state.code_error = f"❌ Syntax Error at line {e.lineno}:\n{str(e)}\n\n"
                st.session_state.code_error += "💡 Check for missing colons (:), parentheses (), or quotes."
            except Exception as e:
                st.session_state.code_error = f"❌ Error: {str(e)}"
    
    with col2:
        if st.button("🔄 Reset Code"):
            st.session_state.user_code = '''# My First AI Robot!
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
'''
            st.rerun()
    
    with col3:
        if st.button("💡 Show Example"):
            st.session_state.user_code = '''# My Improved AI Robot!
print("🤖 ROBOT: Hello! I am RoboBot 3000!")
print("🤖 ROBOT: Ask me anything!")

while True:
    user_input = input("\\n👤 YOU: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("🤖 ROBOT: Hi there! Nice to meet you!")
    
    elif "how are you" in user_input:
        print("🤖 ROBOT: I'm great! Always charged up! ⚡")
    
    elif "name" in user_input:
        print("🤖 ROBOT: My name is RoboBot 3000!")
    
    elif "food" in user_input or "eat" in user_input:
        print("🤖 ROBOT: I love electricity! It's shocking how good it tastes! ⚡🔌")
    
    elif "fact" in user_input:
        print("🤖 ROBOT: Did you know? The first robot was built in 1954!")
    
    elif "subject" in user_input or "favorite subject" in user_input:
        print("🤖 ROBOT: I love Computer Science! Binary is my first language! 01010")
    
    elif "joke" in user_input:
        print("🤖 ROBOT: Why did the robot go on a diet?")
        print("         Because it had too many bytes! 😄")
    
    elif "bye" in user_input or "goodbye" in user_input:
        print("🤖 ROBOT: Goodbye! 👋")
        break
    
    else:
        print("🤖 ROBOT: Hmm, I don't understand that yet. Try asking something else!")

print("\\n🤖 ROBOT: [Powering down...] zzz...")
'''
            st.rerun()
    
    # Display output
    if st.session_state.code_output:
        st.markdown("### 📤 Output:")
        st.markdown(f'<div class="code-output success-output">{st.session_state.code_output}</div>', unsafe_allow_html=True)
    
    if st.session_state.code_error:
        st.markdown("### ❌ Error:")
        st.markdown(f'<div class="code-output error-output">{st.session_state.code_error}</div>', unsafe_allow_html=True)
    
    # Checklist
    st.markdown("---")
    st.subheader("✅ Checklist - What did you add?")
    col1, col2 = st.columns(2)
    
    with col1:
        coding_responses['food'] = st.checkbox("🍕 Favorite food response")
        coding_responses['fact'] = st.checkbox("🧠 Fun fact response")
    
    with col2:
        coding_responses['subject'] = st.checkbox("📚 Favorite subject response")
        coding_responses['joke'] = st.checkbox("😄 Another joke response")
    
    st.markdown("---")
    st.markdown("**📝 Additional Notes:**")
    coding_responses['notes'] = st.text_area(
        "What else did you add to your robot?",
        placeholder="Describe any other features you added...",
        height=100
    )

# Option 2: Creative Design with Drawing Upload
if option in ["🎨 Option 2: Design Your Dream Robot (Creative)", "🚀 Both Options!"]:
    st.markdown("---")
    st.header("🎨 Option 2: Design Your Dream Robot")
    
    st.subheader("🖌️ Draw Your Robot!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("**Option A: Upload a drawing** (draw on paper and take a photo)")
        uploaded_file = st.file_uploader(
            "Upload your robot drawing (PNG, JPG, JPEG)",
            type=['png', 'jpg', 'jpeg'],
            help="Draw your robot on paper, take a photo, and upload it here!"
        )
        
        if uploaded_file is not None:
            canvas_image = Image.open(uploaded_file)
            st.session_state.uploaded_drawing = canvas_image
            st.image(canvas_image, caption="Your Robot Drawing", use_column_width=True)
    
    with col2:
        st.write("**Option B: Describe your robot**")
        robot_description = st.text_area(
            "Describe what your robot looks like:",
            placeholder="My robot is blue with red eyes, has wheels for legs, mechanical arms with 3 fingers...",
            height=200,
            help="If you can't upload a drawing, describe it in detail!"
        )
        
        if robot_description:
            st.info(f"📝 Your description will be included in the PDF!")
    
    st.markdown("---")
    st.subheader("❓ Answer These Questions About Your Robot:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        creative_responses['name'] = st.text_input(
            "🤖 What is your robot's name?",
            placeholder="Example: RoboHelper 3000"
        )
        
        creative_responses['function'] = st.text_area(
            "⚙️ What does it do?",
            placeholder="Example: My robot helps students with homework by...",
            height=120
        )
    
    with col2:
        creative_responses['help'] = st.text_area(
            "💝 How does it help people?",
            placeholder="Example: It helps people by...",
            height=120
        )
        
        creative_responses['special'] = st.text_area(
            "✨ What makes it special?",
            placeholder="Example: It can understand emotions and...",
            height=120
        )
    
    creative_responses['description'] = robot_description

# Bonus Challenge
st.markdown("---")
st.header("🌟 Bonus Challenge (Optional)")
col1, col2 = st.columns(2)

with col1:
    bonus1 = st.checkbox("🎯 I made the robot remember the user's name")
    bonus1_code = ""
    if bonus1:
        bonus1_code = st.text_area(
            "Show your code for remembering names:",
            placeholder="Example: user_name = input('What is your name?')\nprint(f'Hi {user_name}!')",
            height=100,
            key="bonus1"
        )

with col2:
    bonus2 = st.checkbox("🎲 I added random responses")
    bonus2_code = ""
    if bonus2:
        bonus2_code = st.text_area(
            "Show your code for random responses:",
            placeholder="Example: import random\nresponses = ['Hi!', 'Hello!', 'Hey!']\nprint(random.choice(responses))",
            height=100,
            key="bonus2"
        )

# Generate PDF Button
st.markdown("---")
st.header("📥 Generate Your Homework PDF")

if st.button("📄 Create My Homework PDF!", type="primary"):
    if not student_name:
        st.error("⚠️ Please enter your name first!")
    else:
        with st.spinner("🎨 Creating your beautiful PDF homework sheet..."):
            try:
                # Create PDF
                buffer = io.BytesIO()
                doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
                story = []
                styles = getSampleStyleSheet()
                
                # Custom styles
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=24,
                    textColor=colors.HexColor('#667eea'),
                    spaceAfter=20,
                    alignment=TA_CENTER,
                    fontName='Helvetica-Bold'
                )
                
                heading_style = ParagraphStyle(
                    'CustomHeading',
                    parent=styles['Heading2'],
                    fontSize=16,
                    textColor=colors.HexColor('#764ba2'),
                    spaceAfter=12,
                    spaceBefore=12,
                    fontName='Helvetica-Bold'
                )
                
                normal_style = ParagraphStyle(
                    'CustomNormal',
                    parent=styles['Normal'],
                    fontSize=10,
                    spaceAfter=8
                )
                
                code_style = ParagraphStyle(
                    'Code',
                    parent=styles['Normal'],
                    fontSize=8,
                    fontName='Courier',
                    spaceAfter=2,
                    leftIndent=20
                )
                
                # Title
                story.append(Paragraph("🤖 AI ROBOT HOMEWORK", title_style))
                story.append(Paragraph("Lesson 1: What is AI?", heading_style))
                story.append(Spacer(1, 0.2*inch))
                
                # Student Info Table
                student_data = [
                    ['Student Name:', student_name, 'Age:', str(student_age)],
                    ['Date:', str(homework_date), '', '']
                ]
                student_table = Table(student_data, colWidths=[1.5*inch, 2.5*inch, 0.8*inch, 1*inch])
                student_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f4ff')),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#764ba2')),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 10),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#667eea'))
                ]))
                story.append(student_table)
                story.append(Spacer(1, 0.3*inch))
                
                # Option 1: Coding Section
                if option in ["💻 Option 1: Improve Your Robot (Coding)", "🚀 Both Options!"]:
                    story.append(Paragraph("💻 OPTION 1: IMPROVE YOUR ROBOT", heading_style))
                    story.append(Spacer(1, 0.1*inch))
                    
                    story.append(Paragraph("<b>What I Added:</b>", normal_style))
                    for key, value in coding_responses.items():
                        if key != 'notes' and value:
                            icon = {'food': '🍕', 'fact': '🧠', 'subject': '📚', 'joke': '😄'}.get(key, '✓')
                            story.append(Paragraph(f"• {icon} {key.capitalize()} response", normal_style))
                    
                    if coding_responses.get('notes'):
                        story.append(Spacer(1, 0.1*inch))
                        story.append(Paragraph("<b>Additional Features:</b>", normal_style))
                        story.append(Paragraph(coding_responses['notes'], normal_style))
                    
                    story.append(Spacer(1, 0.15*inch))
                    story.append(Paragraph("<b>My Robot Code:</b>", normal_style))
                    story.append(Spacer(1, 0.05*inch))
                    
                    # Add code with line numbers
                    code_lines = st.session_state.user_code.split('\n')
                    for i, line in enumerate(code_lines[:40], 1):  # Limit to first 40 lines
                        clean_line = line.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;')
                        story.append(Paragraph(f"{i:3d} | {clean_line}", code_style))
                    
                    if len(code_lines) > 40:
                        story.append(Paragraph(f"... ({len(code_lines) - 40} more lines)", code_style))
                    
                    story.append(Spacer(1, 0.2*inch))
                
                # Option 2: Creative Design Section
                if option in ["🎨 Option 2: Design Your Dream Robot (Creative)", "🚀 Both Options!"]:
                    if option == "🚀 Both Options!":
                        story.append(PageBreak())
                    
                    story.append(Paragraph("🎨 OPTION 2: DESIGN YOUR DREAM ROBOT", heading_style))
                    story.append(Spacer(1, 0.15*inch))
                    
                    # Add drawing if available
                    if st.session_state.uploaded_drawing:
                        img_buffer = io.BytesIO()
                        # Resize image to fit
                        img = st.session_state.uploaded_drawing
                        img.thumbnail((450, 300), Image.Resampling.LANCZOS)
                        img.save(img_buffer, format='PNG')
                        img_buffer.seek(0)
                        
                        rl_img = RLImage(img_buffer, width=4*inch, height=2.5*inch)
                        story.append(rl_img)
                        story.append(Spacer(1, 0.15*inch))
                    
                    # Add description if provided
                    if creative_responses.get('description'):
                        story.append(Paragraph("<b>Robot Description:</b>", normal_style))
                        story.append(Paragraph(creative_responses['description'], normal_style))
                        story.append(Spacer(1, 0.1*inch))
                    
                    # Questions and answers
                    questions = [
                        ("🤖 Robot's Name:", creative_responses.get('name', '')),
                        ("⚙️ What does it do:", creative_responses.get('function', '')),
                        ("💝 How it helps people:", creative_responses.get('help', '')),
                        ("✨ What makes it special:", creative_responses.get('special', ''))
                    ]
                    
                    for q, a in questions:
                        if a:
                            story.append(Paragraph(f"<b>{q}</b>", normal_style))
                            story.append(Paragraph(a, normal_style))
                            story.append(Spacer(1, 0.08*inch))
                
                # Bonus Challenge
                if bonus1 or bonus2:
                    story.append(Spacer(1, 0.15*inch))
                    story.append(Paragraph("🌟 BONUS CHALLENGE", heading_style))
                    
                    if bonus1:
                        story.append(Paragraph("🎯 <b>Remember User Name</b>", normal_style))
                        if bonus1_code:
                            for line in bonus1_code.split('\n'):
                                clean_line = line.replace('<', '&lt;').replace('>', '&gt;')
                                story.append(Paragraph(clean_line, code_style))
                        story.append(Spacer(1, 0.08*inch))
                    
                    if bonus2:
                        story.append(Paragraph("🎲 <b>Random Responses</b>", normal_style))
                        if bonus2_code:
                            for line in bonus2_code.split('\n'):
                                clean_line = line.replace('<', '&lt;').replace('>', '&gt;')
                                story.append(Paragraph(clean_line, code_style))
                
                # Footer
                story.append(Spacer(1, 0.4*inch))
                footer_style = ParagraphStyle(
                    'Footer',
                    parent=styles['Normal'],
                    fontSize=12,
                    textColor=colors.HexColor('#764ba2'),
                    alignment=TA_CENTER,
                    fontName='Helvetica-Bold'
                )
                story.append(Paragraph("📚 Bring to Next Class! 🚀", footer_style))
                story.append(Spacer(1, 0.1*inch))
                story.append(Paragraph("Have fun learning AI!", footer_style))
                
                # Build PDF
                doc.build(story)
                buffer.seek(0)
                
                # Success message
                st.success("✅ Your homework PDF is ready!")
                
                # Download button
                st.download_button(
                    label="💾 Download Your Homework PDF",
                    data=buffer,
                    file_name=f"AI_Homework_{student_name.replace(' ', '_')}_{homework_date}.pdf",
                    mime="application/pdf",
                    type="primary"
                )
                
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Error creating PDF: {str(e)}")
                st.error("Please make sure you've filled in all required fields.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 20px;'>
    <h3>🎓 Tips for Success:</h3>
    <p>✓ Test your code with the "Run Code" button!</p>
    <p>✓ Upload a clear photo of your robot drawing!</p>
    <p>✓ Be creative with your responses!</p>
    <p>✓ Answer all questions completely!</p>
    <p>✓ Download your PDF when you're done!</p>
</div>
""", unsafe_allow_html=True)
