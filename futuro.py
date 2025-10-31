import streamlit as st
import pandas as pd
import io

# ----------------------------
# 🏷️ APP CONFIGURATION
# ----------------------------
st.set_page_config(page_title="🐼 Pandas from 0 to Hero | Futuro School", layout="wide")

# ----------------------------
# 🎓 HEADER & BRANDING
# ----------------------------
st.title("🐼 Learn All Pandas Functions — From 0 to Hero")
st.write("This app teaches **Pandas** step by step using your dataset. Upload a CSV file and explore every important function interactively!")
st.write("هذا التطبيق يعلم **Pandas** خطوة بخطوة باستخدام بياناتك. قم بتحميل ملف CSV واستكشف كل وظيفة مهمة بشكل تفاعلي!")
st.markdown("### 🎓 **Futuro School** | Created by Teacher **Hadjar Nayla**")
st.markdown("---")

# ----------------------------
# 📂 STEP 1: UPLOAD DATASET
# ----------------------------
st.header("📁 Step 1: Upload a CSV file | الخطوة الأولى: تحميل ملف CSV")
st.write("Upload your dataset to begin exploring Pandas functions | قم بتحميل مجموعة البيانات الخاصة بك لبدء استكشاف وظائف Pandas")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset loaded successfully! | تم تحميل مجموعة البيانات بنجاح!")
    st.dataframe(df.head())

    # ----------------------------
    # 📘 STEP 2: BASIC FUNCTIONS
    # ----------------------------
    st.header("📘 Basic Pandas Functions | الوظائف الأساسية")

    with st.expander("🔹 df.head() — View first rows"):
        st.code("df.head()", language="python")
        st.dataframe(df.head())
        st.write("Shows the first 5 rows of the DataFrame.")

    with st.expander("🔹 df.tail() — View last rows"):
        st.code("df.tail()", language="python")
        st.dataframe(df.tail())
        st.write("Shows the last 5 rows of the DataFrame.")

    with st.expander("🔹 df.shape — Get rows and columns count"):
        st.code("df.shape", language="python")
        st.write(df.shape)
        st.write("Returns (rows, columns).")

    with st.expander("🔹 df.columns — List all columns"):
        st.code("df.columns", language="python")
        st.write(df.columns.tolist())
        st.write("Displays the names of all columns in your dataset.")

    with st.expander("🔹 df.info() — Show data types and non-null counts"):
        st.code("df.info()", language="python")
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.text(info_str)
        st.write("Displays summary info about columns, data types, and missing values.")

    with st.expander("🔹 df.describe() — Statistical summary"):
        st.code("df.describe()", language="python")
        st.dataframe(df.describe())
        st.write("Shows basic statistics for numeric columns (mean, std, min, etc.).")

    with st.expander("🔹 df.dtypes — Data types of each column"):
        st.code("df.dtypes", language="python")
        st.write(df.dtypes)
        st.write("Lists the data type of each column (int, float, object, etc.).")

    with st.expander("🔹 df.index — Index information"):
        st.code("df.index", language="python")
        st.write(df.index)
        st.write("Gives the index (row labels) of your DataFrame.")

    with st.expander("🔹 df.isnull() — Detect missing values"):
        st.code("df.isnull().sum()", language="python")
        st.dataframe(df.isnull().sum())
        st.write("Shows how many missing values are in each column.")

    # ----------------------------
    # 🧹 STEP 3: DATA CLEANING
    # ----------------------------
    st.header("🧹 Data Cleaning Functions | وظائف تنظيف البيانات")

    with st.expander("🔹 df.dropna() — Remove missing rows"):
        st.code("df.dropna()", language="python")
        st.dataframe(df.dropna().head())
        st.write("Removes all rows with missing values.")

    with st.expander("🔹 df.fillna() — Replace missing values"):
        st.code("df.fillna(value)", language="python")
        st.dataframe(df.fillna(0).head())
        st.write("Replaces missing values with the given value (e.g., 0).")

    with st.expander("🔹 df.rename() — Rename columns"):
        st.code("df.rename(columns={'OldName':'NewName'})", language="python")
        st.write("Allows renaming columns in your dataset.")

    with st.expander("🔹 df.drop() — Remove columns or rows"):
        st.code("df.drop('ColumnName', axis=1)", language="python")
        st.write("Removes the specified column or row.")

    with st.expander("🔹 df.duplicated() & df.drop_duplicates()"):
        st.code("df.drop_duplicates()", language="python")
        st.write("Removes duplicate rows from your dataset.")

    # ----------------------------
    # 🔍 STEP 4: FILTERING & SELECTION
    # ----------------------------
    st.header("🔍 Filtering and Selection | التصفية والاختيار")

    with st.expander("🔹 Select one column"):
        st.code("df['ColumnName']", language="python")
        column = st.selectbox("Select a column to view:", df.columns)
        st.dataframe(df[column].head())

    with st.expander("🔹 Select multiple columns"):
        st.code("df[['Col1', 'Col2']]", language="python")
        cols = st.multiselect("Choose columns:", df.columns)
        if cols:
            st.dataframe(df[cols].head())

    with st.expander("🔹 Filter rows with condition"):
        st.code("df[df['Goals'] > 10]", language="python")
        st.write("Example: `df[df['Goals'] > 10]` filters rows where Goals > 10.")

    with st.expander("🔹 iloc and loc — Index selection"):
        st.code("df.iloc[0:5, 0:3]  # by index\n df.loc[0:5, ['Name','Club']]", language="python")
        st.write("Select rows and columns by index (`iloc`) or by label (`loc`).")

    # ----------------------------
    # 📈 STEP 5: SORTING & GROUPING
    # ----------------------------
    st.header("📈 Sorting and Grouping | الترتيب والتجميع")

    with st.expander("🔹 Sort by column"):
        st.code("df.sort_values(by='Goals', ascending=False)", language="python")
        st.dataframe(df.sort_values(by=df.columns[0], ascending=False).head())
        st.write("Sorts data by a chosen column.")

    with st.expander("🔹 Group by and aggregate"):
        st.code("df.groupby('Club').mean()", language="python")
        col_group = st.selectbox("Select a column to group by:", df.columns)
        grouped = df.groupby(col_group).mean(numeric_only=True)
        st.dataframe(grouped.head())
        st.write("Groups data by the selected column and shows the mean of numeric columns.")

    with st.expander("🔹 df.value_counts() — Count unique values"):
        st.code("df['ColumnName'].value_counts()", language="python")
        col_val = st.selectbox("Select a column for value counts:", df.columns)
        st.dataframe(df[col_val].value_counts())
        st.write("Counts how many times each unique value appears in the column.")

    # ----------------------------
    # 🧮 STEP 6: ADVANCED FUNCTIONS
    # ----------------------------
    st.header("🧮 Advanced Pandas Functions | الوظائف المتقدمة")

    with st.expander("🔹 df.apply() — Apply custom functions"):
        st.code("df['Goals'].apply(lambda x: x * 2)", language="python")
        st.write("Applies a function to each element of a column.")

    with st.expander("🔹 df.merge() — Combine two datasets"):
        st.code("pd.merge(df1, df2, on='ID')", language="python")
        st.write("Merges two DataFrames based on a common column.")

    with st.expander("🔹 df.concat() — Stack datasets together"):
        st.code("pd.concat([df1, df2])", language="python")
        st.write("Combines multiple DataFrames vertically or horizontally.")

    with st.expander("🔹 df.pivot_table() — Create summary tables"):
        st.code("pd.pivot_table(df, values='Goals', index='Club', aggfunc='mean')", language="python")
        st.write("Creates pivot tables for summarizing data easily.")

    # ----------------------------
    # 💾 STEP 7: SAVE RESULTS
    # ----------------------------
    st.header("💾 Save and Export Data | حفظ وتصدير البيانات")

    with st.expander("🔹 Save to CSV"):
        st.code("df.to_csv('output.csv', index=False)", language="python")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download CSV", csv, "cleaned_data.csv", "text/csv")

    with st.expander("🔹 Save to Excel"):
        st.code("df.to_excel('output.xlsx', index=False)", language="python")
        st.write("Exports DataFrame to Excel format.")

    # ----------------------------
    # 📝 FOOTER
    # ----------------------------
    st.markdown("---")
    st.markdown("### 🎓 Futuro School - Excellence in Data Science Education")
    st.markdown("**Developed by Teacher Hadjar Nayla** | تم تطويره بواسطة المعلمة حجار نايلة")
    st.markdown("*Empowering students with practical data analysis skills* | *تمكين الطلاب بمهارات تحليل البيانات العملية*")

else:
    st.info("👆 Please upload a CSV file to start learning Pandas! | يرجى تحميل ملف CSV لبدء تعلم Pandas!")
    st.markdown("---")
    st.markdown("### 🎓 Futuro School")
    st.markdown("**Created by Teacher Hadjar Nayla** | تم الإنشاء بواسطة المعلمة حجار نايلة")
