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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### What are Integers?")
        st.markdown("Integers are **whole numbers** (positive, negative, or zero) without decimal points.")
        st.markdown("#### Examples:")
        st.code("""age = 25
temperature = -10
score = 0
year = 2024""", language="python")
        st.markdown("""
        #### Characteristics:
        - No decimal point
        - Can be positive or negative
        - Type: `int`
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to create these integer variables and print them:
        1. `my_age` with your age
        2. `year` with current year (2024)
        3. `temperature` with -5
        
        Print all three variables.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    code = st.text_area("✏️ Write your code here:", height=200, key="var_int_code", 
                        placeholder="my_age = 20\nyear = 2024\ntemperature = -5\nprint(my_age)\nprint(year)\nprint(temperature)")
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### What are Floats?")
        st.markdown("Floats are numbers **with decimal points**.")
        st.markdown("#### Examples:")
        st.code("""price = 19.99
temperature = 36.6
pi = 3.14159
height = 1.75""", language="python")
        st.markdown("""
        #### Characteristics:
        - Must have decimal point
        - Can represent fractions
        - Type: `float`
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Create and print these float variables:
        1. `height` with your height in meters (e.g., 1.75)
        2. `price` with 29.99
        3. `pi` with 3.14159
        
        Print all three variables.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### What are Strings?")
        st.markdown("Strings are **text** enclosed in quotes (single ' or double \").")
        st.markdown("#### Examples:")
        st.code("""name = "Hadjar"
city = 'Algiers'
message = "Hello, World!"
course = 'Python Programming'""", language="python")
        st.markdown("""
        #### Characteristics:
        - Must be in quotes
        - Can contain letters, numbers, symbols
        - Type: `str`
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Create and print these string variables:
        1. `name` with your name
        2. `city` with your city
        3. `message` with "I love Python!"
        
        Print all three variables.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### What are Booleans?")
        st.markdown("Booleans represent **True or False** values.")
        st.markdown("#### Examples:")
        st.code("""is_student = True
is_raining = False
has_license = True
is_adult = False""", language="python")
        st.markdown("""
        #### Characteristics:
        - Only two values: `True` or `False`
        - First letter must be CAPITAL
        - Type: `bool`
        - Used in conditions
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Create and print these boolean variables:
        1. `is_student` with True
        2. `is_raining` with False
        3. `loves_python` with True
        
        Print all three variables.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Converting Between Types")
        st.markdown("You can convert variables from one type to another.")
        st.markdown("#### Conversion Functions:")
        st.code("""int()    # Convert to integer
float()  # Convert to float
str()    # Convert to string
bool()   # Convert to boolean""", language="python")
        st.markdown("#### Examples:")
        st.code("""x = int(3.7)      # x = 3
y = float(5)      # y = 5.0
z = str(100)      # z = "100"
a = int("42")     # a = 42""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to:
        1. Convert 3.9 to integer and store in `num1`
        2. Convert 7 to float and store in `num2`
        3. Convert 50 to string and store in `text`
        4. Convert "123" to integer and store in `num3`
        
        Print all four variables with their types using `type()`.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The print() Function")
        st.markdown("`print()` displays output on the screen.")
        st.markdown("#### Different Ways to Print:")
        st.code("""print("Hello")              # Print text
print(25)                   # Print number
print(x)                    # Print variable
print("Age:", 25)           # Print multiple items
print("Hello", "World")     # Separated by space""", language="python")
        st.markdown("#### Special Characters:")
        st.code("""\\n  # New line
\\t  # Tab""", language="python")
        st.markdown("#### Example:")
        st.code("""name = "Hadjar"
age = 25
print("Name:", name)
print("Age:", age)""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to:
        1. Print "Welcome to Python!"
        2. Create variables: `name` and `age`
        3. Print both on separate lines using labels
        4. Print them together in one line
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The input() Function")
        st.markdown("`input()` gets data from the user.")
        st.markdown("#### Syntax:")
        st.code('variable = input("Your prompt: ")', language="python")
        st.markdown("""
        #### Important:
        - `input()` always returns a STRING
        - Must convert to int/float for numbers
        """)
        st.markdown("#### Examples:")
        st.code("""name = input("Enter name: ")
age = int(input("Enter age: "))
price = float(input("Enter price: "))""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to:
        1. Ask for user's name (string)
        2. Ask for user's age (convert to int)
        3. Ask for user's height (convert to float)
        4. Print all information
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Basic Arithmetic Operations")
        
        data = {
            "Operator": ["`+`", "`-`", "`*`", "`/`"],
            "Name": ["Addition", "Subtraction", "Multiplication", "Division"],
            "Example": ["`10 + 5`", "`10 - 5`", "`10 * 5`", "`10 / 5`"],
            "Result": ["15", "5", "50", "2.0"]
        }
        st.table(data)
        
        st.markdown("**Note:** Division `/` always returns a float!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to calculate and print:
        1. 50 + 30
        2. 100 - 45
        3. 12 * 8
        4. 20 / 4
        
        Use variables to store results, then print each with a label.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Advanced Arithmetic Operations")
        
        data = {
            "Operator": ["`//`", "`%`", "`**`"],
            "Name": ["Floor Division", "Modulus (Remainder)", "Exponent (Power)"],
            "Example": ["`10 // 3`", "`10 % 3`", "`2 ** 3`"],
            "Result": ["3 (no decimal)", "1", "8 (2³)"]
        }
        st.table(data)
        
        st.markdown("""
        #### Explanation:
        - `//` divides and removes decimal part
        - `%` gives remainder after division
        - `**` raises to power (e.g., 2**3 = 2×2×2)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write code to calculate and print:
        1. 17 // 5 (floor division)
        2. 17 % 5 (modulus/remainder)
        3. 3 ** 4 (3 to the power of 4)
        4. 100 // 7 and 100 % 7
        
        Print each result with a descriptive label.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Order of Operations (PEMDAS)")
        st.markdown("""
        Python follows mathematical order:
        1. **P**arentheses: `()`
        2. **E**xponents: `**`
        3. **M**ultiplication & **D**ivision: `* / // %`
        4. **A**ddition & **S**ubtraction: `+ -`
        """)
        st.markdown("#### Examples:")
        st.code("""result = 2 + 3 * 4     # 14 (not 20!)
result = (2 + 3) * 4   # 20
result = 10 + 5 ** 2   # 35
result = (10 + 5) ** 2 # 225""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Calculate these expressions (think about order!):
        1. `5 + 3 * 2`
        2. `(5 + 3) * 2`
        3. `10 / 2 + 3`
        4. `2 ** 3 + 4 * 5`
        5. `(20 + 10) / 2 ** 2`
        
        Store in variables and print each with its calculation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Comparison Operators")
        st.markdown("These operators compare values and return `True` or `False`.")
        
        data = {
            "Operator": ["`==`", "`!=`", "`>`", "`<`", "`>=`", "`<=`"],
            "Meaning": ["Equal to", "Not equal to", "Greater than", "Less than", "Greater or equal", "Less or equal"],
            "Example": ["`5 == 5`", "`5 != 3`", "`10 > 5`", "`5 < 10`", "`5 >= 5`", "`3 <= 5`"],
            "Result": ["True", "True", "True", "True", "True", "True"]
        }
        st.table(data)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Test all comparison operators:
        1. Create `x = 10` and `y = 5`
        2. Print result of `x == y`
        3. Print result of `x != y`
        4. Print result of `x > y`
        5. Print result of `x < y`
        6. Print result of `x >= 10`
        7. Print result of `y <= 5`
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Logical Operators")
        st.markdown("Combine multiple conditions.")
        
        data = {
            "Operator": ["`and`", "`or`", "`not`"],
            "Description": ["Both must be True", "At least one True", "Reverses the value"],
            "Example": ["`True and True`", "`True or False`", "`not True`"],
            "Result": ["True", "True", "False"]
        }
        st.table(data)
        
        st.markdown("#### Examples:")
        st.code("""age = 20
has_id = True
can_enter = age >= 18 and has_id  # True

is_student = True
is_senior = False
gets_discount = is_student or is_senior  # True""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        1. Create: `age = 25`, `has_license = True`
        2. Check: `age >= 18 and has_license`
        3. Create: `is_weekend = False`, `is_holiday = True`
        4. Check: `is_weekend or is_holiday`
        5. Create: `is_raining = True`
        6. Check: `not is_raining`
        
        Print all results with labels.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The if Statement")
        st.markdown("Executes code only if a condition is `True`.")
        st.markdown("#### Syntax:")
        st.code("""if condition:
    # code to execute
    # must be indented (4 spaces or Tab)""", language="python")
        st.markdown("#### Example:")
        st.code("""age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")""", language="python")
        st.markdown("**Important:** Indentation (spaces) is REQUIRED!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write a program that:
        1. Creates a variable `temperature = 30`
        2. If temperature is greater than 25, print "It's hot!"
        3. If temperature is greater than 35, print "It's very hot!"
        
        Remember to use proper indentation!
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The if/else Statement")
        st.markdown("Executes one block if `True`, another if `False`.")
        st.markdown("#### Syntax:")
        st.code("""if condition:
    # code if True
else:
    # code if False""", language="python")
        st.markdown("#### Example:")
        st.code("""age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write a program that:
        1. Creates a variable `score = 75`
        2. If score >= 60, print "You passed!"
        3. Otherwise, print "You failed. Try again!"
        
        Test with different scores to see both messages.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The if/elif/else Statement")
        st.markdown("Test multiple conditions in order.")
        st.markdown("#### Syntax:")
        st.code("""if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
elif condition3:
    # code if condition3 is True
else:
    # code if all are False""", language="python")
        st.markdown("#### Example:")
        st.code("""score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Create a temperature classifier:
        1. Create variable `temp`
        2. If temp > 30: print "Hot"
        3. Elif temp > 20: print "Warm"
        4. Elif temp > 10: print "Cool"
        5. Else: print "Cold"
        
        Test with different temperatures!
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The for Loop")
        st.markdown("Repeats code a specific number of times.")
        st.markdown("#### Syntax:")
        st.code("""for variable in sequence:
    # code to repeat""", language="python")
        st.markdown("#### Examples:")
        st.code("""for i in [1, 2, 3, 4, 5]:
    print(i)

for name in ["Alice", "Bob", "Charlie"]:
    print("Hello", name)

for letter in "Python":
    print(letter)""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        1. Create a list of 5 fruits
        2. Use a for loop to print each fruit
        3. Loop through the word "PYTHON" and print each letter
        4. Loop through numbers [10, 20, 30, 40, 50] and print each
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Using range() with for Loops")
        st.markdown("`range()` generates a sequence of numbers.")
        st.markdown("""
        #### Three Ways to Use range():
        1. `range(stop)` - from 0 to stop-1
        2. `range(start, stop)` - from start to stop-1
        3. `range(start, stop, step)` - with custom step
        """)
        st.markdown("#### Examples:")
        st.code("""for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        Write loops to print:
        1. Numbers from 0 to 10
        2. Numbers from 5 to 15
        3. Even numbers from 0 to 20 (use step=2)
        4. Numbers from 20 down to 1 (backwards)
        5. Multiples of 5 from 0 to 50
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### The while Loop")
        st.markdown("Repeats code while a condition is `True`.")
        st.markdown("#### Syntax:")
        st.code("""while condition:
    # code to repeat
    # MUST update condition or loop forever!""", language="python")
        st.markdown("#### Example:")
        st.code("""count = 1
while count <= 5:
    print(count)
    count = count + 1  # or count += 1

# Output: 1, 2, 3, 4, 5""", language="python")
        st.markdown("**⚠️ Warning:** Always update the condition variable to avoid infinite loops!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        1. Print numbers from 1 to 10 using while loop
        2. Print even numbers from 2 to 20
        3. Count down from 10 to 1
        4. Start at 1 and double until >= 100 (1, 2, 4, 8, ...)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### Nested Loops")
        st.markdown("A loop inside another loop.")
        st.markdown("#### Syntax:")
        st.code("""for i in range(3):
    for j in range(3):
        print(i, j)""", language="python")
        st.markdown("#### Example - Multiplication Table:")
        st.code("""for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")""", language="python")
        st.markdown("#### Pattern Example:")
        st.code("""for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line

# Output:
# *
# **
# ***
# ****
# *****""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        1. Print a 5x5 grid of coordinates (i, j)
        2. Create a multiplication table for 1-5
        3. Print this pattern:
           ```
           1
           22
           333
           4444
           55555
           ```
        4. Print a rectangle of stars (5 rows, 10 columns)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    with st.container():
        st.markdown('<div class="theory-box">', unsafe_allow_html=True)
        st.markdown("### break and continue Statements")
        st.markdown("#### break - Exit the loop completely")
        st.code("""for i in range(10):
    if i == 5:
        break  # Stop loop at 5
    print(i)
# Output: 0, 1, 2, 3, 4""", language="python")
        st.markdown("#### continue - Skip current iteration")
        st.code("""for i in range(6):
    if i == 3:
        continue  # Skip 3
    print(i)
# Output: 0, 1, 2, 4, 5""", language="python")
        st.markdown("#### Example - Skip even numbers:")
        st.code("""for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Only odd numbers""", language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="task-box">', unsafe_allow_html=True)
        st.markdown("### 📝 Your Task:")
        st.markdown("""
        1. Loop 1-20, but break at 15
        2. Loop 1-10, skip (continue) number 5
        3. Print numbers 1-30, but skip multiples of 3
        4. Loop and find first number divisible by 7 and 5, then break
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
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
