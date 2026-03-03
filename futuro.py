import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from io import BytesIO

# ----------------------------
# 🏷️ APP CONFIGURATION
# ----------------------------
st.set_page_config(page_title="🐼 Pandas from 0 to Hero | Futuro School", layout="wide")

# ----------------------------
# 🎓 HEADER & BRANDING
# ----------------------------
st.title("🐼 تعلم جميع وظائف Pandas — من الصفر إلى الاحتراف")
st.title("🐼 Learn All Pandas Functions — From 0 to Hero")
st.write("**English:** This app teaches Pandas step by step using your dataset. Upload a CSV file and explore every important function interactively!")
st.markdown("### 🎓  Futuro School**")
st.markdown("**تم التطوير بواسطة الأستاذة: حجار نايلة | Developed by Teacher: Hadjar Nayla**")
st.markdown("---")

# ----------------------------
# 📂 UPLOAD DATASET
# ----------------------------
st.header("📁 الخطوة 1: تحميل ملف CSV | Step 1: Upload a CSV file")
uploaded_file = st.file_uploader("ارفع ملف CSV | Upload a CSV file", type=["csv"])

# Helper functions
def safe_head(df, n=5):
    """عرض آمن لأول n صف | Safe display of first n rows"""
    try:
        return df.head(n)
    except Exception:
        return df.iloc[:n, :]

