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
st.title("🐼 Learn All Pandas Functions — From 0 to Hero")
st.write("This app teaches **Pandas** step by step using your dataset. Upload a CSV file and explore every important function interactively!")
st.write("هذا التطبيق يعلم **Pandas** خطوة بخطوة باستخدام بياناتك. قم بتحميل ملف CSV واستكشف كل وظيفة مهمة بشكل تفاعلي!")
st.markdown("### 🎓 **Futuro School** | Created by Teacher **Hadjar Nayla**")
st.markdown("---")

# ----------------------------
# 📂 UPLOAD DATASET
# ----------------------------
st.header("📁 Step 1: Upload a CSV file | الخطوة الأولى: تحميل ملف CSV")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# helper: safe head for large dfs
def safe_head(df, n=5):
    try:
        return df.head(n)
    except Exception:
        return df.iloc[:n, :]

def df_to_excel_bytes(df):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
        writer.save()
    return buffer.getvalue()

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception:
        # try with different encodings or separators
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='utf-8', sep=None, engine='python')
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            st.stop()

    st.success("✅ Dataset loaded successfully! | تم تحميل مجموعة البيانات بنجاح!")
    st.dataframe(safe_head(df, 5))

    # ----------------------------
    # 📘 BASIC FUNCTIONS
    # ----------------------------
    st.header("📘 Basic Pandas Functions | الوظائف الأساسية")

    with st.expander("🔹 df.head() — View first rows | عرض الصفوف الأولى"):
        st.code("df.head()", language="python")
        st.write(safe_head(df, 5))
        st.write("Shows the first 5 rows of the DataFrame. | يعرض أول 5 صفوف من إطار البيانات.")

    with st.expander("🔹 df.tail() — View last rows | عرض الصفوف الأخيرة"):
        st.code("df.tail()", language="python")
        st.write(df.tail(5))
        st.write("Shows the last 5 rows of the DataFrame. | يعرض آخر 5 صفوف من إطار البيانات.")

    with st.expander("🔹 df.shape — Get rows and columns count | الحصول على عدد الصفوف والأعمدة"):
        st.code("df.shape", language="python")
        st.write(df.shape)
        st.write("Returns (rows, columns). | يعيد (الصفوف، الأعمدة).")

    with st.expander("🔹 df.columns — List all columns | قائمة بجميع الأعمدة"):
        st.code("df.columns", language="python")
        st.write(df.columns.tolist())
        st.write("Displays the names of all columns in your dataset. | يعرض أسماء جميع الأعمدة في مجموعة البيانات الخاصة بك.")

    with st.expander("🔹 df.info() — Show data types and non-null counts | عرض أنواع البيانات وعدد القيم غير الفارغة"):
        st.code("df.info()", language="python")
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.text(info_str)
        st.write("Summary about columns, dtypes, and missing values. | ملخص عن الأعمدة وأنواع البيانات والقيم المفقودة.")

    with st.expander("🔹 df.describe() — Statistical summary | ملخص إحصائي"):
        st.code("df.describe()", language="python")
        st.write(df.describe(include='all').astype(str).head(20))
        st.write("Stats for numeric and object columns. | إحصائيات للأعمدة الرقمية والنصية.")

    with st.expander("🔹 df.dtypes — Data types of each column | أنواع البيانات لكل عمود"):
        st.code("df.dtypes", language="python")
        st.write(df.dtypes)
        st.write("Lists the data type of each column. | يسرد نوع البيانات لكل عمود.")

    with st.expander("🔹 df.index — Index information | معلومات الفهرس"):
        st.code("df.index", language="python")
        st.write(df.index)
        st.write("Gives the index (row labels). | يعطي الفهرس (تسميات الصفوف).")

    with st.expander("🔹 df.isnull() — Detect missing values | كشف القيم المفقودة"):
        st.code("df.isnull().sum()", language="python")
        st.write(df.isnull().sum())
        st.write("Shows count of missing values per column. | يعرض عدد القيم المفقودة في كل عمود.")

    # ----------------------------
    # 🧹 DATA CLEANING
    # ----------------------------
    st.header("🧹 Data Cleaning Functions | وظائف تنظيف البيانات")

    with st.expander("🔹 df.dropna() — Remove missing rows | إزالة الصفوف المفقودة"):
        st.code("df.dropna()", language="python")
        st.write(safe_head(df.dropna(), 5))
        st.write("Removes rows with any missing values. | يزيل الصفوف التي تحتوي على قيم مفقودة.")

    with st.expander("🔹 df.fillna() — Replace missing values | استبدال القيم المفقودة"):
        st.code("df.fillna(value)", language="python")
        fill_value = st.text_input("Fill missing values with (e.g., 0 or 'unknown'):", "0")
        try:
            # try numeric
            fv = float(fill_value)
        except Exception:
            fv = fill_value
        st.write(safe_head(df.fillna(fv), 5))
        st.write("Replaces missing values with given value. | يستبدل القيم المفقودة بالقيمة المعطاة.")

    with st.expander("🔹 df.rename() — Rename columns | إعادة تسمية الأعمدة"):
        st.code("df.rename(columns={'OldName':'NewName'})", language="python")
        col_old = st.selectbox("Select column to rename:", df.columns, key="rename_old")
        col_new = st.text_input("New name:", f"{col_old}_renamed", key="rename_new")
        if st.button("Rename column"):
            df = df.rename(columns={col_old: col_new})
            st.success(f"Renamed {col_old} -> {col_new}")
            st.write(df.columns.tolist())

    with st.expander("🔹 df.drop() — Remove columns or rows | إزالة الأعمدة أو الصفوف"):
        st.code("df.drop('ColumnName', axis=1)", language="python")
        to_drop = st.multiselect("Select columns to drop (preview only):", df.columns)
        if to_drop:
            st.write(safe_head(df.drop(columns=to_drop), 5))
        else:
            st.write("No column selected.")

    with st.expander("🔹 df.duplicated() & df.drop_duplicates() — Remove duplicates | إزالة التكرارات"):
        st.code("df.drop_duplicates()", language="python")
        st.write("Number of duplicate rows:", int(df.duplicated().sum()))
        st.write(safe_head(df.drop_duplicates(), 5))

    # ----------------------------
    # 🔍 FILTERING & SELECTION
    # ----------------------------
    st.header("🔍 Filtering and Selection | التصفية والاختيار")

    with st.expander("🔹 Select one column | اختيار عمود واحد"):
        st.code("df['ColumnName']", language="python")
        column = st.selectbox("Select a column to view:", df.columns, key="single_col")
        st.write(safe_head(df[[column]], 5))

    with st.expander("🔹 Select multiple columns | اختيار أعمدة متعددة"):
        st.code("df[['Col1', 'Col2']]", language="python")
        cols = st.multiselect("Choose columns:", df.columns, key="multi_cols")
        if cols:
            st.write(safe_head(df[cols], 5))
        else:
            st.write("No columns selected.")

    with st.expander("🔹 Filter rows with condition | تصفية الصفوف بشرط"):
        st.code("df[df['Goals'] > 10]", language="python")
        cond_col = st.selectbox("Column to filter by (must be numeric):", [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])], key="filter_col")
        op = st.selectbox("Operator:", [">", "<", ">=", "<=", "==", "!="], key="filter_op")
        value = st.text_input("Value to compare:", "0", key="filter_val")
        try:
            val = float(value)
            if op == ">":
                out = df[df[cond_col] > val]
            elif op == "<":
                out = df[df[cond_col] < val]
            elif op == ">=":
                out = df[df[cond_col] >= val]
            elif op == "<=":
                out = df[df[cond_col] <= val]
            elif op == "==":
                out = df[df[cond_col] == val]
            else:
                out = df[df[cond_col] != val]
            st.write(safe_head(out, 10))
            st.write(f"Filtered rows: {len(out)}")
        except Exception as e:
            st.write("Could not apply filter:", e)

    with st.expander("🔹 iloc and loc — Index selection | اختيار الفهرس"):
        st.code("df.iloc[0:5, 0:3]  # by index\ndf.loc[0:5, ['Name','Club']]", language="python")
        rstart = st.number_input("Row start (iloc):", min_value=0, max_value=max(0, len(df)-1), value=0, key="iloc_rs")
        rend = st.number_input("Row end (iloc):", min_value=0, max_value=max(0, len(df)), value=min(5, len(df)), key="iloc_re")
        cstart = st.number_input("Col start index (iloc):", min_value=0, max_value=max(0, len(df.columns)-1), value=0, key="iloc_cs")
        cend = st.number_input("Col end index (iloc):", min_value=0, max_value=max(0, len(df.columns)), value=min(3, len(df.columns)), key="iloc_ce")
        try:
            st.write(safe_head(df.iloc[rstart:rend, cstart:cend], 10))
        except Exception as e:
            st.write("iloc selection failed:", e)
        st.write("You can also use df.loc with labels if your index is labeled.")

    # ----------------------------
    # 📈 SORTING & GROUPING
    # ----------------------------
    st.header("📈 Sorting and Grouping | الترتيب والتجميع")

    with st.expander("🔹 Sort by column | الترتيب حسب العمود"):
        st.code("df.sort_values(by='Goals', ascending=False)", language="python")
        sort_col = st.selectbox("Select column to sort by:", df.columns, key="sort_col")
        asc = st.checkbox("Ascending?", value=False, key="sort_asc")
        try:
            st.write(safe_head(df.sort_values(by=sort_col, ascending=asc), 10))
        except Exception as e:
            st.write("Sort failed:", e)

    with st.expander("🔹 Group by and aggregate | التجميع والتجميع"):
        st.code("df.groupby('Club').mean()", language="python")
        col_group = st.selectbox("Select a column to group by:", df.columns, key="group_col")
        try:
            grouped = df.groupby(col_group).mean(numeric_only=True)
            st.write(safe_head(grouped, 10))
        except Exception as e:
            st.write("Grouping failed:", e)

    with st.expander("🔹 df.value_counts() — Count unique values | عد القيم الفريدة"):
        st.code("df['ColumnName'].value_counts()", language="python")
        col_val = st.selectbox("Select a column for value counts:", df.columns, key="value_counts_2")
        try:
            st.write(df[col_val].value_counts().head(50))
        except Exception as e:
            st.write("Value counts failed:", e)

    # ----------------------------
    # 🧮 ADVANCED FUNCTIONS
    # ----------------------------
    st.header("🧮 Advanced Pandas Functions | الوظائف المتقدمة")

    with st.expander("🔹 df.apply() — Apply custom functions | تطبيق وظائف مخصصة"):
        st.code("df['Goals'].apply(lambda x: x * 2)", language="python")
        apply_col = st.selectbox("Column to apply function to (numeric):", [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])], key="apply_col")
        if st.button("Apply x2 to selected column"):
            try:
                df[f"{apply_col}_x2"] = df[apply_col].apply(lambda x: x * 2)
                st.write(safe_head(df[[apply_col, f"{apply_col}_x2"]], 10))
                st.success("Applied function and added new column.")
            except Exception as e:
                st.error(f"Apply failed: {e}")

    with st.expander("🔹 df.merge() — Combine two datasets | دمج مجموعتي بيانات"):
        st.code("pd.merge(df1, df2, on='ID')", language="python")
        st.write("To demo merge upload a second CSV (optional). | لتحويل الدمج حمّل ملف CSV ثانٍ (اختياري).")
        uploaded_file2 = st.file_uploader("Upload second CSV to merge (optional)", type=["csv"], key="merge2")
        if uploaded_file2:
            try:
                df2 = pd.read_csv(uploaded_file2)
                common = list(set(df.columns).intersection(df2.columns))
                st.write("Common columns:", common)
                if common:
                    merge_on = st.selectbox("Select merge key:", common, key="merge_on")
                    how = st.selectbox("How to merge:", ["inner", "left", "right", "outer"], key="merge_how")
                    merged = pd.merge(df, df2, on=merge_on, how=how)
                    st.write("Merged result preview:")
                    st.write(safe_head(merged, 10))
                else:
                    st.write("No common columns to merge on.")
            except Exception as e:
                st.write("Failed to read/merge second file:", e)

    with st.expander("🔹 df.concat() — Stack datasets together | تكديس مجموعات البيانات معًا"):
        st.code("pd.concat([df1, df2])", language="python")
        st.write("Concatenate vertically or horizontally by uploading another file (optional).")
        uploaded_file3 = st.file_uploader("Upload CSV to concat (optional)", type=["csv"], key="concat2")
        if uploaded_file3:
            try:
                df3 = pd.read_csv(uploaded_file3)
                axis = st.radio("Axis:", (0, 1), key="concat_axis")
                conc = pd.concat([df, df3], axis=axis, ignore_index=(axis==0))
                st.write(safe_head(conc, 10))
            except Exception as e:
                st.write("Concat failed:", e)

    with st.expander("🔹 df.pivot_table() — Create summary tables | إنشاء جداول ملخصة"):
        st.code("pd.pivot_table(df, values='Goals', index='Club', aggfunc='mean')", language="python")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            val = st.selectbox("Values (numeric):", numeric_cols, key="pivot_val")
            idx = st.selectbox("Index (categorical):", df.columns.tolist(), key="pivot_idx")
            agg = st.selectbox("Aggfunc:", ["mean", "sum", "count", "median"], key="pivot_agg")
            try:
                pt = pd.pivot_table(df, values=val, index=idx, aggfunc=agg)
                st.write(safe_head(pt, 20))
            except Exception as e:
                st.write("Pivot failed:", e)
        else:
            st.write("No numeric columns available for pivot_table.")

    # ----------------------------
    # 💾 SAVE RESULTS
    # ----------------------------
    st.header("💾 Save and Export Data | حفظ وتصدير البيانات")

    with st.expander("🔹 Save to CSV | الحفظ كملف CSV"):
        st.code("df.to_csv('output.csv', index=False)", language="python")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download CSV", csv, "cleaned_data.csv", "text/csv")
        st.write("Exports DataFrame to CSV format. | يصدر إطار البيانات إلى تنسيق CSV.")

    with st.expander("🔹 Save to Excel | الحفظ كملف Excel"):
        st.code("df.to_excel('output.xlsx', index=False)", language="python")
        xlsx_bytes = df_to_excel_bytes(df)
        st.download_button("⬇️ Download Excel", xlsx_bytes, "cleaned_data.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        st.write("Exports DataFrame to Excel format. | يصدر إطار البيانات إلى تنسيق Excel.")

    # ----------------------------
    # ⚙️ INDEX OPERATIONS
    # ----------------------------
    st.header("⚙️ Index Operations | عمليات الفهرس")

    with st.expander("🔹 df.set_index() & df.reset_index()"):
        st.code("df.set_index('ID', inplace=True)\ndf.reset_index(inplace=True)", language="python")
        index_col = st.selectbox("Choose column to set as index (or None):", ["<none>"] + df.columns.tolist(), key="set_index")
        if index_col != "<none>":
            try:
                df_indexed = df.set_index(index_col)
                st.write("Indexed preview:")
                st.write(safe_head(df_indexed, 5))
            except Exception as e:
                st.write("Setting index failed:", e)
        else:
            st.write("No index change chosen.")

    with st.expander("🔹 df.reindex() — Reindex DataFrame"):
        st.code("df.reindex(range(0, 10))", language="python")
        st.write("This will reindex — preview of first rows only.")
        try:
            st.write(safe_head(df.reindex(range(0, min(10, len(df)))), 10))
        except Exception as e:
            st.write("Reindex failed:", e)

    # ----------------------------
    # 🔁 CONDITIONAL OPERATIONS
    # ----------------------------
    st.header("🔁 Conditional Operations | العمليات الشرطية")

    with st.expander("🔹 np.where & df.apply with condition"):
        st.code("df['Status'] = np.where(df['Age'] > 18, 'Adult', 'Minor')", language="python")
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            cond_col2 = st.selectbox("Choose numeric column for condition:", numeric_cols, key="cond_col2")
            val = st.number_input("Threshold value:", value=0.0, key="cond_val")
            new_col_name = st.text_input("New column name:", f"{cond_col2}_flag", key="cond_newname")
            if st.button("Create conditional column"):
                try:
                    df[new_col_name] = np.where(df[cond_col2] > val, "Yes", "No")
                    st.write(safe_head(df[[cond_col2, new_col_name]], 10))
                except Exception as e:
                    st.write("Conditional creation failed:", e)
        else:
            st.write("No numeric columns available.")

    # ----------------------------
    # 🧩 MULTIINDEX
    # ----------------------------
    st.header("🧩 MultiIndex (Hierarchical Indexing) | الفهرس الهرمي")

    with st.expander("🔹 Set MultiIndex & access"):
        st.code("df = df.set_index(['Region','Year'])", language="python")
        if len(df.columns) >= 2:
            mi_cols = st.multiselect("Choose 2 columns to set as MultiIndex (preview only):", df.columns, max_selections=2, key="mi_cols")
            if len(mi_cols) == 2:
                try:
                    df_mi = df.set_index(mi_cols)
                    st.write("MultiIndex preview:")
                    st.write(safe_head(df_mi, 10))
                except Exception as e:
                    st.write("MultiIndex failed:", e)
            else:
                st.write("Choose exactly 2 columns to demo MultiIndex.")
        else:
            st.write("Not enough columns for MultiIndex demo.")

    # ----------------------------
    # 🪜 ADVANCED GROUPBY
    # ----------------------------
    st.header("🪜 Advanced GroupBy Operations | تجميع متقدم")

    with st.expander("🔹 groupby with custom agg and filter"):
        st.code("grouped = df.groupby('Dept').agg({'Salary':['mean','max'],'Age':'median'})", language="python")
        group_cols = st.multiselect("Group by columns:", df.columns, key="adv_group_cols")
        if group_cols:
            try:
                agg_map = {}
                numeric = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
                for nc in numeric[:3]:
                    agg_map[nc] = ['mean', 'max', 'count']
                grouped = df.groupby(group_cols).agg(agg_map)
                st.write(safe_head(grouped, 20))
            except Exception as e:
                st.write("Advanced groupby failed:", e)
        else:
            st.write("Choose columns to group by to see example.")

    # ----------------------------
    # 📈 ROLLING & WINDOWS
    # ----------------------------
    st.header("📈 Rolling, Expanding, & EWM | دوال النوافذ")

    with st.expander("🔹 rolling & expanding"):
        st.code("df['rolling_mean'] = df['Value'].rolling(window=3).mean()", language="python")
        if numeric_cols:
            win_col = st.selectbox("Choose numeric column for rolling:", numeric_cols, key="rolling_col")
            window = st.number_input("Window size:", min_value=1, max_value=100, value=3, key="rolling_window")
            try:
                df[f"{win_col}_rolling_mean"] = df[win_col].rolling(window=window).mean()
                st.write(safe_head(df[[win_col, f"{win_col}_rolling_mean"]], 10))
            except Exception as e:
                st.write("Rolling failed:", e)
        else:
            st.write("No numeric columns for rolling demo.")

    with st.expander("🔹 ewm (exponential moving average)"):
        st.code("df['ewm_mean'] = df['Value'].ewm(alpha=0.5).mean()", language="python")
        if numeric_cols:
            ewm_col = st.selectbox("Choose column for EWM:", numeric_cols, key="ewm_col")
            span = st.number_input("Span (int):", min_value=1, max_value=100, value=5, key="ewm_span")
            try:
                df[f"{ewm_col}_ewm"] = df[ewm_col].ewm(span=span, adjust=False).mean()
                st.write(safe_head(df[[ewm_col, f"{ewm_col}_ewm"]], 10))
            except Exception as e:
                st.write("EWM failed:", e)
        else:
            st.write("No numeric columns for EWM demo.")

    # ----------------------------
    # ✍️ STRING & TEXT OPERATIONS
    # ----------------------------
    st.header("✍️ String & Text Operations | عمليات النصوص")

    with st.expander("🔹 Common .str methods"):
        st.code("df['Name'].str.lower()", language="python")
        text_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c]) or pd.api.types.is_string_dtype(df[c])]
        if text_cols:
            text_col = st.selectbox("Choose text column:", text_cols, key="text_col")
            op = st.selectbox("Operation:", ["lower", "upper", "title", "strip", "contains", "split"], key="text_op")
            if op == "lower":
                st.write(safe_head(df[text_col].str.lower(), 10))
            elif op == "upper":
                st.write(safe_head(df[text_col].str.upper(), 10))
            elif op == "title":
                st.write(safe_head(df[text_col].str.title(), 10))
            elif op == "strip":
                st.write(safe_head(df[text_col].str.strip(), 10))
            elif op == "contains":
                pat = st.text_input("Substring / regex to search for:", "", key="contains_pat")
                try:
                    st.write(safe_head(df[text_col].str.contains(pat, na=False), 10))
                except Exception as e:
                    st.write("Contains search failed:", e)
            elif op == "split":
                sep = st.text_input("Separator (default whitespace):", " ", key="split_sep")
                try:
                    st.write(safe_head(df[text_col].str.split(sep).astype(str), 10))
                except Exception as e:
                    st.write("Split failed:", e)
        else:
            st.write("No text columns detected.")

    # ----------------------------
    # 🕓 TIME SERIES OPERATIONS
    # ----------------------------
    st.header("🕓 Time Series Operations | عمليات السلاسل الزمنية")

    with st.expander("🔹 Convert to datetime & resample"):
        st.code("df['Date'] = pd.to_datetime(df['Date'])\ndf.set_index('Date', inplace=True)\ndf.resample('M').mean()", language="python")
        date_cols = [c for c in df.columns if pd.api.types.is_datetime64_any_dtype(df[c]) or df[c].astype(str).str.match(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}').any()]
        # present available columns and let user convert
        st.write("Detected likely date-like columns (heuristic):", date_cols[:5])
        chosen_date_col = st.selectbox("Choose a column to convert to datetime (if any):", ["<none>"] + df.columns.tolist(), key="date_col")
        if chosen_date_col != "<none>":
            try:
                df[chosen_date_col] = pd.to_datetime(df[chosen_date_col], errors='coerce')
                st.write(df[chosen_date_col].dt.strftime('%Y-%m-%d').head(10))
                if st.checkbox("Set this column as index and resample monthly mean preview", key="resample_check"):
                    df_ts = df.set_index(chosen_date_col)
                    st.write(safe_head(df_ts.resample('M').mean(numeric_only=True), 10))
            except Exception as e:
                st.write("Datetime conversion failed:", e)
        else:
            st.write("No conversion chosen.")

    # ----------------------------
    # 🧠 LAMBDA & APPLYMAP
    # ----------------------------
    st.header("🧠 Lambda & apply/applymap | دوال لامبدا وتطبيقات")

    with st.expander("🔹 df.applymap and df.apply"):
        st.code("df.applymap(lambda x: x.strip() if isinstance(x, str) else x)", language="python")
        if st.button("Trim whitespace in all object columns (preview)"):
            try:
                obj_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c])]
                df_preview = df.copy()
                for c in obj_cols:
                    df_preview[c] = df_preview[c].apply(lambda x: x.strip() if isinstance(x, str) else x)
                st.write(safe_head(df_preview[obj_cols], 10))
            except Exception as e:
                st.write("applymap failed:", e)

    # ----------------------------
    # 🧮 CROSSTABS & PIVOT
    # ----------------------------
    st.header("🧮 Crosstabs & Pivot | الجداول المحورية")

    with st.expander("🔹 pd.crosstab example"):
        st.code("pd.crosstab(df['Gender'], df['Dept'], margins=True)", language="python")
        if len(df.columns) >= 2:
            col_a = st.selectbox("Row (crosstab):", df.columns, key="ct_a")
            col_b = st.selectbox("Col (crosstab):", df.columns, key="ct_b")
            try:
                st.write(pd.crosstab(df[col_a], df[col_b], margins=True).head(50))
            except Exception as e:
                st.write("Crosstab failed:", e)
        else:
            st.write("Not enough columns for crosstab demo.")

    # ----------------------------
    # 🧱 COMBINING DATASETS (append/concat/merge)
    # ----------------------------
    st.header("🧱 Combining Datasets | دمج البيانات")

    with st.expander("🔹 Append / concat / join examples"):
        st.code("pd.concat([df1, df2]); df.append(row); df.join(other_df)", language="python")
        st.write("Use concat to stack, join to combine by index, append is deprecated in newer pandas versions.")

    # ----------------------------
    # 📊 CORRELATION & COVARIANCE
    # ----------------------------
    st.header("📊 Correlation & Covariance | الارتباط والتغاير")

    with st.expander("🔹 df.corr() and df.cov()"):
        st.code("df.corr(); df.cov()", language="python")
        try:
            corr = df.corr()
            st.write(safe_head(corr, 20))
            st.write("You can visualize the correlation matrix using a heatmap externally.")
        except Exception as e:
            st.write("Correlation calculation failed:", e)

    # ----------------------------
    # 🧰 PERFORMANCE OPTIMIZATION
    # ----------------------------
    st.header("🧰 Performance & Optimization | الأداء والتحسين")

    with st.expander("🔹 memory_usage, astype('category'), sample"):
        st.code("df.memory_usage(deep=True); df.astype('category')", language="python")
        try:
            mem = df.memory_usage(deep=True)
            st.write(mem)
            if st.button("Convert object columns to category where appropriate (preview)"):
                df_preview = df.copy()
                for c in df_preview.columns:
                    if df_preview[c].nunique() < (len(df_preview) * 0.5) and df_preview[c].dtype == object:
                        df_preview[c] = df_preview[c].astype('category')
                st.write(safe_head(df_preview.dtypes, 50))
        except Exception as e:
            st.write("Performance ops failed:", e)

    # ----------------------------
    # 🧾 ADVANCED EXPORT OPTIONS
    # ----------------------------
    st.header("🧾 Advanced Export Options | خيارات التصدير المتقدمة")

    with st.expander("🔹 to_csv with encoding, to_json, to_pickle"):
        st.code("df.to_csv('file.csv', sep=';', encoding='utf-8')", language="python")
        st.write("Use `to_pickle` for faster local re-loads: df.to_pickle('data.pkl')")

    # ----------------------------
    # 🧪 USEFUL SHORTCUTS (display options)
    # ----------------------------
    st.header("🧪 Useful Shortcuts | اختصارات مفيدة")

    with st.expander("🔹 pd.set_option and styling"):
        st.code("pd.set_option('display.max_columns', None)", language="python")
        if st.button("Show all columns (temporary)"):
            pd.set_option('display.max_columns', None)
            st.write("Max columns display set to None (for this session).")
        st.write("You can style DataFrame for reports (df.style...).")

    # ----------------------------
    # 31-50: EXPERT LEVEL (merged into sections)
    # ----------------------------
    st.header("⚡ Expert-Level Pandas (31-50) | مستوى متقدم")

    with st.expander("🔹 Advanced merge & join tricks"):
        st.code("pd.merge(df1, df2, on=['id','year'], how='outer', suffixes=('_l','_r'))", language="python")
        st.write("You can merge on multiple keys, use suffixes, or merge by index.")

    with st.expander("🔹 Map, replace, dictionary mapping"):
        st.code("df['Gender'] = df['Gender'].map({'M':'Male','F':'Female'})", language="python")
        if st.button("Example map first categorical-like column"):
            cat_candidates = [c for c in df.columns if df[c].nunique() < 50]
            if cat_candidates:
                c = cat_candidates[0]
                mapping_preview = {k: str(k) + "_mapped" for k in list(df[c].dropna().unique())[:10]}
                st.write("Preview mapping (example):", mapping_preview)
                st.write(safe_head(df[[c]], 10))
            else:
                st.write("No good categorical candidates for demo.")

    with st.expander("🔹 Math & logical operations"):
        st.code("df['Normalized'] = (df['Value'] - min)/(max-min)", language="python")
        st.write("Normalization, log transforms, boolean masks — use numpy functions (np.log, np.where).")

    with st.expander("🔹 Time series resampling & shifting"):
        st.code("df.shift(1); df['diff'] = df['Value'].diff()", language="python")
        st.write("Shift and diff are handy for time-based features.")

    with st.expander("🔹 Styling DataFrames for reports"):
        st.code("df.style.background_gradient()", language="python")
        st.write("Styling is great for HTML/Excel reports; not all styles show in Streamlit.")

    with st.expander("🔹 Multi-level aggregation example"):
        st.code("df.groupby(['Dept','Gender']).agg({'Salary':['mean','max'],'Age':'median'})", language="python")
        st.write("Use dict-of-lists to specify different aggregations per column.")

    with st.expander("🔹 Reshaping (stack/unstack/melt/pivot)"):
        st.code("df.melt(id_vars=['Name'], var_name='Subject', value_name='Score')", language="python")
        st.write("Melt to long, pivot to wide, stack/unstack for index<->columns transformations.")

    with st.expander("🔹 Numpy integration & math"):
        st.code("df['sqrt'] = np.sqrt(df['Value'])", language="python")
        st.write("Use NumPy for vectorized math: np.log, np.exp, np.where, np.random etc.")

    with st.expander("🔹 sklearn integration (preprocessing)"):
        st.code("from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\ndf[['A','B']] = scaler.fit_transform(df[['A','B']])", language="python")
        st.write("Scale numeric columns before ML. (scikit-learn needed in environment)")

    with st.expander("🔹 Visualization with matplotlib"):
        st.code("df.groupby('Dept')['Salary'].mean().plot(kind='bar')", language="python")
        try:
            viz_col = st.selectbox("Choose a numeric column to histogram (expert):", [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])], key="viz_col")
            if st.button("Show histogram"):
                fig, ax = plt.subplots()
                df[viz_col].dropna().hist(ax=ax)
                ax.set_title(f"Histogram of {viz_col}")
                st.pyplot(fig)
        except Exception as e:
            st.write("Plot failed:", e)

    with st.expander("🔹 Working with large datasets (chunks & dtypes)"):
        st.code("pd.read_csv('big.csv', chunksize=10000); dtype={'ID':'int32'}", language="python")
        st.write("Use chunksize to iterate and dtype argument to save memory when reading big files.")

    with st.expander("🔹 Encoding & categorical handling"):
        st.code("pd.get_dummies(df, columns=['Gender'])", language="python")
        st.write("Use .astype('category') or pd.get_dummies for one-hot encoding.")

    with st.expander("🔹 Outlier detection (IQR)"):
        st.code("iqr = q3 - q1; outliers = df[(df['Value'] < q1-1.5*iqr) | (df['Value'] > q3+1.5*iqr)]", language="python")
        st.write("IQR method for simple outlier detection.")

    with st.expander("🔹 Correlation heatmap hint"):
        st.code("import seaborn as sns\nsns.heatmap(df.corr(), annot=True)", language="python")
        st.write("Seaborn heatmap is useful in notebooks; Streamlit can show matplotlib figs.")

    with st.expander("🔹 Data transformations (log/scaling/rank)"):
        st.code("df['log_salary'] = np.log1p(df['Salary'])", language="python")
        st.write("log1p handles zero values safely; ranking via df['rank'] = df['Score'].rank().")

    with st.expander("🔹 Window analytics (rolling std/mean)"):
        st.code("df['rolling_avg'] = df['Value'].rolling(5).mean()", language="python")
        st.write("Use rolling/ewm for time-series features.")

    with st.expander("🔹 DataFrame compare/debug"):
        st.code("df.compare(df2); df.equals(df2)", language="python")
        st.write("Useful to check changes between versions of datasets.")

    with st.expander("🔹 String normalization & regex cleaning"):
        st.code("df['Text'] = df['Text'].str.replace(r'[^A-Za-z0-9 ]','', regex=True)", language="python")
        st.write("Use regex to clean text columns (be careful with languages and characters).")

    with st.expander("🔹 Save/load with pickle for speed"):
        st.code("df.to_pickle('dataset.pkl'); pd.read_pickle('dataset.pkl')", language="python")
        st.write("Pickle is fast for local workflows but not ideal for sharing.")

    with st.expander("🔹 Debugging tools & pipe"):
        st.code("df.pipe(lambda x: x.head())", language="python")
        st.write("Use df.info(memory_usage='deep') and df.pipe() for chaining and debugging.")

    # ----------------------------
    # 🧾 FINAL NOTES & FOOTER
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
