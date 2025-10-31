import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# APP TITLE
# -------------------------------
st.set_page_config(page_title="📊 Learn Pandas from 0 to Hero", layout="wide")
st.title("🐼 Learn Pandas from 0 to Hero")
st.write("Welcome! This app will help you understand **Pandas** step by step using your own dataset.")

# -------------------------------
# STEP 1: UPLOAD DATASET
# -------------------------------
st.header("📂 Step 1: Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File loaded successfully!")
    
    # Display basic info
    st.subheader("👀 Preview of Your Data")
    st.dataframe(df.head())

    # -------------------------------
    # STEP 2: LEARN BASIC COMMANDS
    # -------------------------------
    st.header("📘 Step 2: Basic Pandas Commands")

    with st.expander("🔹 View the first few rows of the dataset"):
        st.code("df.head()", language="python")
        st.dataframe(df.head())
        st.write("Shows the **first 5 rows** of your dataset. You can use `df.head(10)` to show 10 rows.")

    with st.expander("🔹 View the last few rows of the dataset"):
        st.code("df.tail()", language="python")
        st.dataframe(df.tail())
        st.write("Shows the **last 5 rows** of your dataset.")

    with st.expander("🔹 Get basic information about the dataset"):
        st.code("df.info()", language="python")
        buffer = []
        df.info(buf=buffer)
        s = "\n".join(buffer)
        st.text(s)
        st.write("Gives info about **columns, data types, and missing values**.")

    with st.expander("🔹 Summary statistics"):
        st.code("df.describe()", language="python")
        st.dataframe(df.describe())
        st.write("Provides **mean, min, max, and standard deviation** for numeric columns.")

    with st.expander("🔹 Check for missing values"):
        st.code("df.isnull().sum()", language="python")
        st.dataframe(df.isnull().sum())
        st.write("Shows how many **missing values** are in each column.")

    with st.expander("🔹 Get column names"):
        st.code("df.columns", language="python")
        st.write(df.columns.tolist())
        st.write("Lists all column names in your dataset.")

    with st.expander("🔹 Select a single column"):
        st.code("df['column_name']", language="python")
        column = st.selectbox("Select a column to view:", df.columns)
        st.dataframe(df[column])
        st.write("Displays all values in the selected column.")

    with st.expander("🔹 Filter rows (example: players with goals > 10)"):
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if numeric_cols:
            selected_col = st.selectbox("Select a numeric column to filter:", numeric_cols)
            threshold = st.slider("Choose a threshold:", float(df[selected_col].min()), float(df[selected_col].max()))
            filtered = df[df[selected_col] > threshold]
            st.dataframe(filtered)
            st.write("Shows rows where the selected column value is greater than your threshold.")

    # -------------------------------
    # STEP 3: VISUALIZATION
    # -------------------------------
    st.header("📊 Step 3: Data Visualization with Pandas")

    with st.expander("🔹 Plot a column (Histogram)"):
        num_col = st.selectbox("Select a numeric column to plot:", numeric_cols, key="plot_col")
        fig, ax = plt.subplots()
        df[num_col].hist(ax=ax, bins=20)
        st.pyplot(fig)
        st.write("Visualizes the distribution of the selected column.")

    with st.expander("🔹 Correlation Heatmap"):
        fig, ax = plt.subplots(figsize=(6,4))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
        st.write("Shows correlation between numeric columns — how they move together.")

    # -------------------------------
    # STEP 4: GROUPING & SORTING
    # -------------------------------
    st.header("📈 Step 4: Grouping and Sorting")

    with st.expander("🔹 Sort values"):
        col_sort = st.selectbox("Choose a column to sort by:", df.columns)
        sorted_df = df.sort_values(by=col_sort, ascending=False)
        st.dataframe(sorted_df.head())
        st.write("Sorts the dataset by the selected column (descending order).")

    with st.expander("🔹 Group by column"):
        col_group = st.selectbox("Select a column to group by:", df.columns)
        grouped = df.groupby(col_group).mean(numeric_only=True)
        st.dataframe(grouped.head())
        st.write("Groups the dataset by the selected column and calculates the mean for numeric values.")

    # -------------------------------
    # STEP 5: SAVE & DOWNLOAD
    # -------------------------------
    st.header("💾 Step 5: Save Your Work")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Cleaned Dataset", data=csv, file_name="cleaned_data.csv", mime="text/csv")
else:
    st.info("👆 Upload a CSV file to begin learning Pandas!")
