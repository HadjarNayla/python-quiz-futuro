import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io

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
</style>
""", unsafe_allow_html=True)

# Header
st.title("🤖 AI Robot Homework Helper")
st.subheader("✨ Lesson 1: What is AI?")

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

# Option 1: Coding
if option in ["💻 Option 1: Improve Your Robot (Coding)", "🚀 Both Options!"]:
    st.markdown("---")
    st.header("💻 Option 1: Improve Your Robot")
    st.write("**Add at least TWO new responses to your robot:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        food_checked = st.checkbox("🍕 Favorite food response")
        food_response = ""
        if food_checked:
            food_response = st.text_area(
                "What will your robot say about food?",
                placeholder="Example: I love electricity! ⚡",
                key="food"
            )
        
        fact_checked = st.checkbox("🧠 Fun fact response")
        fact_response = ""
        if fact_checked:
            fact_response = st.text_area(
                "What fun fact will your robot share?",
                placeholder="Example: Did you know robots never sleep?",
                key="fact"
            )
    
    with col2:
        subject_checked = st.checkbox("📚 Favorite subject response")
        subject_response = ""
        if subject_checked:
            subject_response = st.text_area(
                "What subject does your robot like?",
                placeholder="Example: I love Math! Numbers are my friends!",
                key="subject"
            )
        
        joke_checked = st.checkbox("😄 Another joke response")
        joke_response = ""
        if joke_checked:
            joke_response = st.text_area(
                "What joke will your robot tell?",
                placeholder="Example: Why did the robot cross the road? To charge on the other side!",
                key="joke"
            )
    
    # Code preview
    if any([food_checked, fact_checked, subject_checked, joke_checked]):
        st.subheader("📝 Your Code Preview:")
        code = "# My Improved Robot Code\n\n"
        
        if food_checked and food_response:
            code += f'''elif "food" in user_input:
    print("🤖 ROBOT: {food_response}")
\n'''
        
        if fact_checked and fact_response:
            code += f'''elif "fact" in user_input:
    print("🤖 ROBOT: {fact_response}")
\n'''
        
        if subject_checked and subject_response:
            code += f'''elif "subject" in user_input:
    print("🤖 ROBOT: {subject_response}")
\n'''
        
        if joke_checked and joke_response:
            code += f'''elif "joke" in user_input:
    print("🤖 ROBOT: {joke_response}")
\n'''
        
        st.code(code, language="python")

# Option 2: Creative Design
robot_name = ""
robot_function = ""
robot_help = ""
robot_special = ""

if option in ["🎨 Option 2: Design Your Dream Robot (Creative)", "🚀 Both Options!"]:
    st.markdown("---")
    st.header("🎨 Option 2: Design Your Dream Robot")
    
    st.subheader("🖼️ Draw Your Robot")
    st.write("📝 Describe your robot drawing (we'll add this to your worksheet):")
    robot_drawing_description = st.text_area(
        "Describe what your robot looks like:",
        placeholder="Example: My robot is blue with red eyes, has wheels for legs, and mechanical arms...",
        height=100
    )
    
    st.markdown("---")
    st.subheader("❓ Answer These Questions:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        robot_name = st.text_input(
            "🤖 What is your robot's name?",
            placeholder="Example: RoboHelper 3000"
        )
        
        robot_function = st.text_area(
            "⚙️ What does it do?",
            placeholder="Example: My robot helps students with homework...",
            height=100
        )
    
    with col2:
        robot_help = st.text_area(
            "💝 How does it help people?",
            placeholder="Example: It helps people by...",
            height=100
        )
        
        robot_special = st.text_area(
            "✨ What makes it special?",
            placeholder="Example: It can understand emotions and...",
            height=100
        )

# Bonus Challenge
st.markdown("---")
st.header("🌟 Bonus Challenge (Optional)")
bonus1 = st.checkbox("🎯 Make robot remember your name")
bonus1_description = ""
if bonus1:
    bonus1_description = st.text_area(
        "How will you implement this?",
        placeholder="Describe your approach...",
        key="bonus1_desc"
    )

bonus2 = st.checkbox("🎲 Add random responses")
bonus2_description = ""
if bonus2:
    bonus2_description = st.text_area(
        "How will you implement this?",
        placeholder="Describe your approach...",
        key="bonus2_desc"
    )

# Generate Image Button
st.markdown("---")
st.header("📥 Generate Your Homework Sheet")

if st.button("🎨 Create My Homework Image!"):
    if not student_name:
        st.error("⚠️ Please enter your name first!")
    else:
        # Create image
        img_width = 1200
        img_height = 2400
        
        # Create a white background
        img = Image.new('RGB', (img_width, img_height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Try to use a nice font, fallback to default
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            heading_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
            small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        except:
            title_font = ImageFont.load_default()
            heading_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Colors
        purple = (102, 126, 234)
        dark_purple = (118, 75, 162)
        light_bg = (246, 248, 255)
        
        # Draw header background
        draw.rectangle([0, 0, img_width, 200], fill=purple)
        
        # Title
        draw.text((img_width//2, 60), "🤖 AI ROBOT HOMEWORK", font=title_font, fill='white', anchor='mm')
        draw.text((img_width//2, 140), "Lesson 1: What is AI?", font=heading_font, fill='white', anchor='mm')
        
        y_position = 250
        
        # Student Info Box
        draw.rectangle([50, y_position, img_width-50, y_position+120], fill=light_bg, outline=purple, width=3)
        draw.text((100, y_position+30), f"Student: {student_name}", font=text_font, fill=dark_purple)
        draw.text((100, y_position+70), f"Age: {student_age}  |  Date: {homework_date}", font=text_font, fill=dark_purple)
        
        y_position += 170
        
        # Option 1: Coding Section
        if option in ["💻 Option 1: Improve Your Robot (Coding)", "🚀 Both Options!"]:
            draw.rectangle([50, y_position, img_width-50, y_position+50], fill=purple)
            draw.text((100, y_position+25), "💻 OPTION 1: IMPROVE YOUR ROBOT", font=heading_font, fill='white', anchor='lm')
            y_position += 80
            
            responses = []
            if food_checked and food_response:
                responses.append(f"🍕 Food: {food_response}")
            if fact_checked and fact_response:
                responses.append(f"🧠 Fact: {fact_response}")
            if subject_checked and subject_response:
                responses.append(f"📚 Subject: {subject_response}")
            if joke_checked and joke_response:
                responses.append(f"😄 Joke: {joke_response}")
            
            for resp in responses:
                # Word wrap
                words = resp.split()
                lines = []
                current_line = []
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    if len(test_line) <= 60:
                        current_line.append(word)
                    else:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(' '.join(current_line))
                
                for line in lines:
                    draw.text((100, y_position), line, font=text_font, fill='black')
                    y_position += 40
                y_position += 20
        
        # Option 2: Creative Design Section
        if option in ["🎨 Option 2: Design Your Dream Robot (Creative)", "🚀 Both Options!"]:
            y_position += 30
            draw.rectangle([50, y_position, img_width-50, y_position+50], fill=dark_purple)
            draw.text((100, y_position+25), "🎨 OPTION 2: DESIGN YOUR DREAM ROBOT", font=heading_font, fill='white', anchor='lm')
            y_position += 80
            
            if robot_drawing_description:
                draw.text((100, y_position), "Robot Description:", font=heading_font, fill=dark_purple)
                y_position += 50
                
                # Word wrap for description
                words = robot_drawing_description.split()
                lines = []
                current_line = []
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    if len(test_line) <= 70:
                        current_line.append(word)
                    else:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(' '.join(current_line))
                
                for line in lines:
                    draw.text((100, y_position), line, font=text_font, fill='black')
                    y_position += 40
            
            y_position += 30
            
            questions = [
                (f"🤖 Robot Name: {robot_name}", robot_name),
                (f"⚙️ What it does: {robot_function}", robot_function),
                (f"💝 How it helps: {robot_help}", robot_help),
                (f"✨ What makes it special: {robot_special}", robot_special)
            ]
            
            for q_text, q_value in questions:
                if q_value:
                    draw.rectangle([80, y_position, img_width-80, y_position+5], fill=purple)
                    y_position += 20
                    
                    # Word wrap
                    words = q_text.split()
                    lines = []
                    current_line = []
                    for word in words:
                        test_line = ' '.join(current_line + [word])
                        if len(test_line) <= 70:
                            current_line.append(word)
                        else:
                            lines.append(' '.join(current_line))
                            current_line = [word]
                    if current_line:
                        lines.append(' '.join(current_line))
                    
                    for line in lines:
                        draw.text((100, y_position), line, font=text_font, fill='black')
                        y_position += 40
                    y_position += 20
        
        # Bonus Challenge Section
        if bonus1 or bonus2:
            y_position += 30
            draw.rectangle([50, y_position, img_width-50, y_position+50], fill=(255, 215, 0))
            draw.text((100, y_position+25), "🌟 BONUS CHALLENGE", font=heading_font, fill=dark_purple, anchor='lm')
            y_position += 80
            
            if bonus1:
                draw.text((100, y_position), "🎯 Remember user name", font=text_font, fill='black')
                y_position += 40
                if bonus1_description:
                    words = bonus1_description.split()
                    lines = []
                    current_line = []
                    for word in words:
                        test_line = ' '.join(current_line + [word])
                        if len(test_line) <= 70:
                            current_line.append(word)
                        else:
                            lines.append(' '.join(current_line))
                            current_line = [word]
                    if current_line:
                        lines.append(' '.join(current_line))
                    
                    for line in lines:
                        draw.text((120, y_position), line, font=small_font, fill='black')
                        y_position += 35
                y_position += 20
            
            if bonus2:
                draw.text((100, y_position), "🎲 Random responses", font=text_font, fill='black')
                y_position += 40
                if bonus2_description:
                    words = bonus2_description.split()
                    lines = []
                    current_line = []
                    for word in words:
                        test_line = ' '.join(current_line + [word])
                        if len(test_line) <= 70:
                            current_line.append(word)
                        else:
                            lines.append(' '.join(current_line))
                            current_line = [word]
                    if current_line:
                        lines.append(' '.join(current_line))
                    
                    for line in lines:
                        draw.text((120, y_position), line, font=small_font, fill='black')
                        y_position += 35
        
        # Footer
        y_position = img_height - 150
        draw.rectangle([0, y_position, img_width, img_height], fill=purple)
        draw.text((img_width//2, y_position+40), "📚 Bring to Next Class!", font=heading_font, fill='white', anchor='mm')
        draw.text((img_width//2, y_position+90), "Have fun learning AI! 🚀", font=text_font, fill='white', anchor='mm')
        
        # Save to BytesIO
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        # Display the image
        st.success("✅ Your homework sheet is ready!")
        st.image(buf, caption=f"{student_name}'s AI Robot Homework", use_column_width=True)
        
        # Download button
        st.download_button(
            label="💾 Download Your Homework Sheet",
            data=buf,
            file_name=f"AI_Homework_{student_name.replace(' ', '_')}.png",
            mime="image/png"
        )
        
        st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 20px;'>
    <h3>🎓 Tips for Success:</h3>
    <p>✓ Be creative with your responses!</p>
    <p>✓ Test your code before submitting</p>
    <p>✓ Have fun and learn something new!</p>
</div>
""", unsafe_allow_html=True)
