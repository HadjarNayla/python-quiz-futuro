import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Page Configuration
st.set_page_config(
    page_title="⚽ Football Analytics - Pandas Tutorial",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #10b981, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card {
        background-color: #f0f9ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3b82f6;
    }
    .success-box {
        padding: 1rem;
        background-color: #d1fae5;
        border-radius: 0.5rem;
        border-left: 4px solid #10b981;
    }
    .code-box {
        background-color: #1e293b;
        color: #10b981;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">⚽ Football Players Analytics Tutorial</p>', unsafe_allow_html=True)
st.markdown("### 🐼 Interactive Pandas Learning with Your Dataset (2015-2024)")

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None

# Sidebar
with st.sidebar:
    st.header("📚 Tutorial Navigation")
    
    tutorial_section = st.radio(
        "Choose Section:",
        [
            "🏠 Home",
            "📤 Upload Data",
            "🔍 Explore Data",
            "📊 Statistical Analysis",
            "🎯 Filter & Sort",
            "📈 Grouping & Aggregation",
            "🆕 Create New Columns",
            "🧹 Data Cleaning",
            "📉 Visualizations",
            "💾 Export Results",
            "🎓 Complete Example"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("Upload your CSV file to start analyzing!")
    
    # Sample Data Generator
    if st.button("🎲 Generate Sample Data"):
        sample_data = {
            'Player_Name': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr', 
                           'Kylian Mbappé', 'Mohamed Salah', 'Kevin De Bruyne',
                           'Robert Lewandowski', 'Erling Haaland', 'Harry Kane',
                           'Luka Modrić', 'Vinicius Jr', 'Jude Bellingham'],
            'Club': ['Inter Miami', 'Al Nassr', 'Al Hilal', 'Real Madrid', 
                    'Liverpool', 'Manchester City', 'Barcelona', 'Manchester City',
                    'Bayern Munich', 'Real Madrid', 'Real Madrid', 'Real Madrid'],
            'Goals': [32, 44, 23, 52, 30, 10, 42, 56, 44, 5, 28, 23],
            'Assists': [35, 12, 28, 16, 16, 25, 15, 11, 12, 15, 21, 13],
            'Rating': [8.9, 8.5, 8.3, 9.2, 8.7, 8.8, 8.6, 9.0, 8.5, 8.4, 8.7, 8.9],
            'Tenure_Years': [1, 2, 1, 5, 7, 9, 3, 3, 4, 12, 6, 1],
            'Matches_Played': [38, 42, 35, 45, 41, 38, 40, 43, 42, 40, 44, 42]
        }
        st.session_state.df = pd.DataFrame(sample_data)
        st.success("✅ Sample data generated!")
        st.rerun()

# Main Content
if tutorial_section == "🏠 Home":
    st.header("Welcome to Interactive Pandas Tutorial! 🎉")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📖 What You'll Learn:
        - 📤 Loading and exploring datasets
        - 🔍 Data selection and filtering
        - 📊 Statistical analysis techniques
        - 📈 Grouping and aggregation
        - 🆕 Creating calculated columns
        - 🧹 Data cleaning methods
        - 📉 Data visualization
        - 💾 Exporting results
        
        ### 🎯 Dataset Features:
        - ⚽ Player Name
        - 🏢 Club
        - 🎯 Goals & Assists
        - 🌟 Rating
        - ⏳ Tenure in Club
        - 🏆 Matches Played
        """)
    
    with col2:
        st.markdown("""
        ### 🚀 Getting Started:
        
        **Step 1:** Upload your CSV file or generate sample data
        
        **Step 2:** Navigate through sections using the sidebar
        
        **Step 3:** Interact with filters and options
        
        **Step 4:** See live results and code examples
        
        **Step 5:** Download your analysis results
        
        ### 📚 Prerequisites:
        ```python
        pip install streamlit pandas numpy matplotlib seaborn
        ```
        
        ### ▶️ Run this app:
        ```bash
        streamlit run app.py
        ```
        """)
    
    st.info("👈 Start by uploading your dataset in the sidebar or generate sample data!")

elif tutorial_section == "📤 Upload Data":
    st.header("📤 Upload Your Dataset")
    
    st.markdown("""
    ### Upload your Football Players CSV file
    Your CSV should contain columns like: Player_Name, Club, Goals, Assists, Rating, Tenure_Years, Matches_Played
    """)
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            st.session_state.df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully!")
            
            st.markdown("### Preview of uploaded data:")
            st.dataframe(st.session_state.df.head(10), use_container_width=True)
            
            st.markdown("### Dataset Info:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", len(st.session_state.df))
            with col2:
                st.metric("Total Columns", len(st.session_state.df.columns))
            with col3:
                st.metric("Memory Usage", f"{st.session_state.df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            
            # Show code
            with st.expander("📝 Show Python Code"):
                st.code("""
import pandas as pd

# Load data from CSV
df = pd.read_csv('football_players_2015_2024.csv')

# Preview data
print(df.head())

# Dataset shape
print(f"Shape: {df.shape}")
                """, language="python")
                
        except Exception as e:
            st.error(f"❌ Error loading file: {e}")
    else:
        st.info("Please upload a CSV file to continue")

elif tutorial_section == "🔍 Explore Data":
    st.header("🔍 Explore Your Dataset")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Preview", "ℹ️ Info", "📈 Statistics", "🔎 Details"])
        
        with tab1:
            st.subheader("Dataset Preview")
            
            col1, col2 = st.columns(2)
            with col1:
                n_rows = st.slider("Number of rows to display", 5, 50, 10)
            with col2:
                view_type = st.radio("View", ["Head", "Tail", "Sample"], horizontal=True)
            
            if view_type == "Head":
                st.dataframe(df.head(n_rows), use_container_width=True)
            elif view_type == "Tail":
                st.dataframe(df.tail(n_rows), use_container_width=True)
            else:
                st.dataframe(df.sample(min(n_rows, len(df))), use_container_width=True)
            
            with st.expander("📝 Show Code"):
                st.code(f"""
# View first {n_rows} rows
df.head({n_rows})

# View last {n_rows} rows
df.tail({n_rows})

# Random sample
df.sample({n_rows})
                """, language="python")
        
        with tab2:
            st.subheader("Dataset Information")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Rows", len(df))
            with col2:
                st.metric("Columns", len(df.columns))
            with col3:
                st.metric("Duplicates", df.duplicated().sum())
            with col4:
                st.metric("Missing Values", df.isnull().sum().sum())
            
            st.markdown("### Column Information:")
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.values,
                'Non-Null Count': df.count().values,
                'Null Count': df.isnull().sum().values
            })
            st.dataframe(col_info, use_container_width=True)
            
            with st.expander("📝 Show Code"):
                st.code("""
# Dataset info
df.info()

# Check missing values
df.isnull().sum()

# Check duplicates
df.duplicated().sum()
                """, language="python")
        
        with tab3:
            st.subheader("Statistical Summary")
            
            # Select numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if numeric_cols:
                st.dataframe(df[numeric_cols].describe(), use_container_width=True)
                
                st.markdown("### Correlation Matrix")
                if len(numeric_cols) > 1:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0, ax=ax)
                    st.pyplot(fig)
                
                with st.expander("📝 Show Code"):
                    st.code("""
# Statistical summary
df.describe()

# Correlation matrix
import seaborn as sns
import matplotlib.pyplot as plt

correlation = df[numeric_columns].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()
                    """, language="python")
            else:
                st.warning("No numeric columns found in dataset")
        
        with tab4:
            st.subheader("Detailed Column Analysis")
            
            selected_col = st.selectbox("Select Column to Analyze", df.columns)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### {selected_col} - Statistics")
                if df[selected_col].dtype in ['int64', 'float64']:
                    st.write(f"**Mean:** {df[selected_col].mean():.2f}")
                    st.write(f"**Median:** {df[selected_col].median():.2f}")
                    st.write(f"**Std Dev:** {df[selected_col].std():.2f}")
                    st.write(f"**Min:** {df[selected_col].min()}")
                    st.write(f"**Max:** {df[selected_col].max()}")
                else:
                    st.write(f"**Unique Values:** {df[selected_col].nunique()}")
                    st.write(f"**Most Common:** {df[selected_col].mode()[0]}")
            
            with col2:
                st.markdown(f"### {selected_col} - Distribution")
                if df[selected_col].dtype in ['int64', 'float64']:
                    fig, ax = plt.subplots()
                    df[selected_col].hist(bins=20, ax=ax, edgecolor='black')
                    ax.set_xlabel(selected_col)
                    ax.set_ylabel('Frequency')
                    st.pyplot(fig)
                else:
                    st.write(df[selected_col].value_counts())
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "📊 Statistical Analysis":
    st.header("📊 Statistical Analysis")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if numeric_cols:
            st.subheader("Basic Statistics")
            
            selected_columns = st.multiselect(
                "Select columns to analyze",
                numeric_cols,
                default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
            )
            
            if selected_columns:
                col1, col2, col3 = st.columns(3)
                
                for idx, col in enumerate(selected_columns):
                    with [col1, col2, col3][idx % 3]:
                        st.markdown(f"### {col}")
                        st.metric("Mean", f"{df[col].mean():.2f}")
                        st.metric("Median", f"{df[col].median():.2f}")
                        st.metric("Std Dev", f"{df[col].std():.2f}")
                        st.metric("Max", f"{df[col].max():.2f}")
                        st.metric("Min", f"{df[col].min():.2f}")
                
                st.markdown("---")
                st.subheader("Value Counts for Categorical Columns")
                
                cat_cols = df.select_dtypes(include=['object']).columns.tolist()
                if cat_cols:
                    selected_cat = st.selectbox("Select categorical column", cat_cols)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.dataframe(df[selected_cat].value_counts(), use_container_width=True)
                    with col2:
                        fig, ax = plt.subplots()
                        df[selected_cat].value_counts().plot(kind='bar', ax=ax)
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
                
                with st.expander("📝 Show Code"):
                    st.code("""
# Basic statistics
print(f"Mean: {df['Goals'].mean():.2f}")
print(f"Median: {df['Goals'].median():.2f}")
print(f"Std: {df['Goals'].std():.2f}")
print(f"Max: {df['Goals'].max()}")
print(f"Min: {df['Goals'].min()}")

# Value counts
df['Club'].value_counts()

# Correlation
df[['Goals', 'Assists', 'Rating']].corr()
                    """, language="python")
        else:
            st.warning("No numeric columns found!")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "🎯 Filter & Sort":
    st.header("🎯 Filter and Sort Data")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        tab1, tab2 = st.tabs(["🔍 Filtering", "📊 Sorting"])
        
        with tab1:
            st.subheader("Filter Your Data")
            
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if numeric_cols:
                filter_col = st.selectbox("Select column to filter", numeric_cols)
                
                col1, col2 = st.columns(2)
                with col1:
                    filter_op = st.selectbox("Operation", [">", "<", ">=", "<=", "=="])
                with col2:
                    filter_value = st.number_input("Value", value=float(df[filter_col].mean()))
                
                # Apply filter
                if filter_op == ">":
                    filtered_df = df[df[filter_col] > filter_value]
                elif filter_op == "<":
                    filtered_df = df[df[filter_col] < filter_value]
                elif filter_op == ">=":
                    filtered_df = df[df[filter_col] >= filter_value]
                elif filter_op == "<=":
                    filtered_df = df[df[filter_col] <= filter_value]
                else:
                    filtered_df = df[df[filter_col] == filter_value]
                
                st.success(f"✅ Found {len(filtered_df)} rows matching criteria")
                st.dataframe(filtered_df, use_container_width=True)
                
                with st.expander("📝 Show Code"):
                    st.code(f"""
# Filter data
filtered_df = df[df['{filter_col}'] {filter_op} {filter_value}]
print(f"Found {{len(filtered_df)}} rows")
print(filtered_df)
                    """, language="python")
        
        with tab2:
            st.subheader("Sort Your Data")
            
            sort_col = st.selectbox("Select column to sort by", df.columns)
            sort_order = st.radio("Sort order", ["Ascending", "Descending"], horizontal=True)
            
            sorted_df = df.sort_values(sort_col, ascending=(sort_order == "Ascending"))
            
            st.dataframe(sorted_df, use_container_width=True)
            
            with st.expander("📝 Show Code"):
                st.code(f"""
# Sort data
sorted_df = df.sort_values('{sort_col}', ascending={sort_order == "Ascending"})
print(sorted_df)

# Sort by multiple columns
df.sort_values(['Rating', 'Goals'], ascending=[False, False])
                """, language="python")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "📈 Grouping & Aggregation":
    st.header("📈 Grouping and Aggregation")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if cat_cols and numeric_cols:
            st.subheader("Group By Analysis")
            
            group_col = st.selectbox("Group by column", cat_cols)
            agg_cols = st.multiselect("Columns to aggregate", numeric_cols, default=numeric_cols[:2])
            agg_func = st.selectbox("Aggregation function", ["mean", "sum", "count", "min", "max", "median"])
            
            if agg_cols:
                grouped = df.groupby(group_col)[agg_cols].agg(agg_func).round(2)
                
                st.dataframe(grouped, use_container_width=True)
                
                # Visualization
                st.subheader("Visualization")
                chart_col = st.selectbox("Select column to visualize", agg_cols)
                
                fig, ax = plt.subplots(figsize=(10, 6))
                grouped[chart_col].plot(kind='bar', ax=ax)
                plt.xlabel(group_col)
                plt.ylabel(f"{agg_func.title()} of {chart_col}")
                plt.title(f"{agg_func.title()} {chart_col} by {group_col}")
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig)
                
                with st.expander("📝 Show Code"):
                    st.code(f"""
# Group by and aggregate
grouped = df.groupby('{group_col}')[{agg_cols}].{agg_func}()
print(grouped)

# Multiple aggregations
df.groupby('{group_col}').agg({{
    '{agg_cols[0]}': ['sum', 'mean', 'max'],
    '{agg_cols[1] if len(agg_cols) > 1 else agg_cols[0]}': ['mean', 'count']
}})
                    """, language="python")
        else:
            st.warning("Need both categorical and numeric columns for grouping!")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "🆕 Create New Columns":
    st.header("🆕 Create New Calculated Columns")
    
    if st.session_state.df is not None:
        df = st.session_state.df.copy()
        
        st.subheader("Add Custom Columns")
        
        col_name = st.text_input("New column name", "Goal_Contribution")
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                first_col = st.selectbox("First column", numeric_cols, index=0)
            with col2:
                operation = st.selectbox("Operation", ["+", "-", "*", "/"])
            
            second_col = st.selectbox("Second column", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
            
            if st.button("Create Column"):
                if operation == "+":
                    df[col_name] = df[first_col] + df[second_col]
                elif operation == "-":
                    df[col_name] = df[first_col] - df[second_col]
                elif operation == "*":
                    df[col_name] = df[first_col] * df[second_col]
                else:
                    df[col_name] = df[first_col] / df[second_col]
                
                st.session_state.df = df
                st.success(f"✅ Created column: {col_name}")
                st.dataframe(df[[first_col, second_col, col_name]].head(10), use_container_width=True)
                
                with st.expander("📝 Show Code"):
                    st.code(f"""
# Create new column
df['{col_name}'] = df['{first_col}'] {operation} df['{second_col}']

# Example: Goals per match
df['Goals_Per_Match'] = df['Goals'] / df['Matches_Played']

# Example: Total contribution
df['Goal_Contribution'] = df['Goals'] + df['Assists']
                    """, language="python")
        
        st.markdown("---")
        st.subheader("Common Calculations")
        
        if st.button("🎯 Calculate Goals per Match"):
            if 'Goals' in df.columns and 'Matches_Played' in df.columns:
                df['Goals_Per_Match'] = (df['Goals'] / df['Matches_Played']).round(2)
                st.session_state.df = df
                st.success("✅ Added Goals_Per_Match column!")
                st.dataframe(df[['Player_Name', 'Goals', 'Matches_Played', 'Goals_Per_Match']].head(), use_container_width=True)
        
        if st.button("🤝 Calculate Goal Contribution"):
            if 'Goals' in df.columns and 'Assists' in df.columns:
                df['Goal_Contribution'] = df['Goals'] + df['Assists']
                st.session_state.df = df
                st.success("✅ Added Goal_Contribution column!")
                st.dataframe(df[['Player_Name', 'Goals', 'Assists', 'Goal_Contribution']].head(), use_container_width=True)
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "🧹 Data Cleaning":
    st.header("🧹 Data Cleaning")
    
    if st.session_state.df is not None:
        df = st.session_state.df.copy()
        
        tab1, tab2, tab3 = st.tabs(["🔍 Check Issues", "🗑️ Remove Duplicates", "❓ Handle Missing"])
        
        with tab1:
            st.subheader("Data Quality Check")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", len(df))
                st.metric("Duplicates", df.duplicated().sum())
            with col2:
                st.metric("Missing Values", df.isnull().sum().sum())
                st.metric("Complete Rows", len(df.dropna()))
            with col3:
                st.metric("Columns", len(df.columns))
                st.metric("Memory (KB)", f"{df.memory_usage(deep=True).sum() / 1024:.2f}")
            
            st.markdown("### Missing Values by Column")
            missing_df = pd.DataFrame({
                'Column': df.columns,
                'Missing': df.isnull().sum().values,
                'Percentage': (df.isnull().sum().values / len(df) * 100).round(2)
            })
            st.dataframe(missing_df, use_container_width=True)
        
        with tab2:
            st.subheader("Remove Duplicate Rows")
            
            dup_count = df.duplicated().sum()
            st.info(f"Found {dup_count} duplicate rows")
            
            if dup_count > 0:
                st.dataframe(df[df.duplicated(keep=False)], use_container_width=True)
                
                if st.button("🗑️ Remove Duplicates"):
                    df = df.drop_duplicates()
                    st.session_state.df = df
                    st.success(f"✅ Removed {dup_count} duplicates!")
                    st.rerun()
            else:
                st.success("✅ No duplicates found!")
            
            with st.expander("📝 Show Code"):
                st.code("""
# Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# Remove duplicates
df_clean = df.drop_duplicates()

# Reset index
df_clean = df_clean.reset_index(drop=True)
                """, language="python")
        
        with tab3:
            st.subheader("Handle Missing Values")
            
            missing_cols = df.columns[df.isnull().any()].tolist()
            
            if missing_cols:
                selected_col = st.selectbox("Select column with missing values", missing_cols)
                
                method = st.radio(
                    "Handling method",
                    ["Fill with Mean", "Fill with Median", "Fill with Mode", "Fill with Custom Value", "Drop Rows"]
                )
                
                if method == "Fill with Custom Value":
                    custom_value = st.text_input("Custom value", "0")
                
                if st.button("Apply"):
                    if method == "Fill with Mean":
                        df[selected_col].fillna(df[selected_col].mean(), inplace=True)
                    elif method == "Fill with Median":
                        df[selected_col].fillna(df[selected_col].median(), inplace=True)
                    elif method == "Fill with Mode":
                        df[selected_col].fillna(df[selected_col].mode()[0], inplace=True)
                    elif method == "Fill with Custom Value":
                        df[selected_col].fillna(custom_value, inplace=True)
                    else:
                        df = df.dropna(subset=[selected_col])
                    
                    st.session_state.df = df
                    st.success("✅ Missing values handled!")
                    st.rerun()
            else:
                st.success("✅ No missing values found!")
            
            with st.expander("📝 Show Code"):
                st.code("""
# Fill with mean
df['Goals'].fillna(df['Goals'].mean(), inplace=True)

# Fill with median
df['Rating'].fillna(df['Rating'].median(), inplace=True)

# Drop rows with missing values
df_clean = df.dropna()

# Drop specific columns with missing values
df_clean = df.dropna(subset=['Goals', 'Assists'])
                """, language="python")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "📉 Visualizations":
    st.header("📉 Data Visualizations")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        viz_type = st.selectbox(
            "Select visualization type",
            ["Bar Chart", "Line Chart", "Scatter Plot", "Box Plot", "Histogram", "Pie Chart"]
        )
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        if viz_type == "Bar Chart" and cat_cols and numeric_cols:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("X-axis (Category)", cat_cols)
            with col2:
                y_col = st.selectbox("Y-axis (Numeric)", numeric_cols)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            df.groupby(x_col)[y_col].mean().plot(kind='bar', ax=ax)
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f'{y_col} by {x_col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
        
        elif viz_type == "Line Chart" and numeric_cols:
            y_col = st.selectbox("Select Y-axis", numeric_cols)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            df[y_col].plot(kind='line', ax=ax, marker='o')
            plt.ylabel(y_col)
            plt.title(f'{y_col} Trend')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
        
        elif viz_type == "Scatter Plot" and len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("X-axis", numeric_cols, index=0)
            with col2:
                y_col = st.selectbox("Y-axis", numeric_cols, index=1)
            
            color_by = st.selectbox("Color by (optional)", ["None"] + cat_cols)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            if color_by != "None":
                for category in df[color_by].unique():
                    mask = df[color_by] == category
                    ax.scatter(df[mask][x_col], df[mask][y_col], label=category, alpha=0.6, s=100)
                plt.legend()
            else:
                ax.scatter(df[x_col], df[y_col], alpha=0.6, s=100)
            
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f'{y_col} vs {x_col}')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
        
        elif viz_type == "Box Plot" and numeric_cols:
            y_col = st.selectbox("Select column", numeric_cols)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            df.boxplot(column=y_col, ax=ax)
            plt.ylabel(y_col)
            plt.title(f'{y_col} Distribution')
            plt.tight_layout()
            st.pyplot(fig)
        
        elif viz_type == "Histogram" and numeric_cols:
            col = st.selectbox("Select column", numeric_cols)
            bins = st.slider("Number of bins", 5, 50, 20)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            df[col].hist(bins=bins, ax=ax, edgecolor='black', alpha=0.7)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.title(f'{col} Distribution')
            plt.tight_layout()
            st.pyplot(fig)
        
        elif viz_type == "Pie Chart" and cat_cols:
            col = st.selectbox("Select column", cat_cols)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            df[col].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
            plt.ylabel('')
            plt.title(f'{col} Distribution')
            plt.tight_layout()
            st.pyplot(fig)
        
        with st.expander("📝 Show Code"):
            st.code("""
import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart
df.groupby('Club')['Goals'].mean().plot(kind='bar')
plt.title('Average Goals by Club')
plt.show()

# Scatter plot
plt.scatter(df['Goals'], df['Assists'])
plt.xlabel('Goals')
plt.ylabel('Assists')
plt.show()

# Histogram
df['Rating'].hist(bins=20)
plt.xlabel('Rating')
plt.show()

# Box plot
df.boxplot(column='Goals')
plt.show()
            """, language="python")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "💾 Export Results":
    st.header("💾 Export Your Analysis Results")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        st.subheader("Download Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📄 Export to CSV")
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name='football_analysis_results.csv',
                mime='text/csv',
            )
        
        with col2:
            st.markdown("### 📊 Export to Excel")
            
            # Create Excel file
            from io import BytesIO
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Players', index=False)
            excel_data = output.getvalue()
            
            st.download_button(
                label="⬇️ Download Excel",
                data=excel_data,
                file_name='football_analysis_results.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
        
        st.markdown("---")
        st.subheader("Export Filtered Data")
        
        # Select columns to export
        selected_cols = st.multiselect(
            "Select columns to export",
            df.columns.tolist(),
            default=df.columns.tolist()
        )
        
        if selected_cols:
            export_df = df[selected_cols]
            
            st.dataframe(export_df.head(), use_container_width=True)
            
            csv_filtered = export_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Filtered CSV",
                data=csv_filtered,
                file_name='filtered_data.csv',
                mime='text/csv',
            )
        
        with st.expander("📝 Show Code"):
            st.code("""
# Save to CSV
df.to_csv('football_analysis_results.csv', index=False)

# Save to Excel
df.to_excel('football_analysis_results.xlsx', index=False, sheet_name='Players')

# Save specific columns
df[['Player_Name', 'Goals', 'Assists']].to_csv('goals_assists.csv', index=False)

# Save filtered data
high_scorers = df[df['Goals'] > 40]
high_scorers.to_csv('high_scorers.csv', index=False)
            """, language="python")
    else:
        st.warning("⚠️ Please upload a dataset first!")

elif tutorial_section == "🎓 Complete Example":
    st.header("🎓 Complete Analysis Example")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        
        st.markdown("### 🏆 Comprehensive Football Analytics Report")
        
        # Overview metrics
        st.subheader("📊 Dataset Overview")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Players", len(df))
        with col2:
            if 'Club' in df.columns:
                st.metric("Total Clubs", df['Club'].nunique())
            else:
                st.metric("Total Clubs", "N/A")
        with col3:
            if 'Goals' in df.columns:
                st.metric("Total Goals", int(df['Goals'].sum()))
            else:
                st.metric("Total Goals", "N/A")
        with col4:
            if 'Assists' in df.columns:
                st.metric("Total Assists", int(df['Assists'].sum()))
            else:
                st.metric("Total Assists", "N/A")
        
        st.markdown("---")
        
        # Top performers
        if 'Goals' in df.columns and 'Player_Name' in df.columns:
            st.subheader("🎯 Top 5 Scorers")
            top_scorers = df.nlargest(5, 'Goals')[['Player_Name', 'Club', 'Goals', 'Matches_Played']]
            st.dataframe(top_scorers, use_container_width=True)
        
        if 'Assists' in df.columns and 'Player_Name' in df.columns:
            st.subheader("🤝 Top 5 Assist Providers")
            top_assisters = df.nlargest(5, 'Assists')[['Player_Name', 'Club', 'Assists', 'Matches_Played']]
            st.dataframe(top_assisters, use_container_width=True)
        
        if 'Rating' in df.columns and 'Player_Name' in df.columns:
            st.subheader("⭐ Top 5 Rated Players")
            top_rated = df.nlargest(5, 'Rating')[['Player_Name', 'Club', 'Rating', 'Goals', 'Assists']]
            st.dataframe(top_rated, use_container_width=True)
        
        st.markdown("---")
        
        # Club analysis
        if 'Club' in df.columns and 'Goals' in df.columns:
            st.subheader("🏢 Club Statistics")
            
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                club_stats = df.groupby('Club')[numeric_cols].agg(['sum', 'mean']).round(2)
                st.dataframe(club_stats, use_container_width=True)
                
                # Visualization
                st.subheader("📊 Goals by Club")
                fig, ax = plt.subplots(figsize=(12, 6))
                df.groupby('Club')['Goals'].sum().sort_values(ascending=False).plot(kind='bar', ax=ax)
                plt.ylabel('Total Goals')
                plt.title('Total Goals by Club')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig)
        
        st.markdown("---")
        
        # Statistical summary
        st.subheader("📈 Statistical Summary")
        
        if 'Goals' in df.columns:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("#### Goals Statistics")
                st.write(f"**Average:** {df['Goals'].mean():.2f}")
                st.write(f"**Median:** {df['Goals'].median():.2f}")
                st.write(f"**Std Dev:** {df['Goals'].std():.2f}")
        
            with col2:
                if 'Assists' in df.columns:
                    st.markdown("#### Assists Statistics")
                    st.write(f"**Average:** {df['Assists'].mean():.2f}")
                    st.write(f"**Median:** {df['Assists'].median():.2f}")
                    st.write(f"**Std Dev:** {df['Assists'].std():.2f}")
            
            with col3:
                if 'Rating' in df.columns:
                    st.markdown("#### Rating Statistics")
                    st.write(f"**Average:** {df['Rating'].mean():.2f}")
                    st.write(f"**Median:** {df['Rating'].median():.2f}")
                    st.write(f"**Std Dev:** {df['Rating'].std():.2f}")
        
        st.markdown("---")
        
        # Correlation analysis
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) >= 2:
            st.subheader("🔗 Correlation Analysis")
            
            fig, ax = plt.subplots(figsize=(10, 8))
            correlation_matrix = df[numeric_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax, fmt='.2f')
            plt.title('Feature Correlation Matrix')
            plt.tight_layout()
            st.pyplot(fig)
        
        st.markdown("---")
        
        # Download full report
        st.subheader("💾 Download Complete Report")
        
        col1, col2 = st.columns(2)
        with col1:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Full Dataset (CSV)",
                data=csv,
                file_name='complete_analysis.csv',
                mime='text/csv',
            )
        
        with col2:
            from io import BytesIO
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Full Data', index=False)
                if 'Goals' in df.columns and 'Player_Name' in df.columns:
                    df.nlargest(10, 'Goals').to_excel(writer, sheet_name='Top Scorers', index=False)
                if 'Club' in df.columns:
                    df.groupby('Club').mean().to_excel(writer, sheet_name='Club Stats')
            
            st.download_button(
                label="⬇️ Download Full Report (Excel)",
                data=output.getvalue(),
                file_name='complete_report.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
        
        with st.expander("📝 Show Complete Code"):
            st.code("""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('football_players_2015_2024.csv')

# Overview
print(f"Total Players: {len(df)}")
print(f"Total Clubs: {df['Club'].nunique()}")
print(f"Total Goals: {df['Goals'].sum()}")

# Top performers
print("\\nTop 5 Scorers:")
print(df.nlargest(5, 'Goals')[['Player_Name', 'Club', 'Goals']])

print("\\nTop 5 Assist Providers:")
print(df.nlargest(5, 'Assists')[['Player_Name', 'Club', 'Assists']])

print("\\nTop 5 Rated Players:")
print(df.nlargest(5, 'Rating')[['Player_Name', 'Club', 'Rating']])

# Club analysis
club_stats = df.groupby('Club').agg({
    'Goals': ['sum', 'mean'],
    'Assists': ['sum', 'mean'],
    'Rating': 'mean'
}).round(2)
print("\\nClub Statistics:")
print(club_stats)

# Statistical summary
print("\\nStatistical Summary:")
print(f"Average Goals: {df['Goals'].mean():.2f}")
print(f"Average Assists: {df['Assists'].mean():.2f}")
print(f"Average Rating: {df['Rating'].mean():.2f}")

# Correlation
correlation = df[['Goals', 'Assists', 'Rating']].corr()
print("\\nCorrelation Matrix:")
print(correlation)

# Visualizations
plt.figure(figsize=(12, 6))
df.groupby('Club')['Goals'].sum().sort_values().plot(kind='barh')
plt.title('Total Goals by Club')
plt.xlabel('Goals')
plt.tight_layout()
plt.savefig('goals_by_club.png')

# Save results
df.to_csv('complete_analysis.csv', index=False)
club_stats.to_csv('club_statistics.csv')

print("\\n✅ Analysis complete!")
            """, language="python")
    else:
        st.warning("⚠️ Please upload a dataset first!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>🐼 Pandas Football Analytics Tutorial</strong></p>
    <p>Built with Streamlit | Made for learning data analysis</p>
    <p>📚 <a href='https://pandas.pydata.org/docs/' target='_blank'>Pandas Documentation</a> | 
       🎨 <a href='https://streamlit.io/' target='_blank'>Streamlit Docs</a></p>
</div>
""", unsafe_allow_html=True)
