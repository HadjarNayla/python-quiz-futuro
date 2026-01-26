import streamlit as st
import sys
from io import StringIO

# Page configuration
st.set_page_config(
    page_title="Interactive Python Learning - Futuro Skills Academy",
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
        margin-bottom: 0;
    }
    .instructor {
        text-align: center;
        color: #F18F01;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    .lesson-title {
        color: #2E86AB;
        font-size: 2em;
        font-weight: bold;
        border-bottom: 3px solid #F18F01;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .theory-box {
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 20px 0;
    }
    .task-box {
        background-color: #FFF3E0;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #F18F01;
        margin: 20px 0;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
    }
    .error-box {
        background-color: #FFEBEE;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #F44336;
        margin: 10px 0;
    }
    .output-box {
        background-color: #F5F5F5;
        padding: 15px;
        border-radius: 5px;
        font-family: monospace;
        white-space: pre-wrap;
        margin: 10px 0;
        border: 1px solid #BDBDBD;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🐍 Interactive Python Learning</p>', unsafe_allow_html=True)
st.markdown('<p class="instructor">by Hadjar Naila | Futuro Skills Academy</p>', unsafe_allow_html=True)

# Function to execute code safely
def execute_code(code, input_data=""):
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    sys.stdout = StringIO()
    sys.stdin = StringIO(input_data)
    
    output = ""
    error = ""
    
    try:
        exec(code, {"__builtins__": __builtins__})
        output = sys.stdout.getvalue()
    except Exception as e:
        error = str(e)
    finally:
        sys.stdout = old_stdout
        sys.stdin = old_stdin
    
    return output, error

# Sidebar
st.sidebar.title("📚 Lessons")
lessons = {
    "🏠 Start Here": "intro",
    "📊 Variables - Integers": "var_int",
    "📊 Variables - Floats": "var_float",
    "📊 Variables - Strings": "var_string",
    "📊 Variables - Booleans": "var_bool",
    "📊 Variables - Type Conversion": "var_conversion",
    "🖨️ Output - print()": "output",
    "⌨️ Input - input()": "input",
    "➕ Arithmetic - Basic": "arith_basic",
    "➗ Arithmetic - Advanced": "arith_advanced",
    "🔢 Arithmetic - Operations": "arith_operations",
    "❓ Conditions - if": "cond_if",
    "🔀 Conditions - if/else": "cond_ifelse",
    "🔀 Conditions - if/elif/else": "cond_ifelif",
    "⚖️ Comparison Operators": "comp_operators",
    "🔗 Logical Operators": "logical_operators",
    "🔁 Loops - for": "loop_for",
    "🔁 Loops - while": "loop_while",
    "🔁 Loops - range()": "loop_range",
    "🔁 Loops - Nested": "loop_nested",
    "🔁 Loops - break/continue": "loop_control"
}

selected = st.sidebar.radio("", list(lessons.keys()))
lesson_id = lessons[selected]

st.sidebar.markdown("---")
st.sidebar.info("💡 Write the code yourself and click 'Run Code' to execute!")

# Initialize session state
if 'code_input' not in st.session_state:
    st.session_state.code_input = {}

# Main content
if lesson_id == "intro":
    st.markdown('<div class="lesson-title">🏠 Welcome to Interactive Python!</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="theory-box">
        <h3>👋 Welcome, Student!</h3>
        
        This is a hands-on Python course where <strong>YOU write the code</strong>.
        
        <h4>What you'll learn:</h4>
        <ul>
        <li>✅ All variable types (int, float, str, bool)</li>
        <li>✅ Input and Output operations</li>
        <li>✅ All arithmetic operators (+, -, *, /, //, %, **)</li>
        <li>✅ All comparison operators (==, !=, >, <, >=, <=)</li>
        <li>✅ Logical operators (and, or, not)</li>
        <li>✅ Conditions (if, elif, else)</li>
        <li>✅ Loops (for, while, nested loops)</li>
        <li>✅ Loop control (break, continue)</li>
        </ul>
        
        <h4>How it works:</h4>
        <ol>
        <li>Read the theory</li>
        <li>Complete the task by writing code</li>
        <li>Click "Run Code" to execute</li>
        <li>See your results!</li>
        </ol>
        
        <p style="font-size: 1.2em; color: #F18F01;"><strong>👈 Start with the first lesson!</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=200)
        st.balloons()

elif lesson_id == "var_int":
    st.markdown('<div class="lesson-title">📊 Integer Variables</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>What are Integers?</h3>
    Integers are <strong>whole numbers</strong> (positive, negative, or zero) without decimal points.
    
    <h4>Examples:</h4>
    <code>age = 25</code><br>
    <code>temperature = -10</code><br>
    <code>score = 0</code><br>
    <code>year = 2024</code>
    
    <h4>Characteristics:</h4>
    <ul>
    <li>No decimal point</li>
    <li>Can be positive or negative</li>
    <li>Type: <code>int</code></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to create these integer variables and print them:
    <ol>
    <li><code>my_age</code> with your age</li>
    <li><code>year</code> with current year (2024)</li>
    <li><code>temperature</code> with -5</li>
    </ol>
    Print all three variables.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=200, key="var_int_code", 
                        placeholder="my_age = 20\nyear = 2024\n...")
    
    if st.button("▶️ Run Code", key="run_var_int"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "var_float":
    st.markdown('<div class="lesson-title">📊 Float Variables</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>What are Floats?</h3>
    Floats are numbers <strong>with decimal points</strong>.
    
    <h4>Examples:</h4>
    <code>price = 19.99</code><br>
    <code>temperature = 36.6</code><br>
    <code>pi = 3.14159</code><br>
    <code>height = 1.75</code>
    
    <h4>Characteristics:</h4>
    <ul>
    <li>Must have decimal point</li>
    <li>Can represent fractions</li>
    <li>Type: <code>float</code></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Create and print these float variables:
    <ol>
    <li><code>height</code> with your height in meters (e.g., 1.75)</li>
    <li><code>price</code> with 29.99</li>
    <li><code>pi</code> with 3.14159</li>
    </ol>
    Print all three variables.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=200, key="var_float_code")
    
    if st.button("▶️ Run Code", key="run_var_float"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "var_string":
    st.markdown('<div class="lesson-title">📊 String Variables</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>What are Strings?</h3>
    Strings are <strong>text</strong> enclosed in quotes (single ' or double ").
    
    <h4>Examples:</h4>
    <code>name = "Hadjar"</code><br>
    <code>city = 'Algiers'</code><br>
    <code>message = "Hello, World!"</code><br>
    <code>course = 'Python Programming'</code>
    
    <h4>Characteristics:</h4>
    <ul>
    <li>Must be in quotes</li>
    <li>Can contain letters, numbers, symbols</li>
    <li>Type: <code>str</code></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Create and print these string variables:
    <ol>
    <li><code>name</code> with your name</li>
    <li><code>city</code> with your city</li>
    <li><code>message</code> with "I love Python!"</li>
    </ol>
    Print all three variables.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=200, key="var_string_code")
    
    if st.button("▶️ Run Code", key="run_var_string"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "var_bool":
    st.markdown('<div class="lesson-title">📊 Boolean Variables</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>What are Booleans?</h3>
    Booleans represent <strong>True or False</strong> values.
    
    <h4>Examples:</h4>
    <code>is_student = True</code><br>
    <code>is_raining = False</code><br>
    <code>has_license = True</code><br>
    <code>is_adult = False</code>
    
    <h4>Characteristics:</h4>
    <ul>
    <li>Only two values: <code>True</code> or <code>False</code></li>
    <li>First letter must be CAPITAL</li>
    <li>Type: <code>bool</code></li>
    <li>Used in conditions</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Create and print these boolean variables:
    <ol>
    <li><code>is_student</code> with True</li>
    <li><code>is_raining</code> with False</li>
    <li><code>loves_python</code> with True</li>
    </ol>
    Print all three variables.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=200, key="var_bool_code")
    
    if st.button("▶️ Run Code", key="run_var_bool"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "var_conversion":
    st.markdown('<div class="lesson-title">📊 Type Conversion</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Converting Between Types</h3>
    You can convert variables from one type to another.
    
    <h4>Conversion Functions:</h4>
    <code>int()</code> - Convert to integer<br>
    <code>float()</code> - Convert to float<br>
    <code>str()</code> - Convert to string<br>
    <code>bool()</code> - Convert to boolean
    
    <h4>Examples:</h4>
    <code>x = int(3.7)      # x = 3</code><br>
    <code>y = float(5)      # y = 5.0</code><br>
    <code>z = str(100)      # z = "100"</code><br>
    <code>a = int("42")     # a = 42</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to:
    <ol>
    <li>Convert 3.9 to integer and store in <code>num1</code></li>
    <li>Convert 7 to float and store in <code>num2</code></li>
    <li>Convert 50 to string and store in <code>text</code></li>
    <li>Convert "123" to integer and store in <code>num3</code></li>
    </ol>
    Print all four variables with their types using <code>type()</code>.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="var_conv_code",
                       placeholder="num1 = int(3.9)\nprint(num1, type(num1))\n...")
    
    if st.button("▶️ Run Code", key="run_var_conv"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "output":
    st.markdown('<div class="lesson-title">🖨️ Output with print()</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The print() Function</h3>
    <code>print()</code> displays output on the screen.
    
    <h4>Different Ways to Print:</h4>
    <code>print("Hello")</code> - Print text<br>
    <code>print(25)</code> - Print number<br>
    <code>print(x)</code> - Print variable<br>
    <code>print("Age:", 25)</code> - Print multiple items<br>
    <code>print("Hello", "World")</code> - Separated by space
    
    <h4>Special Characters:</h4>
    <code>\\n</code> - New line<br>
    <code>\\t</code> - Tab
    
    <h4>Example:</h4>
    <code>name = "Hadjar"</code><br>
    <code>age = 25</code><br>
    <code>print("Name:", name)</code><br>
    <code>print("Age:", age)</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to:
    <ol>
    <li>Print "Welcome to Python!"</li>
    <li>Create variables: <code>name</code> and <code>age</code></li>
    <li>Print both on separate lines using labels</li>
    <li>Print them together in one line</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="output_code")
    
    if st.button("▶️ Run Code", key="run_output"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "input":
    st.markdown('<div class="lesson-title">⌨️ Input with input()</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The input() Function</h3>
    <code>input()</code> gets data from the user.
    
    <h4>Syntax:</h4>
    <code>variable = input("Your prompt: ")</code>
    
    <h4>Important:</h4>
    <ul>
    <li><code>input()</code> always returns a STRING</li>
    <li>Must convert to int/float for numbers</li>
    </ul>
    
    <h4>Examples:</h4>
    <code>name = input("Enter name: ")</code><br>
    <code>age = int(input("Enter age: "))</code><br>
    <code>price = float(input("Enter price: "))</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to:
    <ol>
    <li>Ask for user's name (string)</li>
    <li>Ask for user's age (convert to int)</li>
    <li>Ask for user's height (convert to float)</li>
    <li>Print all information</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 For testing, provide input data below (one line per input)")
    input_data = st.text_area("Test Input Data:", height=100, key="input_data",
                              placeholder="Hadjar\n25\n1.75")
    
    code = st.text_area("✏️ Write your code here:", height=250, key="input_code")
    
    if st.button("▶️ Run Code", key="run_input"):
        if code.strip():
            output, error = execute_code(code, input_data)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "arith_basic":
    st.markdown('<div class="lesson-title">➕ Basic Arithmetic Operators</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Basic Arithmetic Operations</h3>
    
    <table style="width:100%; border-collapse: collapse;">
    <tr style="background-color: #2E86AB; color: white;">
    <th style="padding: 10px; border: 1px solid #ddd;">Operator</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Name</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Example</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Result</th>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>+</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Addition</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 + 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">15</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>-</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Subtraction</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 - 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">5</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>*</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Multiplication</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 * 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">50</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>/</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Division</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 / 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">2.0</td>
    </tr>
    </table>
    
    <p><strong>Note:</strong> Division <code>/</code> always returns a float!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to calculate and print:
    <ol>
    <li>50 + 30</li>
    <li>100 - 45</li>
    <li>12 * 8</li>
    <li>20 / 4</li>
    </ol>
    Use variables to store results, then print each with a label.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="arith_basic_code")
    
    if st.button("▶️ Run Code", key="run_arith_basic"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "arith_advanced":
    st.markdown('<div class="lesson-title">➗ Advanced Arithmetic Operators</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Advanced Arithmetic Operations</h3>
    
    <table style="width:100%; border-collapse: collapse;">
    <tr style="background-color: #2E86AB; color: white;">
    <th style="padding: 10px; border: 1px solid #ddd;">Operator</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Name</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Example</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Result</th>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>//</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Floor Division</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 // 3</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">3 (no decimal)</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>%</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Modulus (Remainder)</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 % 3</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">1</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>**</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Exponent (Power)</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>2 ** 3</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">8 (2³)</td>
    </tr>
    </table>
    
    <h4>Explanation:</h4>
    <ul>
    <li><code>//</code> divides and removes decimal part</li>
