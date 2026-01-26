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
    <code>year = 2026</code>
    
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
    <li><code>%</code> gives remainder after division</li>
    <li><code>**</code> raises to power (e.g., 2**3 = 2×2×2)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write code to calculate and print:
    <ol>
    <li>17 // 5 (floor division)</li>
    <li>17 % 5 (modulus/remainder)</li>
    <li>3 ** 4 (3 to the power of 4)</li>
    <li>100 // 7 and 100 % 7</li>
    </ol>
    Print each result with a descriptive label.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="arith_adv_code")
    
    if st.button("▶️ Run Code", key="run_arith_adv"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "arith_operations":
    st.markdown('<div class="lesson-title">🔢 Combined Arithmetic Operations</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Order of Operations (PEMDAS)</h3>
    Python follows mathematical order:
    <ol>
    <li><strong>P</strong>arentheses: <code>()</code></li>
    <li><strong>E</strong>xponents: <code>**</code></li>
    <li><strong>M</strong>ultiplication & <strong>D</strong>ivision: <code>* / // %</code></li>
    <li><strong>A</strong>ddition & <strong>S</strong>ubtraction: <code>+ -</code></li>
    </ol>
    
    <h4>Examples:</h4>
    <code>result = 2 + 3 * 4     # 14 (not 20!)</code><br>
    <code>result = (2 + 3) * 4   # 20</code><br>
    <code>result = 10 + 5 ** 2   # 35</code><br>
    <code>result = (10 + 5) ** 2 # 225</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Calculate these expressions (think about order!):
    <ol>
    <li><code>5 + 3 * 2</code></li>
    <li><code>(5 + 3) * 2</code></li>
    <li><code>10 / 2 + 3</code></li>
    <li><code>2 ** 3 + 4 * 5</code></li>
    <li><code>(20 + 10) / 2 ** 2</code></li>
    </ol>
    Store in variables and print each with its calculation.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=300, key="arith_ops_code")
    
    if st.button("▶️ Run Code", key="run_arith_ops"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "comp_operators":
    st.markdown('<div class="lesson-title">⚖️ Comparison Operators</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Comparison Operators</h3>
    These operators compare values and return <code>True</code> or <code>False</code>.
    
    <table style="width:100%; border-collapse: collapse;">
    <tr style="background-color: #2E86AB; color: white;">
    <th style="padding: 10px; border: 1px solid #ddd;">Operator</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Meaning</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Example</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Result</th>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>==</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Equal to</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>5 == 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>!=</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Not equal to</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>5 != 3</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>&gt;</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Greater than</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>10 &gt; 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>&lt;</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Less than</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>5 &lt; 10</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>&gt;=</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Greater or equal</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>5 &gt;= 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>&lt;=</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Less or equal</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>3 &lt;= 5</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Test all comparison operators:
    <ol>
    <li>Create <code>x = 10</code> and <code>y = 5</code></li>
    <li>Print result of <code>x == y</code></li>
    <li>Print result of <code>x != y</code></li>
    <li>Print result of <code>x &gt; y</code></li>
    <li>Print result of <code>x &lt; y</code></li>
    <li>Print result of <code>x &gt;= 10</code></li>
    <li>Print result of <code>y &lt;= 5</code></li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=300, key="comp_code")
    
    if st.button("▶️ Run Code", key="run_comp"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "logical_operators":
    st.markdown('<div class="lesson-title">🔗 Logical Operators</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Logical Operators</h3>
    Combine multiple conditions.
    
    <table style="width:100%; border-collapse: collapse;">
    <tr style="background-color: #2E86AB; color: white;">
    <th style="padding: 10px; border: 1px solid #ddd;">Operator</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Description</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Example</th>
    <th style="padding: 10px; border: 1px solid #ddd;">Result</th>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>and</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Both must be True</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>True and True</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>or</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">At least one True</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>True or False</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">True</td>
    </tr>
    <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>not</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">Reverses the value</td>
    <td style="padding: 10px; border: 1px solid #ddd;"><code>not True</code></td>
    <td style="padding: 10px; border: 1px solid #ddd;">False</td>
    </tr>
    </table>
    
    <h4>Examples:</h4>
    <code>age = 20</code><br>
    <code>has_id = True</code><br>
    <code>can_enter = age >= 18 and has_id  # True</code><br>
    <code>is_student = True</code><br>
    <code>is_senior = False</code><br>
    <code>gets_discount = is_student or is_senior  # True</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    <ol>
    <li>Create: <code>age = 25</code>, <code>has_license = True</code></li>
    <li>Check: <code>age >= 18 and has_license</code></li>
    <li>Create: <code>is_weekend = False</code>, <code>is_holiday = True</code></li>
    <li>Check: <code>is_weekend or is_holiday</code></li>
    <li>Create: <code>is_raining = True</code></li>
    <li>Check: <code>not is_raining</code></li>
    </ol>
    Print all results with labels.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=300, key="logical_code")
    
    if st.button("▶️ Run Code", key="run_logical"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "cond_if":
    st.markdown('<div class="lesson-title">❓ if Statement</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The if Statement</h3>
    Executes code only if a condition is <code>True</code>.
    
    <h4>Syntax:</h4>
    <pre><code>if condition:
        # code to execute
        # must be indented (4 spaces or Tab)</code></pre>
    
    <h4>Example:</h4>
    <pre><code>age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")</code></pre>
    
    <p><strong>Important:</strong> Indentation (spaces) is REQUIRED!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write a program that:
    <ol>
    <li>Creates a variable <code>temperature = 30</code></li>
    <li>If temperature is greater than 25, print "It's hot!"</li>
    <li>If temperature is greater than 35, print "It's very hot!"</li>
    </ol>
    Remember to use proper indentation!
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="cond_if_code")
    
    if st.button("▶️ Run Code", key="run_cond_if"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "cond_ifelse":
    st.markdown('<div class="lesson-title">🔀 if/else Statement</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The if/else Statement</h3>
    Executes one block if <code>True</code>, another if <code>False</code>.
    
    <h4>Syntax:</h4>
    <pre><code>if condition:
        # code if True
    else:
        # code if False</code></pre>
    
    <h4>Example:</h4>
    <pre><code>age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write a program that:
    <ol>
    <li>Creates a variable <code>score = 75</code></li>
    <li>If score >= 60, print "You passed!"</li>
    <li>Otherwise, print "You failed. Try again!"</li>
    </ol>
    Test with different scores to see both messages.
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=250, key="cond_ifelse_code")
    
    if st.button("▶️ Run Code", key="run_cond_ifelse"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "cond_ifelif":
    st.markdown('<div class="lesson-title">🔀 if/elif/else Statement</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The if/elif/else Statement</h3>
    Test multiple conditions in order.
    
    <h4>Syntax:</h4>
    <pre><code>if condition1:
        # code if condition1 is True
    elif condition2:
        # code if condition2 is True
    elif condition3:
        # code if condition3 is True
    else:
        # code if all are False</code></pre>
    
    <h4>Example:</h4>
    <pre><code>score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Create a temperature classifier:
    <ol>
    <li>Create variable <code>temp</code></li>
    <li>If temp > 30: print "Hot"</li>
    <li>Elif temp > 20: print "Warm"</li>
    <li>Elif temp > 10: print "Cool"</li>
    <li>Else: print "Cold"</li>
    </ol>
    Test with different temperatures!
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=300, key="cond_ifelif_code")
    
    if st.button("▶️ Run Code", key="run_cond_ifelif"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "loop_for":
    st.markdown('<div class="lesson-title">🔁 for Loop</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The for Loop</h3>
    Repeats code a specific number of times.
    
    <h4>Syntax:</h4>
    <pre><code>for variable in sequence:
        # code to repeat</code></pre>
    
    <h4>Examples:</h4>
    <pre><code>for i in [1, 2, 3, 4, 5]:
    print(i)
    
for name in ["Alice", "Bob", "Charlie"]:
    print("Hello", name)
    
for letter in "Python":
    print(letter)</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    <ol>
    <li>Create a list of 5 fruits</li>
    <li>Use a for loop to print each fruit</li>
    <li>Loop through the word "PYTHON" and print each letter</li>
    <li>Loop through numbers [10, 20, 30, 40, 50] and print each</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=300, key="loop_for_code")
    
    if st.button("▶️ Run Code", key="run_loop_for"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "loop_range":
    st.markdown('<div class="lesson-title">🔁 The range() Function</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Using range() with for Loops</h3>
    <code>range()</code> generates a sequence of numbers.
    
    <h4>Three Ways to Use range():</h4>
    <ol>
    <li><code>range(stop)</code> - from 0 to stop-1</li>
    <li><code>range(start, stop)</code> - from start to stop-1</li>
    <li><code>range(start, stop, step)</code> - with custom step</li>
    </ol>
    
    <h4>Examples:</h4>
    <pre><code>for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
    
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6
    
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
    
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    Write loops to print:
    <ol>
    <li>Numbers from 0 to 10</li>
    <li>Numbers from 5 to 15</li>
    <li>Even numbers from 0 to 20 (use step=2)</li>
    <li>Numbers from 20 down to 1 (backwards)</li>
    <li>Multiples of 5 from 0 to 50</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=350, key="loop_range_code")
    
    if st.button("▶️ Run Code", key="run_loop_range"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "loop_while":
    st.markdown('<div class="lesson-title">🔁 while Loop</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>The while Loop</h3>
    Repeats code while a condition is <code>True</code>.
    
    <h4>Syntax:</h4>
    <pre><code>while condition:
        # code to repeat
        # MUST update condition or loop forever!</code></pre>
    
    <h4>Example:</h4>
    <pre><code>count = 1
while count <= 5:
    print(count)
    count = count + 1  # or count += 1
    
# Output: 1, 2, 3, 4, 5</code></pre>
    
    <p><strong>⚠️ Warning:</strong> Always update the condition variable to avoid infinite loops!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    <ol>
    <li>Print numbers from 1 to 10 using while loop</li>
    <li>Print even numbers from 2 to 20</li>
    <li>Count down from 10 to 1</li>
    <li>Start at 1 and double until >= 100 (1, 2, 4, 8, ...)</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=350, key="loop_while_code")
    
    if st.button("▶️ Run Code", key="run_loop_while"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "loop_nested":
    st.markdown('<div class="lesson-title">🔁 Nested Loops</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>Nested Loops</h3>
    A loop inside another loop.
    
    <h4>Syntax:</h4>
    <pre><code>for i in range(3):
        for j in range(3):
            print(i, j)</code></pre>
    
    <h4>Example - Multiplication Table:</h4>
    <pre><code>for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i*j}")</code></pre>
    
    <h4>Pattern Example:</h4>
    <pre><code>for i in range(5):
        for j in range(i + 1):
            print("*", end="")
        print()  # New line
        
# Output:
# *
# **
# ***
# ****
# *****</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    <ol>
    <li>Print a 5x5 grid of coordinates (i, j)</li>
    <li>Create a multiplication table for 1-5</li>
    <li>Print this pattern:<br>
    <code>1<br>22<br>333<br>4444<br>55555</code></li>
    <li>Print a rectangle of stars (5 rows, 10 columns)</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=400, key="loop_nested_code")
    
    if st.button("▶️ Run Code", key="run_loop_nested"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

elif lesson_id == "loop_control":
    st.markdown('<div class="lesson-title">🔁 Loop Control: break and continue</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
    <h3>break and continue Statements</h3>
    
    <h4>break - Exit the loop completely</h4>
    <pre><code>for i in range(10):
    if i == 5:
        break  # Stop loop at 5
    print(i)
# Output: 0, 1, 2, 3, 4</code></pre>
    
    <h4>continue - Skip current iteration</h4>
    <pre><code>for i in range(6):
    if i == 3:
        continue  # Skip 3
    print(i)
# Output: 0, 1, 2, 4, 5</code></pre>
    
    <h4>Example - Skip even numbers:</h4>
    <pre><code>for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Only odd numbers</code></pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="task-box">
    <h3>📝 Your Task:</h3>
    <ol>
    <li>Loop 1-20, but break at 15</li>
    <li>Loop 1-10, skip (continue) number 5</li>
    <li>Print numbers 1-30, but skip multiples of 3</li>
    <li>Loop and find first number divisible by 7 and 5, then break</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=350, key="loop_control_code")
    
    if st.button("▶️ Run Code", key="run_loop_control"):
        if code.strip():
            output, error = execute_code(code)
            if error:
                st.markdown(f'<div class="error-box">❌ <strong>Error:</strong><br>{error}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="success-box">✅ <strong>Output:</strong></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{output if output else "(No output)"}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p style='font-size: 1.1em;'><strong>Keep practicing! 🚀</strong></p>
    <p>Master Python by writing code yourself!</p>
    <p style='color: #F18F01;'>© 2024 Futuro Skills Academy - Hadjar Naila</p>
</div>
""", unsafe_allow_html=True)

