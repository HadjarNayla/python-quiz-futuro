import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Learn Python - Futuro Skills Academy",
    page_icon="🐍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 3em;
        font-weight: bold;
    }
    .instructor {
        text-align: center;
        color: #F18F01;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    .code-output {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🐍 Learn Python</p>', unsafe_allow_html=True)
st.markdown('<p class="instructor">by Hadjar Naila | Futuro Skills Academy</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Lessons")
lessons = [
    "🏠 Start Here",
    "1️⃣ First Program",
    "2️⃣ Variables",
    "3️⃣ Math",
    "4️⃣ Text",
    "5️⃣ Lists",
    "6️⃣ If/Else",
    "7️⃣ Loops",
    "8️⃣ Functions",
    "🎮 Projects"
]

selected = st.sidebar.radio("", lessons)
st.sidebar.markdown("---")
st.sidebar.info("💡 Try the code yourself!")

# Lessons
if selected == "🏠 Start Here":
    st.balloons()
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Welcome! 👋
        
        **You'll learn:**
        - Python basics
        - Write real code
        - Build projects
        
        **No experience needed!**
        
        👈 Start with Lesson 1
        """)
    
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=150)

elif selected == "1️⃣ First Program":
    st.header("Your First Program")
    
    st.code('print("Hello, World!")', language="python")
    st.markdown('<div class="code-output">Hello, World!</div>', unsafe_allow_html=True)
    
    st.markdown("### Try it! ✏️")
    msg = st.text_input("Your message:", "Hello, Python!")
    if st.button("▶ Run"):
        st.markdown(f'<div class="code-output">{msg}</div>', unsafe_allow_html=True)

elif selected == "2️⃣ Variables":
    st.header("Variables")
    
    st.markdown("Variables store data:")
    
    st.code("""name = "Hadjar"
age = 25
print(name)
print(age)""", language="python")
    
    st.markdown("### Create a variable:")
    col1, col2 = st.columns(2)
    with col1:
        var_name = st.text_input("Name:", "my_var")
    with col2:
        var_value = st.text_input("Value:", "Hello")
    
    if st.button("Create"):
        st.code(f'{var_name} = "{var_value}"', language="python")

elif selected == "3️⃣ Math":
    st.header("Math Operations")
    
    col1, col2 = st.columns(2)
    with col1:
        st.code("""10 + 5   # 15
10 - 5   # 5
10 * 5   # 50
10 / 5   # 2""", language="python")
    
    with col2:
        st.code("""10 // 3  # 3
10 % 3   # 1
2 ** 3   # 8""", language="python")
    
    st.markdown("### 🧮 Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("Number 1:", value=10.0)
    with col2:
        op = st.selectbox("", ["+", "-", "*", "/"])
    with col3:
        num2 = st.number_input("Number 2:", value=5.0)
    
    if st.button("Calculate"):
        result = eval(f"{num1}{op}{num2}")
        st.success(f"**{num1} {op} {num2} = {result}**")

elif selected == "4️⃣ Text":
    st.header("Working with Text")
    
    st.code("""text = "Python"
print(text.upper())  # PYTHON
print(text.lower())  # python
print(len(text))     # 6""", language="python")
    
    st.markdown("### Try it:")
    text = st.text_input("Enter text:", "Hello Python")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("UPPER"):
            st.code(text.upper())
    with col2:
        if st.button("lower"):
            st.code(text.lower())
    with col3:
        if st.button("Length"):
            st.info(f"{len(text)} characters")

elif selected == "5️⃣ Lists":
    st.header("Lists")
    
    st.code("""fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
fruits.append("orange")
print(len(fruits))    # 4""", language="python")
    
    st.markdown("### List Manager:")
    
    if 'items' not in st.session_state:
        st.session_state.items = []
    
    st.write(f"**List:** {st.session_state.items}")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        new = st.text_input("Add item:")
    with col2:
        st.write("")
        st.write("")
        if st.button("➕ Add"):
            st.session_state.items.append(new)
            st.rerun()
    
    if st.button("🗑️ Clear"):
        st.session_state.items = []
        st.rerun()

elif selected == "6️⃣ If/Else":
    st.header("If/Else")
    
    st.code("""age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")""", language="python")
    
    st.markdown("### Grade Calculator:")
    score = st.slider("Your score:", 0, 100, 75)
    
    if st.button("Get Grade"):
        if score >= 90:
            st.success("🌟 Grade: A - Excellent!")
        elif score >= 80:
            st.success("😊 Grade: B - Great!")
        elif score >= 70:
            st.info("👍 Grade: C - Good!")
        elif score >= 60:
            st.warning("📚 Grade: D - Keep studying!")
        else:
            st.error("💪 Grade: F - Don't give up!")

elif selected == "7️⃣ Loops":
    st.header("Loops")
    
    st.code("""for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4""", language="python")
    
    st.markdown("### Loop Demo:")
    n = st.slider("Count to:", 1, 10, 5)
    
    if st.button("▶ Run Loop"):
        output = []
        for i in range(n):
            output.append(str(i))
        st.code(", ".join(output))

elif selected == "8️⃣ Functions":
    st.header("Functions")
    
    st.code("""def greet(name):
    return f"Hello, {name}!"

message = greet("Hadjar")
print(message)  # Hello, Hadjar!""", language="python")
    
    st.markdown("### Try it:")
    name = st.text_input("Your name:", "Student")
    
    if st.button("Greet Me"):
        st.markdown(f'<div class="code-output">Hello, {name}! 👋</div>', unsafe_allow_html=True)

elif selected == "🎮 Projects":
    st.header("Practice Projects")
    
    project = st.selectbox("Choose:", ["Temperature Converter", "Calculator", "To-Do List"])
    
    if project == "Temperature Converter":
        st.markdown("### 🌡️ Temperature Converter")
        
        temp_type = st.radio("", ["°C → °F", "°F → °C"])
        temp = st.number_input("Temperature:", value=0.0)
        
        if st.button("Convert"):
            if temp_type == "°C → °F":
                result = (temp * 9/5) + 32
                st.success(f"{temp}°C = {result:.1f}°F")
            else:
                result = (temp - 32) * 5/9
                st.success(f"{temp}°F = {result:.1f}°C")
    
    elif project == "Calculator":
        st.markdown("### 🧮 Calculator")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("First:", value=0.0)
        with col2:
            op = st.selectbox("Op:", ["+", "-", "*", "/"])
        with col3:
            b = st.number_input("Second:", value=0.0)
        
        if st.button("="):
            result = eval(f"{a}{op}{b}")
            st.success(f"**{a} {op} {b} = {result}**")
    
    else:  # To-Do List
        st.markdown("### ✅ To-Do List")
        
        if 'todos' not in st.session_state:
            st.session_state.todos = []
        
        task = st.text_input("New task:")
        if st.button("➕ Add") and task:
            st.session_state.todos.append(task)
            st.rerun()
        
        for i, todo in enumerate(st.session_state.todos):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"{i+1}. {todo}")
            with col2:
                if st.button("✓", key=i):
                    st.session_state.todos.pop(i)
                    st.rerun()

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>Keep practicing! 🚀</div>", unsafe_allow_html=True)
