# 🐼 Learn Pandas from 0 to Hero - Streamlit App
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ------------------------------------
# 🏷️ APP CONFIGURATION
# ------------------------------------
st.set_page_config(page_title="🐼 Learn Pandas from 0 to Hero", layout="wide")
st.title("📊 Learn Pandas from 0 to Hero")
st.write("Welcome! This interactive app helps beginners learn **Pandas** step by step using any dataset (like your football players dataset).")

# ------------------------------------
# 📂 STEP 1: UPLOAD YOUR DATASET
# ------------------------------------
st.header("📁 Step 1: Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    st.subheader("👀 Preview of Your Dataset")
    st.dataframe(df.head())

    # ------------------------------------
    # 📘 STEP 2: LEARN BASIC PANDAS COMMANDS
    # ------------------------------------
    st.header("📘 Step 2: Basic Pandas Commands")

    with st.expander("🔹 View the first few rows"):
        st.code("df.head()", language="python")
        st.dataframe(df.head())
        st.write("Displays the **first 5 rows** of the dataset. Use `df.head(10)` to show more.")

    with st.expander("🔹 View the last few rows"):
        st.code("df.tail()", language="python")
        st.dataframe(df.tail())
        st.write("Displays the **last 5 rows** of the dataset.")

    with st.expander("🔹 Get basic information about the dataset"):
        st.code("df.info()", language="python")
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.text(info_str)
        st.write("Shows information about **columns, data types, and missing values**.")

    with st.expander("🔹 Summary statistics of numeric data"):
        st.code("df.describe()", language="python")
        st.dataframe(df.describe())
        st.write("Shows **count, mean, min, max, and standard deviation** for numeric columns.")

    with st.expander("🔹 Check for missing values"):
        st.code("df.isnull().sum()", language="python")
        st.dataframe(df.isnull().sum())
        st.write("Shows how many **missing values** exist in each column.")

    with st.expander("🔹 List column names"):
        st.code("df.columns", language="python")
        st.write(df.columns.tolist())
        st.write("Lists all column names in your dataset.")

    with st.expander("🔹 Select a specific column"):
        st.code("df['column_name']", language="python")
        column = st.selectbox("Select a column to display:", df.columns)
        st.dataframe(df[column])
        st.write("Displays all values from the chosen column.")

    with st.expander("🔹 Filter rows (example: Goals > 10)"):
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if numeric_cols:
            selected_col = st.selectbox("Select a numeric column to filter:", numeric_cols)
            threshold = st.slider("Select a threshold:", float(df[selected_col].min()), float(df[selected_col].max()))
            filtered = df[df[selected_col] > threshold]
            st.dataframe(filtered)
            st.write(f"Displays rows where `{selected_col}` is greater than {threshold}.")
        else:
            st.warning("No numeric columns available for filtering.")

    # ------------------------------------
    # 📊 STEP 3: VISUALIZATION
    # ------------------------------------
    st.header("📊 Step 3: Data Visualization")

    with st.expander("🔹 Histogram"):
        if numeric_cols:
            num_col = st.selectbox("Select a numeric column to plot:", numeric_cols, key="hist_col")
            fig, ax = plt.subplots()
            df[num_col].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {num_col}")
            st.pyplot(fig)
            st.write("A histogram shows how data is distributed across values.")
        else:
            st.warning("No numeric columns to visualize.")

    with st.expander("🔹 Correlation Heatmap"):
        if len(numeric_cols) > 1:
            fig, ax = plt.subplots(figsize=(6,4))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
            st.write("Shows the correlation between numeric columns (how they change together).")
        else:
            st.warning("Not enough numeric columns for a correlation heatmap.")

    # ------------------------------------
    # 📈 STEP 4: GROUPING & SORTING
    # ------------------------------------
    st.header("📈 Step 4: Grouping and Sorting")

    with st.expander("🔹 Sort the dataset by a column"):
        col_sort = st.selectbox("Select a column to sort by:", df.columns)
        sorted_df = df.sort_values(by=col_sort, ascending=False)
        st.dataframe(sorted_df.head())
        st.write(f"Sorts the dataset by `{col_sort}` in descending order.")

    with st.expander("🔹 Group by column and calculate averages"):
        col_group = st.selectbox("Select a column to group by:", df.columns)
        grouped = df.groupby(col_group).mean(numeric_only=True)
        st.dataframe(grouped.head())
        st.write(f"Groups the dataset by `{col_group}` and shows the average for numeric columns.")

    # ------------------------------------
    # 💾 STEP 5: SAVE & DOWNLOAD
    # ------------------------------------
    st.header("💾 Step 5: Save and Download Processed Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV file to begin learning Pandas!")
