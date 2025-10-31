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

    with st.expander("🔹 df.head() — View first rows | عرض الصفوف الأولى"):
        st.code("df.head()", language="python")
        st.dataframe(df.head())
        st.write("Shows the first 5 rows of the DataFrame.")
        st.write("يعرض أول 5 صفوف من إطار البيانات.")

    with st.expander("🔹 df.tail() — View last rows | عرض الصفوف الأخيرة"):
        st.code("df.tail()", language="python")
        st.dataframe(df.tail())
        st.write("Shows the last 5 rows of the DataFrame.")
        st.write("يعرض آخر 5 صفوف من إطار البيانات.")

    with st.expander("🔹 df.shape — Get rows and columns count | الحصول على عدد الصفوف والأعمدة"):
        st.code("df.shape", language="python")
        st.write(df.shape)
        st.write("Returns (rows, columns).")
        st.write("يعيد (الصفوف، الأعمدة).")

    with st.expander("🔹 df.columns — List all columns | قائمة بجميع الأعمدة"):
        st.code("df.columns", language="python")
        st.write(df.columns.tolist())
        st.write("Displays the names of all columns in your dataset.")
        st.write("يعرض أسماء جميع الأعمدة في مجموعة البيانات الخاصة بك.")

    with st.expander("🔹 df.info() — Show data types and non-null counts | عرض أنواع البيانات وعدد القيم غير الفارغة"):
        st.code("df.info()", language="python")
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.text(info_str)
        st.write("Displays summary info about columns, data types, and missing values.")
        st.write("يعرض معلومات موجزة عن الأعمدة وأنواع البيانات والقيم المفقودة.")

    with st.expander("🔹 df.describe() — Statistical summary | ملخص إحصائي"):
        st.code("df.describe()", language="python")
        st.dataframe(df.describe())
        st.write("Shows basic statistics for numeric columns (mean, std, min, etc.).")
        st.write("يعرض الإحصائيات الأساسية للأعمدة الرقمية (المتوسط، الانحراف المعياري، الحد الأدنى، إلخ).")

    with st.expander("🔹 df.dtypes — Data types of each column | أنواع البيانات لكل عمود"):
        st.code("df.dtypes", language="python")
        st.write(df.dtypes)
        st.write("Lists the data type of each column (int, float, object, etc.).")
        st.write("يسرد نوع البيانات لكل عمود (int, float, object، إلخ).")

    with st.expander("🔹 df.index — Index information | معلومات الفهرس"):
        st.code("df.index", language="python")
        st.write(df.index)
        st.write("Gives the index (row labels) of your DataFrame.")
        st.write("يعطي الفهرس (تسميات الصفوف) لإطار البيانات الخاص بك.")

    with st.expander("🔹 df.isnull() — Detect missing values | كشف القيم المفقودة"):
        st.code("df.isnull().sum()", language="python")
        st.dataframe(df.isnull().sum())
        st.write("Shows how many missing values are in each column.")
        st.write("يعرض عدد القيم المفقودة في كل عمود.")

    # ----------------------------
    # 🧹 STEP 3: DATA CLEANING
    # ----------------------------
    st.header("🧹 Data Cleaning Functions | وظائف تنظيف البيانات")

    with st.expander("🔹 df.dropna() — Remove missing rows | إزالة الصفوف المفقودة"):
        st.code("df.dropna()", language="python")
        st.dataframe(df.dropna().head())
        st.write("Removes all rows with missing values.")
        st.write("يزيل جميع الصفوف التي تحتوي على قيم مفقودة.")

    with st.expander("🔹 df.fillna() — Replace missing values | استبدال القيم المفقودة"):
        st.code("df.fillna(value)", language="python")
        st.dataframe(df.fillna(0).head())
        st.write("Replaces missing values with the given value (e.g., 0).")
        st.write("يستبدل القيم المفقودة بالقيمة المعطاة (مثل، 0).")

    with st.expander("🔹 df.rename() — Rename columns | إعادة تسمية الأعمدة"):
        st.code("df.rename(columns={'OldName':'NewName'})", language="python")
        st.write("Allows renaming columns in your dataset.")
        st.write("يسمح بإعادة تسمية الأعمدة في مجموعة البيانات الخاصة بك.")

    with st.expander("🔹 df.drop() — Remove columns or rows | إزالة الأعمدة أو الصفوف"):
        st.code("df.drop('ColumnName', axis=1)", language="python")
        st.write("Removes the specified column or row.")
        st.write("يزيل العمود أو الصف المحدد.")

    with st.expander("🔹 df.duplicated() & df.drop_duplicates() — Remove duplicates | إزالة التكرارات"):
        st.code("df.drop_duplicates()", language="python")
        st.write("Removes duplicate rows from your dataset.")
        st.write("يزيل الصفوف المكررة من مجموعة البيانات الخاصة بك.")

    # ----------------------------
    # 🔍 STEP 4: FILTERING & SELECTION
    # ----------------------------
    st.header("🔍 Filtering and Selection | التصفية والاختيار")

    with st.expander("🔹 Select one column | اختيار عمود واحد"):
        st.code("df['ColumnName']", language="python")
        column = st.selectbox("Select a column to view:", df.columns)
        st.dataframe(df[column].head())
        st.write("Selects and displays a single column from the DataFrame.")
        st.write("يختار ويعرض عمودًا واحدًا من إطار البيانات.")

    with st.expander("🔹 Select multiple columns | اختيار أعمدة متعددة"):
        st.code("df[['Col1', 'Col2']]", language="python")
        cols = st.multiselect("Choose columns:", df.columns)
        if cols:
            st.dataframe(df[cols].head())
        st.write("Selects and displays multiple columns at once.")
        st.write("يختار ويعرض عدة أعمدة في وقت واحد.")

    with st.expander("🔹 Filter rows with condition | تصفية الصفوف بشرط"):
        st.code("df[df['Goals'] > 10]", language="python")
        st.write("Example: `df[df['Goals'] > 10]` filters rows where Goals > 10.")
        st.write("مثال: `df[df['Goals'] > 10]` يصفي الصفوف حيث Goals > 10.")

    with st.expander("🔹 iloc and loc — Index selection | اختيار الفهرس"):
        st.code("df.iloc[0:5, 0:3]  # by index\ndf.loc[0:5, ['Name','Club']]", language="python")
        st.write("Select rows and columns by index (`iloc`) or by label (`loc`).")
        st.write("اختيار الصفوف والأعمدة بالفهرس (`iloc`) أو بالتسمية (`loc`).")

    # ----------------------------
    # 📈 STEP 5: SORTING & GROUPING
    # ----------------------------
    st.header("📈 Sorting and Grouping | الترتيب والتجميع")

    with st.expander("🔹 Sort by column | الترتيب حسب العمود"):
        st.code("df.sort_values(by='Goals', ascending=False)", language="python")
        st.dataframe(df.sort_values(by=df.columns[0], ascending=False).head())
        st.write("Sorts data by a chosen column.")
        st.write("يرتب البيانات حسب عمود مختار.")

    with st.expander("🔹 Group by and aggregate | التجميع والتجميع"):
        st.code("df.groupby('Club').mean()", language="python")
        col_group = st.selectbox("Select a column to group by:", df.columns)
        grouped = df.groupby(col_group).mean(numeric_only=True)
        st.dataframe(grouped.head())
        st.write("Groups data by the selected column and shows the mean of numeric columns.")
        st.write("يجمع البيانات حسب العمود المحدد ويعرض متوسط الأعمدة الرقمية.")

    with st.expander("🔹 df.value_counts() — Count unique values | عد القيم الفريدة"):
        st.code("df['ColumnName'].value_counts()", language="python")
        col_val = st.selectbox("Select a column for value counts:", df.columns, key="value_counts")
        st.dataframe(df[col_val].value_counts())
        st.write("Counts how many times each unique value appears in the column.")
        st.write("يحسب عدد المرات التي تظهر فيها كل قيمة فريدة في العمود.")

    # ----------------------------
    # 🧮 STEP 6: ADVANCED FUNCTIONS
    # ----------------------------
    st.header("🧮 Advanced Pandas Functions | الوظائف المتقدمة")

    with st.expander("🔹 df.apply() — Apply custom functions | تطبيق وظائف مخصصة"):
        st.code("df['Goals'].apply(lambda x: x * 2)", language="python")
        st.write("Applies a function to each element of a column.")
        st.write("يطبق دالة على كل عنصر من عناصر العمود.")

    with st.expander("🔹 df.merge() — Combine two datasets | دمج مجموعتي بيانات"):
        st.code("pd.merge(df1, df2, on='ID')", language="python")
        st.write("Merges two DataFrames based on a common column.")
        st.write("يدمج إطارين من البيانات بناءً على عمود مشترك.")

    with st.expander("🔹 df.concat() — Stack datasets together | تكديس مجموعات البيانات معًا"):
        st.code("pd.concat([df1, df2])", language="python")
        st.write("Combines multiple DataFrames vertically or horizontally.")
        st.write("يجمع عدة إطارات بيانات عموديًا أو أفقيًا.")

    with st.expander("🔹 df.pivot_table() — Create summary tables | إنشاء جداول ملخصة"):
        st.code("pd.pivot_table(df, values='Goals', index='Club', aggfunc='mean')", language="python")
        st.write("Creates pivot tables for summarizing data easily.")
        st.write("ينشئ جداول محورية لتلخيص البيانات بسهولة.")

    # ----------------------------
    # 💾 STEP 7: SAVE RESULTS
    # ----------------------------
    st.header("💾 Save and Export Data | حفظ وتصدير البيانات")

    with st.expander("🔹 Save to CSV | الحفظ كملف CSV"):
        st.code("df.to_csv('output.csv', index=False)", language="python")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download CSV", csv, "cleaned_data.csv", "text/csv")
        st.write("Exports DataFrame to CSV format for easy sharing and storage.")
        st.write("يصدر إطار البيانات إلى تنسيق CSV لسهولة المشاركة والتخزين.")

    with st.expander("🔹 Save to Excel | الحفظ كملف Excel"):
        st.code("df.to_excel('output.xlsx', index=False)", language="python")
        st.write("Exports DataFrame to Excel format.")
        st.write("يصدر إطار البيانات إلى تنسيق Excel.")

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