def df_to_excel_bytes(df):
    """تحويل DataFrame إلى بايتات Excel | Convert DataFrame to Excel bytes"""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
    return buffer.getvalue()

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='utf-8', sep=None, engine='python')
        except Exception as e:
            st.error(f"فشل قراءة الملف | Failed to read CSV: {e}")
            st.stop()

    st.success("✅ تم تحميل البيانات بنجاح! | Dataset loaded successfully!")
    st.dataframe(safe_head(df, 5))

    # ----------------------------
    # 📘 SECTION 1: BASIC FUNCTIONS
    # القسم 1: الوظائف الأساسية
    # ----------------------------
    st.markdown("---")
    st.header("📘 القسم 1: الوظائف الأساسية | Section 1: Basic Functions")
    st.write("**العربية:** تعلم الوظائف الأساسية للتعرف على البيانات")
    st.write("**English:** Learn basic functions to explore your data")

    with st.expander("1️⃣ df.head() — عرض الصفوف الأولى | View first rows"):
        st.code("df.head()", language="python")
        st.write("**العربية:** يعرض أول 5 صفوف من إطار البيانات")
        st.write("**English:** Shows the first 5 rows of the DataFrame")
        st.dataframe(safe_head(df, 5))

    with st.expander("2️⃣ df.tail() — عرض الصفوف الأخيرة | View last rows"):
        st.code("df.tail()", language="python")
        st.write("**العربية:** يعرض آخر 5 صفوف من إطار البيانات")
        st.write("**English:** Shows the last 5 rows of the DataFrame")
        st.dataframe(df.tail(5))

    with st.expander("3️⃣ df.shape — الحصول على عدد الصفوف والأعمدة | Get rows and columns count"):
        st.code("df.shape", language="python")
        st.write("**العربية:** يعيد (عدد الصفوف، عدد الأعمدة)")
        st.write("**English:** Returns (number of rows, number of columns)")
        st.write(f"الشكل | Shape: {df.shape}")
        st.write(f"عدد الصفوف | Rows: {df.shape[0]}")
        st.write(f"عدد الأعمدة | Columns: {df.shape[1]}")

    with st.expander("4️⃣ df.columns — قائمة جميع الأعمدة | List all columns"):
        st.code("df.columns", language="python")
        st.write("**العربية:** يعرض أسماء جميع الأعمدة في مجموعة البيانات")
        st.write("**English:** Displays the names of all columns in your dataset")
        st.write(df.columns.tolist())

    with st.expander("5️⃣ df.info() — معلومات عن أنواع البيانات | Data types information"):
        st.code("df.info()", language="python")
        st.write("**العربية:** ملخص عن الأعمدة وأنواع البيانات والقيم المفقودة")
        st.write("**English:** Summary about columns, data types, and missing values")
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

    with st.expander("6️⃣ df.describe() — الملخص الإحصائي | Statistical summary"):
        st.code("df.describe()", language="python")
        st.write("**العربية:** إحصائيات للأعمدة الرقمية (المتوسط، الحد الأدنى، الحد الأقصى، إلخ)")
        st.write("**English:** Statistics for numeric columns (mean, min, max, etc.)")
        st.dataframe(df.describe(include='all'))

    with st.expander("7️⃣ df.dtypes — أنواع البيانات لكل عمود | Data types of each column"):
        st.code("df.dtypes", language="python")
        st.write("**العربية:** يسرد نوع البيانات لكل عمود (int, float, object, إلخ)")
        st.write("**English:** Lists the data type of each column (int, float, object, etc.)")
        st.write(df.dtypes)

    with st.expander("8️⃣ df.index — معلومات الفهرس | Index information"):
        st.code("df.index", language="python")
        st.write("**العربية:** يعطي معلومات عن فهرس الصفوف")
        st.write("**English:** Gives information about the row index")
        st.write(df.index)

    with st.expander("9️⃣ df.isnull() — كشف القيم المفقودة | Detect missing values"):
        st.code("df.isnull().sum()", language="python")
        st.write("**العربية:** يعرض عدد القيم المفقودة في كل عمود")
        st.write("**English:** Shows count of missing values per column")
        st.write(df.isnull().sum())

    # ----------------------------
    # 🧹 SECTION 2: DATA CLEANING
    # القسم 2: تنظيف البيانات
    # ----------------------------
    st.markdown("---")
    st.header("🧹 القسم 2: تنظيف البيانات | Section 2: Data Cleaning")
    st.write("**العربية:** تعلم كيفية تنظيف وتحضير بياناتك")
    st.write("**English:** Learn how to clean and prepare your data")

    with st.expander("🔟 df.dropna() — إزالة الصفوف المفقودة | Remove missing rows"):
        st.code("df.dropna()", language="python")
        st.write("**العربية:** يزيل جميع الصفوف التي تحتوي على قيم مفقودة")
        st.write("**English:** Removes all rows containing missing values")
        st.write(f"عدد الصفوف قبل الحذف | Rows before: {len(df)}")
        st.write(f"عدد الصفوف بعد الحذف | Rows after: {len(df.dropna())}")
        st.dataframe(safe_head(df.dropna(), 5))

    with st.expander("1️⃣1️⃣ df.fillna() — استبدال القيم المفقودة | Replace missing values"):
        st.code("df.fillna(value)", language="python")
        st.write("**العربية:** يستبدل القيم المفقودة بقيمة محددة")
        st.write("**English:** Replaces missing values with a specified value")
        fill_value = st.text_input("القيمة البديلة | Fill value (e.g., 0 or 'unknown'):", "0")
        try:
            fv = float(fill_value)
        except:
            fv = fill_value
        st.dataframe(safe_head(df.fillna(fv), 5))

    with st.expander("1️⃣2️⃣ df.rename() — إعادة تسمية الأعمدة | Rename columns"):
        st.code("df.rename(columns={'OldName':'NewName'})", language="python")
        st.write("**العربية:** يعيد تسمية الأعمدة المحددة")
        st.write("**English:** Renames specified columns")
        col_old = st.selectbox("اختر عمود لإعادة التسمية | Select column to rename:", df.columns, key="rename_old")
        col_new = st.text_input("الاسم الجديد | New name:", f"{col_old}_renamed", key="rename_new")
        if st.button("إعادة التسمية | Rename"):
            df_renamed = df.rename(columns={col_old: col_new})
            st.success(f"✅ تم: {col_old} ← {col_new}")
            st.write(df_renamed.columns.tolist())

    with st.expander("1️⃣3️⃣ df.drop() — حذف الأعمدة أو الصفوف | Remove columns or rows"):
        st.code("df.drop('ColumnName', axis=1)", language="python")
        st.write("**العربية:** يحذف الأعمدة أو الصفوف المحددة")
        st.write("**English:** Removes specified columns or rows")
        to_drop = st.multiselect("اختر أعمدة للحذف (معاينة فقط) | Select columns to drop (preview):", df.columns)
        if to_drop:
            st.dataframe(safe_head(df.drop(columns=to_drop), 5))
        else:
            st.write("لم يتم اختيار أعمدة | No columns selected")

    with st.expander("1️⃣4️⃣ df.drop_duplicates() — إزالة التكرارات | Remove duplicates"):
        st.code("df.drop_duplicates()", language="python")
        st.write("**العربية:** يزيل الصفوف المكررة")
        st.write("**English:** Removes duplicate rows")
        st.write(f"عدد الصفوف المكررة | Duplicate rows: {int(df.duplicated().sum())}")
        st.dataframe(safe_head(df.drop_duplicates(), 5))

    # ----------------------------
    # 🔍 SECTION 3: FILTERING & SELECTION
    # القسم 3: التصفية والاختيار
    # ----------------------------
    st.markdown("---")
    st.header("🔍 القسم 3: التصفية والاختيار | Section 3: Filtering & Selection")
    st.write("**العربية:** تعلم كيفية اختيار وتصفية البيانات")
    st.write("**English:** Learn how to select and filter data")

    with st.expander("1️⃣5️⃣ df['column'] — اختيار عمود واحد | Select one column"):
        st.code("df['ColumnName']", language="python")
        st.write("**العربية:** يختار عمود واحد من البيانات")
        st.write("**English:** Selects a single column from the data")
        column = st.selectbox("اختر عمود | Select column:", df.columns, key="single_col")
        st.dataframe(safe_head(df[[column]], 5))

    with st.expander("1️⃣6️⃣ df[['col1', 'col2']] — اختيار أعمدة متعددة | Select multiple columns"):
        st.code("df[['Col1', 'Col2']]", language="python")
        st.write("**العربية:** يختار عدة أعمدة في نفس الوقت")
        st.write("**English:** Selects multiple columns at once")
        cols = st.multiselect("اختر أعمدة | Choose columns:", df.columns, key="multi_cols")
        if cols:
            st.dataframe(safe_head(df[cols], 5))
        else:
            st.write("لم يتم اختيار أعمدة | No columns selected")

    with st.expander("1️⃣7️⃣ df[condition] — تصفية الصفوف بشرط | Filter rows with condition"):
        st.code("df[df['Goals'] > 10]", language="python")
        st.write("**العربية:** يصفي الصفوف بناءً على شرط معين")
        st.write("**English:** Filters rows based on a condition")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            cond_col = st.selectbox("العمود للتصفية | Column to filter:", numeric_cols, key="filter_col")
            op = st.selectbox("المعامل | Operator:", [">", "<", ">=", "<=", "==", "!="], key="filter_op")
            value = st.text_input("القيمة للمقارنة | Value to compare:", "0", key="filter_val")
            try:
                val = float(value)
                if op == ">": out = df[df[cond_col] > val]
                elif op == "<": out = df[df[cond_col] < val]
                elif op == ">=": out = df[df[cond_col] >= val]
                elif op == "<=": out = df[df[cond_col] <= val]
                elif op == "==": out = df[df[cond_col] == val]
                else: out = df[df[cond_col] != val]
                st.write(f"عدد الصفوف المفلترة | Filtered rows: {len(out)}")
                st.dataframe(safe_head(out, 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns available")

    with st.expander("1️⃣8️⃣ df.iloc & df.loc — اختيار بالفهرس | Index-based selection"):
        st.code("df.iloc[0:5, 0:3]  # by position\ndf.loc[0:5, ['Name','Club']]  # by label", language="python")
        st.write("**العربية:** iloc للاختيار بالموضع، loc للاختيار بالتسمية")
        st.write("**English:** iloc for position-based, loc for label-based selection")
        rstart = st.number_input("بداية الصف | Row start:", min_value=0, max_value=max(0, len(df)-1), value=0, key="iloc_rs")
        rend = st.number_input("نهاية الصف | Row end:", min_value=0, max_value=len(df), value=min(5, len(df)), key="iloc_re")
        cstart = st.number_input("بداية العمود | Col start:", min_value=0, max_value=max(0, len(df.columns)-1), value=0, key="iloc_cs")
        cend = st.number_input("نهاية العمود | Col end:", min_value=0, max_value=len(df.columns), value=min(3, len(df.columns)), key="iloc_ce")
        try:
            st.dataframe(df.iloc[int(rstart):int(rend), int(cstart):int(cend)])
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    # ----------------------------
    # 📈 SECTION 4: SORTING & GROUPING
    # القسم 4: الترتيب والتجميع
    # ----------------------------
    st.markdown("---")
    st.header("📈 القسم 4: الترتيب والتجميع | Section 4: Sorting & Grouping")
    st.write("**العربية:** تعلم كيفية ترتيب وتجميع البيانات")
    st.write("**English:** Learn how to sort and group data")

    with st.expander("1️⃣9️⃣ df.sort_values() — الترتيب حسب عمود | Sort by column"):
        st.code("df.sort_values(by='Goals', ascending=False)", language="python")
        st.write("**العربية:** يرتب البيانات حسب عمود محدد (تصاعدي أو تنازلي)")
        st.write("**English:** Sorts data by a specified column (ascending or descending)")
        sort_col = st.selectbox("اختر عمود للترتيب | Select column to sort:", df.columns, key="sort_col")
        asc = st.checkbox("تصاعدي؟ | Ascending?", value=False, key="sort_asc")
        try:
            st.dataframe(safe_head(df.sort_values(by=sort_col, ascending=asc), 10))
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣0️⃣ df.groupby() — التجميع والتلخيص | Group and aggregate"):
        st.code("df.groupby('Club').mean()", language="python")
        st.write("**العربية:** يجمع البيانات حسب فئة ويحسب إحصائيات")
        st.write("**English:** Groups data by category and calculates statistics")
        col_group = st.selectbox("اختر عمود للتجميع | Select grouping column:", df.columns, key="group_col")
        try:
            grouped = df.groupby(col_group).mean(numeric_only=True)
            st.dataframe(safe_head(grouped, 10))
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣1️⃣ df.value_counts() — عد القيم الفريدة | Count unique values"):
        st.code("df['ColumnName'].value_counts()", language="python")
        st.write("**العربية:** يعد كم مرة ظهرت كل قيمة في العمود")
        st.write("**English:** Counts how many times each value appears in the column")
        col_val = st.selectbox("اختر عمود | Select column:", df.columns, key="value_counts")
        try:
            st.write(df[col_val].value_counts().head(20))
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    # ----------------------------
    # 🧮 SECTION 5: ADVANCED OPERATIONS
    # القسم 5: العمليات المتقدمة
    # ----------------------------
    st.markdown("---")
    st.header("🧮 القسم 5: العمليات المتقدمة | Section 5: Advanced Operations")
    st.write("**العربية:** وظائف متقدمة للتحليل الاحترافي")
    st.write("**English:** Advanced functions for professional analysis")

    with st.expander("2️⃣2️⃣ df.apply() — تطبيق دالة مخصصة | Apply custom function"):
        st.code("df['Goals'].apply(lambda x: x * 2)", language="python")
        st.write("**العربية:** يطبق دالة مخصصة على عمود معين")
        st.write("**English:** Applies a custom function to a column")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            apply_col = st.selectbox("اختر عمود | Select column:", numeric_cols, key="apply_col")
            if st.button("ضرب القيم × 2 | Multiply values × 2"):
                try:
                    df_copy = df.copy()
                    df_copy[f"{apply_col}_x2"] = df_copy[apply_col].apply(lambda x: x * 2)
                    st.dataframe(safe_head(df_copy[[apply_col, f"{apply_col}_x2"]], 10))
                    st.success("✅ تم التطبيق | Applied successfully")
                except Exception as e:
                    st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    with st.expander("2️⃣3️⃣ pd.merge() — دمج مجموعتي بيانات | Merge two datasets"):
        st.code("pd.merge(df1, df2, on='ID')", language="python")
        st.write("**العربية:** يدمج مجموعتي بيانات بناءً على عمود مشترك")
        st.write("**English:** Merges two datasets based on a common column")
        uploaded_file2 = st.file_uploader("ارفع ملف CSV ثاني (اختياري) | Upload 2nd CSV (optional):", type=["csv"], key="merge2")
        if uploaded_file2:
            try:
                df2 = pd.read_csv(uploaded_file2)
                common = list(set(df.columns).intersection(df2.columns))
                st.write(f"الأعمدة المشتركة | Common columns: {common}")
                if common:
                    merge_on = st.selectbox("عمود الدمج | Merge key:", common, key="merge_on")
                    how = st.selectbox("نوع الدمج | Merge type:", ["inner", "left", "right", "outer"], key="merge_how")
                    merged = pd.merge(df, df2, on=merge_on, how=how)
                    st.write(f"عدد الصفوف بعد الدمج | Rows after merge: {len(merged)}")
                    st.dataframe(safe_head(merged, 10))
                else:
                    st.write("لا توجد أعمدة مشتركة | No common columns")
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣4️⃣ pd.concat() — تكديس البيانات | Stack datasets"):
        st.code("pd.concat([df1, df2])", language="python")
        st.write("**العربية:** يكدس مجموعات البيانات رأسياً أو أفقياً")
        st.write("**English:** Stacks datasets vertically or horizontally")
        uploaded_file3 = st.file_uploader("ارفع ملف للتكديس (اختياري) | Upload CSV to concat (optional):", type=["csv"], key="concat2")
        if uploaded_file3:
            try:
                df3 = pd.read_csv(uploaded_file3)
                axis = st.radio("المحور | Axis:", (0, 1), format_func=lambda x: "عمودي (0) | Vertical" if x == 0 else "أفقي (1) | Horizontal", key="concat_axis")
                conc = pd.concat([df, df3], axis=axis, ignore_index=(axis==0))
                st.dataframe(safe_head(conc, 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣5️⃣ df.pivot_table() — جدول محوري | Pivot table"):
        st.code("pd.pivot_table(df, values='Goals', index='Club', aggfunc='mean')", language="python")
        st.write("**العربية:** ينشئ جدول ملخص بتجميع وإحصائيات")
        st.write("**English:** Creates a summary table with grouping and statistics")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            val = st.selectbox("القيم (رقمية) | Values (numeric):", numeric_cols, key="pivot_val")
            idx = st.selectbox("الفهرس | Index:", df.columns.tolist(), key="pivot_idx")
            agg = st.selectbox("الدالة | Function:", ["mean", "sum", "count", "median"], key="pivot_agg")
            try:
                pt = pd.pivot_table(df, values=val, index=idx, aggfunc=agg)
                st.dataframe(safe_head(pt, 20))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    # ----------------------------
    # 📊 SECTION 6: STATISTICAL ANALYSIS
    # القسم 6: التحليل الإحصائي
    # ----------------------------
    st.markdown("---")
    st.header("📊 القسم 6: التحليل الإحصائي | Section 6: Statistical Analysis")
    st.write("**العربية:** تحليل إحصائي وارتباطات")
    st.write("**English:** Statistical analysis and correlations")

    with st.expander("2️⃣6️⃣ df.corr() — مصفوفة الارتباط | Correlation matrix"):
        st.code("df.corr()", language="python")
        st.write("**العربية:** يحسب الارتباط بين الأعمدة الرقمية")
        st.write("**English:** Calculates correlation between numeric columns")
        try:
            corr = df.corr(numeric_only=True)
            st.dataframe(corr)
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣7️⃣ df.cov() — مصفوفة التغاير | Covariance matrix"):
        st.code("df.cov()", language="python")
        st.write("**العربية:** يحسب التغاير بين الأعمدة الرقمية")
        st.write("**English:** Calculates covariance between numeric columns")
        try:
            cov = df.cov(numeric_only=True)
            st.dataframe(cov)
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    with st.expander("2️⃣8️⃣ pd.crosstab() — جدول تقاطعي | Cross-tabulation"):
        st.code("pd.crosstab(df['Gender'], df['Dept'])", language="python")
        st.write("**العربية:** ينشئ جدول تقاطعي بين متغيرين")
        st.write("**English:** Creates a cross-tabulation between two variables")
        if len(df.columns) >= 2:
            col_a = st.selectbox("الصفوف | Rows:", df.columns, key="ct_a")
            col_b = st.selectbox("الأعمدة | Columns:", df.columns, key="ct_b")
            try:
                ct = pd.crosstab(df[col_a], df[col_b], margins=True)
                st.dataframe(ct)
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    # ----------------------------
    # 🔄 SECTION 7: DATA TRANSFORMATION
    # القسم 7: تحويل البيانات
    # ----------------------------
    st.markdown("---")
    st.header("🔄 القسم 7: تحويل البيانات | Section 7: Data Transformation")
    st.write("**العربية:** تحويل وإعادة تشكيل البيانات")
    st.write("**English:** Transform and reshape data")

    with st.expander("2️⃣9️⃣ df.rolling() — النوافذ المتحركة | Rolling windows"):
        st.code("df['Value'].rolling(window=3).mean()", language="python")
        st.write("**العربية:** يحسب المتوسط المتحرك أو إحصائيات على نافذة متحركة")
        st.write("**English:** Calculates moving average or statistics over a rolling window")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            win_col = st.selectbox("اختر عمود | Select column:", numeric_cols, key="rolling_col")
            window = st.number_input("حجم النافذة | Window size:", min_value=1, max_value=100, value=3, key="rolling_window")
            try:
                df_copy = df.copy()
                df_copy[f"{win_col}_rolling"] = df_copy[win_col].rolling(window=int(window)).mean()
                st.dataframe(safe_head(df_copy[[win_col, f"{win_col}_rolling"]], 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    with st.expander("3️⃣0️⃣ df.ewm() — المتوسط المتحرك الأسي | Exponential moving average"):
        st.code("df['Value'].ewm(span=5).mean()", language="python")
        st.write("**العربية:** يحسب المتوسط المتحرك الأسي (يعطي وزن أكبر للقيم الحديثة)")
        st.write("**English:** Calculates exponential moving average (gives more weight to recent values)")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            ewm_col = st.selectbox("اختر عمود | Select column:", numeric_cols, key="ewm_col")
            span = st.number_input("المدى | Span:", min_value=1, max_value=100, value=5, key="ewm_span")
            try:
                df_copy = df.copy()
                df_copy[f"{ewm_col}_ewm"] = df_copy[ewm_col].ewm(span=int(span), adjust=False).mean()
                st.dataframe(safe_head(df_copy[[ewm_col, f"{ewm_col}_ewm"]], 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    # ----------------------------
    # ✍️ SECTION 8: STRING OPERATIONS
    # القسم 8: عمليات النصوص
    # ----------------------------
    st.markdown("---")
    st.header("✍️ القسم 8: عمليات النصوص | Section 8: String Operations")
    st.write("**العربية:** معالجة وتحويل النصوص")
    st.write("**English:** Text processing and transformation")

    with st.expander("3️⃣1️⃣ str.lower() & str.upper() — تحويل الأحرف | Case conversion"):
        st.code("df['Name'].str.lower()\ndf['Name'].str.upper()", language="python")
        st.write("**العربية:** يحول النص إلى أحرف صغيرة أو كبيرة")
        st.write("**English:** Converts text to lowercase or uppercase")
        text_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c])]
        if text_cols:
            text_col = st.selectbox("اختر عمود نصي | Select text column:", text_cols, key="text_col")
            op = st.selectbox("العملية | Operation:", ["lower", "upper", "title", "strip"], key="text_op")
            if op == "lower":
                st.dataframe(safe_head(df[text_col].str.lower(), 10))
            elif op == "upper":
                st.dataframe(safe_head(df[text_col].str.upper(), 10))
            elif op == "title":
                st.dataframe(safe_head(df[text_col].str.title(), 10))
            elif op == "strip":
                st.dataframe(safe_head(df[text_col].str.strip(), 10))
        else:
            st.write("لا توجد أعمدة نصية | No text columns")

    with st.expander("3️⃣2️⃣ str.contains() — البحث في النصوص | Search in text"):
        st.code("df['Name'].str.contains('Ahmed')", language="python")
        st.write("**العربية:** يبحث عن نص معين داخل العمود")
        st.write("**English:** Searches for specific text within the column")
        text_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c])]
        if text_cols:
            text_col = st.selectbox("اختر عمود | Select column:", text_cols, key="contains_col")
            pattern = st.text_input("النص للبحث | Text to search:", "", key="contains_pat")
            if pattern:
                try:
                    result = df[text_col].str.contains(pattern, na=False)
                    st.write(f"عدد الصفوف المطابقة | Matching rows: {result.sum()}")
                    st.dataframe(safe_head(df[result], 10))
                except Exception as e:
                    st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة نصية | No text columns")

    with st.expander("3️⃣3️⃣ str.split() — تقسيم النصوص | Split text"):
        st.code("df['Name'].str.split(' ')", language="python")
        st.write("**العربية:** يقسم النص إلى أجزاء بناءً على فاصل")
        st.write("**English:** Splits text into parts based on a separator")
        text_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c])]
        if text_cols:
            text_col = st.selectbox("اختر عمود | Select column:", text_cols, key="split_col")
            sep = st.text_input("الفاصل | Separator:", " ", key="split_sep")
            try:
                st.dataframe(safe_head(df[text_col].str.split(sep).astype(str), 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة نصية | No text columns")

    # ----------------------------
    # 🕓 SECTION 9: TIME SERIES
    # القسم 9: السلاسل الزمنية
    # ----------------------------
    st.markdown("---")
    st.header("🕓 القسم 9: السلاسل الزمنية | Section 9: Time Series")
    st.write("**العربية:** العمل مع البيانات الزمنية")
    st.write("**English:** Working with time-based data")

    with st.expander("3️⃣4️⃣ pd.to_datetime() — تحويل إلى تاريخ | Convert to datetime"):
        st.code("pd.to_datetime(df['Date'])", language="python")
        st.write("**العربية:** يحول النص إلى صيغة تاريخ ووقت")
        st.write("**English:** Converts text to datetime format")
        date_col = st.selectbox("اختر عمود للتحويل | Select column to convert:", ["<none>"] + df.columns.tolist(), key="date_col")
        if date_col != "<none>":
            try:
                df_copy = df.copy()
                df_copy[date_col] = pd.to_datetime(df_copy[date_col], errors='coerce')
                st.dataframe(safe_head(df_copy[[date_col]], 10))
                st.success("✅ تم التحويل | Converted successfully")
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("3️⃣5️⃣ df.resample() — إعادة العينة الزمنية | Time resampling"):
        st.code("df.resample('M').mean()", language="python")
        st.write("**العربية:** يعيد تجميع البيانات الزمنية (شهرياً، أسبوعياً، إلخ)")
        st.write("**English:** Regroups time-based data (monthly, weekly, etc.)")
        st.write("💡 يتطلب فهرس زمني | Requires datetime index")

    # ----------------------------
    # ⚙️ SECTION 10: INDEX OPERATIONS
    # القسم 10: عمليات الفهرس
    # ----------------------------
    st.markdown("---")
    st.header("⚙️ القسم 10: عمليات الفهرس | Section 10: Index Operations")
    st.write("**العربية:** التحكم في فهرس البيانات")
    st.write("**English:** Control data index")

    with st.expander("3️⃣6️⃣ df.set_index() — تعيين الفهرس | Set index"):
        st.code("df.set_index('ID')", language="python")
        st.write("**العربية:** يجعل عمود معين هو فهرس البيانات")
        st.write("**English:** Makes a specific column the data index")
        index_col = st.selectbox("اختر عمود للفهرس | Select index column:", ["<none>"] + df.columns.tolist(), key="set_index")
        if index_col != "<none>":
            try:
                df_indexed = df.set_index(index_col)
                st.dataframe(safe_head(df_indexed, 5))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("3️⃣7️⃣ df.reset_index() — إعادة تعيين الفهرس | Reset index"):
        st.code("df.reset_index()", language="python")
        st.write("**العربية:** يعيد الفهرس إلى الأرقام الافتراضية")
        st.write("**English:** Resets index to default numbers")
        st.dataframe(safe_head(df.reset_index(drop=True), 5))

    # ----------------------------
    # 🔁 SECTION 11: CONDITIONAL OPERATIONS
    # القسم 11: العمليات الشرطية
    # ----------------------------
    st.markdown("---")
    st.header("🔁 القسم 11: العمليات الشرطية | Section 11: Conditional Operations")
    st.write("**العربية:** إنشاء أعمدة بناءً على شروط")
    st.write("**English:** Create columns based on conditions")

    with st.expander("3️⃣8️⃣ np.where() — الشرط الثنائي | Binary condition"):
        st.code("np.where(df['Age'] > 18, 'Adult', 'Minor')", language="python")
        st.write("**العربية:** ينشئ قيم بناءً على شرط (إذا/وإلا)")
        st.write("**English:** Creates values based on condition (if/else)")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            cond_col = st.selectbox("اختر عمود | Select column:", numeric_cols, key="cond_col")
            threshold = st.number_input("القيمة الحدية | Threshold:", value=0.0, key="cond_val")
            new_col = st.text_input("اسم العمود الجديد | New column name:", f"{cond_col}_flag", key="cond_newname")
            if st.button("إنشاء العمود | Create column"):
                try:
                    df_copy = df.copy()
                    df_copy[new_col] = np.where(df_copy[cond_col] > threshold, "نعم | Yes", "لا | No")
                    st.dataframe(safe_head(df_copy[[cond_col, new_col]], 10))
                except Exception as e:
                    st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    # ----------------------------
    # 🧩 SECTION 12: MULTIINDEX
    # القسم 12: الفهرس الهرمي
    # ----------------------------
    st.markdown("---")
    st.header("🧩 القسم 12: الفهرس الهرمي | Section 12: MultiIndex")
    st.write("**العربية:** العمل مع فهرس متعدد المستويات")
    st.write("**English:** Working with hierarchical index")

    with st.expander("3️⃣9️⃣ MultiIndex — الفهرس متعدد المستويات | Hierarchical indexing"):
        st.code("df.set_index(['Region', 'Year'])", language="python")
        st.write("**العربية:** ينشئ فهرس بمستويين أو أكثر")
        st.write("**English:** Creates an index with two or more levels")
        if len(df.columns) >= 2:
            mi_cols = st.multiselect("اختر عمودين | Choose 2 columns:", df.columns, max_selections=2, key="mi_cols")
            if len(mi_cols) == 2:
                try:
                    df_mi = df.set_index(mi_cols)
                    st.dataframe(safe_head(df_mi, 10))
                except Exception as e:
                    st.error(f"خطأ | Error: {e}")
        else:
            st.write("غير كافي | Not enough columns")

    # ----------------------------
    # 📈 SECTION 13: VISUALIZATION
    # القسم 13: الرسوم البيانية
    # ----------------------------
    st.markdown("---")
    st.header("📈 القسم 13: الرسوم البيانية | Section 13: Visualization")
    st.write("**العربية:** تصور البيانات برسوم بيانية")
    st.write("**English:** Visualize data with charts")

    with st.expander("4️⃣0️⃣ رسم الهستوغرام | Histogram plot"):
        st.code("df['Column'].hist()", language="python")
        st.write("**العربية:** يرسم توزيع القيم في عمود")
        st.write("**English:** Plots the distribution of values in a column")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            viz_col = st.selectbox("اختر عمود للرسم | Select column to plot:", numeric_cols, key="viz_col")
            if st.button("إظهار الرسم | Show plot"):
                try:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    df[viz_col].dropna().hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
                    ax.set_title(f"توزيع | Distribution: {viz_col}", fontsize=14, fontweight='bold')
                    ax.set_xlabel(viz_col, fontsize=12)
                    ax.set_ylabel("التكرار | Frequency", fontsize=12)
                    ax.grid(alpha=0.3)
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"خطأ | Error: {e}")
        else:
            st.write("لا توجد أعمدة رقمية | No numeric columns")

    # ----------------------------
    # 🧰 SECTION 14: PERFORMANCE
    # القسم 14: الأداء والتحسين
    # ----------------------------
    st.markdown("---")
    st.header("🧰 القسم 14: الأداء والتحسين | Section 14: Performance & Optimization")
    st.write("**العربية:** تحسين استهلاك الذاكرة والسرعة")
    st.write("**English:** Optimize memory usage and speed")

    with st.expander("4️⃣1️⃣ df.memory_usage() — استهلاك الذاكرة | Memory usage"):
        st.code("df.memory_usage(deep=True)", language="python")
        st.write("**العربية:** يعرض استهلاك الذاكرة لكل عمود")
        st.write("**English:** Shows memory usage for each column")
        try:
            mem = df.memory_usage(deep=True)
            mem_mb = mem / 1024 / 1024
            st.write(mem_mb)
            st.write(f"الاستهلاك الكلي | Total: {mem_mb.sum():.2f} MB")
        except Exception as e:
            st.error(f"خطأ | Error: {e}")

    with st.expander("4️⃣2️⃣ astype('category') — تحسين نوع البيانات | Optimize data type"):
        st.code("df['Gender'].astype('category')", language="python")
        st.write("**العربية:** يحول الأعمدة النصية المتكررة إلى نوع category لتوفير الذاكرة")
        st.write("**English:** Converts repetitive text columns to category type to save memory")
        if st.button("تطبيق التحسين | Apply optimization"):
            try:
                df_opt = df.copy()
                for c in df_opt.columns:
                    if df_opt[c].dtype == object and df_opt[c].nunique() < len(df_opt) * 0.5:
                        df_opt[c] = df_opt[c].astype('category')
                st.write("أنواع البيانات بعد التحسين | Data types after optimization:")
                st.write(df_opt.dtypes)
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    # ----------------------------
    # 💾 SECTION 15: EXPORT DATA
    # القسم 15: تصدير البيانات
    # ----------------------------
    st.markdown("---")
    st.header("💾 القسم 15: تصدير البيانات | Section 15: Export Data")
    st.write("**العربية:** احفظ بياناتك بصيغ مختلفة")
    st.write("**English:** Save your data in different formats")

    with st.expander("4️⃣3️⃣ تصدير إلى CSV | Export to CSV"):
        st.code("df.to_csv('output.csv', index=False)", language="python")
        st.write("**العربية:** يحفظ البيانات كملف CSV")
        st.write("**English:** Saves data as CSV file")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ تحميل CSV | Download CSV",
            data=csv,
            file_name="data_export.csv",
            mime="text/csv"
        )

    with st.expander("4️⃣4️⃣ تصدير إلى Excel | Export to Excel"):
        st.code("df.to_excel('output.xlsx', index=False)", language="python")
        st.write("**العربية:** يحفظ البيانات كملف Excel")
        st.write("**English:** Saves data as Excel file")
        xlsx_bytes = df_to_excel_bytes(df)
        st.download_button(
            label="⬇️ تحميل Excel | Download Excel",
            data=xlsx_bytes,
            file_name="data_export.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    with st.expander("4️⃣5️⃣ تصدير إلى JSON | Export to JSON"):
        st.code("df.to_json('output.json')", language="python")
        st.write("**العربية:** يحفظ البيانات كملف JSON")
        st.write("**English:** Saves data as JSON file")
        json_str = df.to_json(orient='records', force_ascii=False, indent=2)
        st.download_button(
            label="⬇️ تحميل JSON | Download JSON",
            data=json_str,
            file_name="data_export.json",
            mime="application/json"
        )

    # ----------------------------
    # ⚡ SECTION 16: EXPERT TIPS
    # القسم 16: نصائح الخبراء
    # ----------------------------
    st.markdown("---")
    st.header("⚡ القسم 16: نصائح الخبراء | Section 16: Expert Tips")
    st.write("**العربية:** تقنيات متقدمة للمحترفين")
    st.write("**English:** Advanced techniques for professionals")

    with st.expander("4️⃣6️⃣ قراءة الملفات الكبيرة | Reading large files"):
        st.code("pd.read_csv('big.csv', chunksize=10000)", language="python")
        st.write("**العربية:** استخدم chunksize لقراءة الملفات الكبيرة تدريجياً")
        st.write("**English:** Use chunksize to read large files incrementally")

    with st.expander("4️⃣7️⃣ pd.get_dummies() — الترميز الثنائي | One-hot encoding"):
        st.code("pd.get_dummies(df, columns=['Gender'])", language="python")
        st.write("**العربية:** يحول الأعمدة الفئوية إلى أعمدة ثنائية (0 و 1)")
        st.write("**English:** Converts categorical columns to binary columns (0 and 1)")
        cat_cols = [c for c in df.columns if df[c].nunique() < 10 and pd.api.types.is_object_dtype(df[c])]
        if cat_cols and st.button("تطبيق الترميز | Apply encoding"):
            try:
                df_encoded = pd.get_dummies(df, columns=cat_cols[:1])
                st.dataframe(safe_head(df_encoded, 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("4️⃣8️⃣ اكتشاف القيم الشاذة | Outlier detection"):
        st.code("q1 = df['Value'].quantile(0.25)\nq3 = df['Value'].quantile(0.75)\niqr = q3 - q1", language="python")
        st.write("**العربية:** استخدم طريقة IQR لاكتشاف القيم الشاذة")
        st.write("**English:** Use IQR method to detect outliers")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            outlier_col = st.selectbox("اختر عمود | Select column:", numeric_cols, key="outlier_col")
            try:
                q1 = df[outlier_col].quantile(0.25)
                q3 = df[outlier_col].quantile(0.75)
                iqr = q3 - q1
                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr
                outliers = df[(df[outlier_col] < lower) | (df[outlier_col] > upper)]
                st.write(f"عدد القيم الشاذة | Outliers count: {len(outliers)}")
                if len(outliers) > 0:
                    st.dataframe(safe_head(outliers, 10))
            except Exception as e:
                st.error(f"خطأ | Error: {e}")

    with st.expander("4️⃣9️⃣ df.sample() — اختيار عشوائي | Random sampling"):
        st.code("df.sample(n=10)", language="python")
        st.write("**العربية:** يختار صفوف عشوائية من البيانات")
        st.write("**English:** Selects random rows from the data")
        n_samples = st.number_input("عدد الصفوف | Number of rows:", min_value=1, max_value=len(df), value=min(10, len(df)), key="sample_n")
        if st.button("اختيار عشوائي | Random sample"):
            st.dataframe(df.sample(n=int(n_samples)))

    with st.expander("5️⃣0️⃣ df.pipe() — ربط العمليات | Chain operations"):
        st.code("df.pipe(lambda x: x.dropna()).pipe(lambda x: x.fillna(0))", language="python")
        st.write("**العربية:** يسمح بربط عمليات متعددة بشكل متسلسل")
        st.write("**English:** Allows chaining multiple operations sequentially")
        st.write("💡 مفيد لكتابة كود نظيف ومنظم | Useful for writing clean, organized code")

    # ----------------------------
    # 🎓 FINAL FOOTER
    # الختام
    # ----------------------------
    st.markdown("---")
    st.markdown("## 🎉 تهانينا! لقد أكملت جميع وظائف Pandas")
    st.markdown("## 🎉 Congratulations! You've completed all Pandas functions")
    st.markdown("---")
    st.markdown("**تم التطوير بواسطة الأستاذة: حجار نايلة**")
    st.markdown("**Developed by Teacher: Hadjar Nayla**")
    st.markdown("*تمكين الطلاب بمهارات تحليل البيانات العملية*")
    st.markdown("*Empowering students with practical data analysis skills*")
    
    # Quick reference
    st.markdown("---")
    with st.expander("📚 مرجع سريع | Quick Reference"):
        st.markdown("""
        ### الوظائف الأساسية | Basic Functions
        - `df.head()` - أول 5 صفوف | First 5 rows
        - `df.tail()` - آخر 5 صفوف | Last 5 rows
        - `df.shape` - الأبعاد | Dimensions
        - `df.info()` - معلومات البيانات | Data info
        - `df.describe()` - إحصائيات | Statistics
        
        ### التنظيف | Cleaning
        - `df.dropna()` - حذف القيم المفقودة | Drop missing
        - `df.fillna()` - ملء القيم المفقودة | Fill missing
        - `df.drop_duplicates()` - حذف التكرارات | Remove duplicates
        
        ### الاختيار | Selection
        - `df['col']` - اختيار عمود | Select column
        - `df[['col1', 'col2']]` - أعمدة متعددة | Multiple columns
        - `df[df['col'] > 10]` - التصفية | Filtering
        
        ### التحليل | Analysis
        - `df.groupby()` - التجميع | Grouping
        - `df.sort_values()` - الترتيب | Sorting
        - `df.corr()` - الارتباط | Correlation
        
        ### التصدير | Export
        - `df.to_csv()` - حفظ CSV | Save CSV
        - `df.to_excel()` - حفظ Excel | Save Excel
        - `df.to_json()` - حفظ JSON | Save JSON
        """)

else:
    # Welcome screen when no file is uploaded
    st.info("👆 يرجى تحميل ملف CSV لبدء التعلم | Please upload a CSV file to start learning")
    
    st.markdown("---")
    st.markdown("## 📚 ماذا ستتعلم؟ | What will you learn?")
    st.markdown("## 🌟 ستتعلم 50 وظيفة في Pandas مقسمة على 16 قسم")
    st.markdown("## 🌟 You will learn 50 Pandas functions across 16 sections")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### الأقسام بالعربية:
        1. 📘 الوظائف الأساسية
        2. 🧹 تنظيف البيانات
        3. 🔍 التصفية والاختيار
        4. 📈 الترتيب والتجميع
        5. 🧮 العمليات المتقدمة
        6. 📊 التحليل الإحصائي
        7. 🔄 تحويل البيانات
        8. ✍️ عمليات النصوص
        9. 🕓 السلاسل الزمنية
        10. ⚙️ عمليات الفهرس
        11. 🔁 العمليات الشرطية
        12. 🧩 الفهرس الهرمي
        13. 📈 الرسوم البيانية
        14. 🧰 الأداء والتحسين
        15. 💾 تصدير البيانات
        16. ⚡ نصائح الخبراء
        """)
