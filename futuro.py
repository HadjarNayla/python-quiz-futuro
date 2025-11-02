import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO, StringIO

# ========================================
# CONFIGURATION
# ========================================
st.set_page_config(page_title="🎯 تمرين Pandas الشامل | Exercice Complet", layout="wide")

# ========================================
# HEADER
# ========================================
st.title("🎯 تمرين Pandas الشامل من A إلى Z")
st.title("🎯 Exercice Complet Pandas de A à Z")
st.markdown("### 🎓 مدرسة فيوتشر | Futuro School")
st.markdown("**الأستاذة: حجار نايلة | Prof: Hadjar Nayla**")
st.markdown("---")

# ========================================
# INTRODUCTION
# ========================================
with st.expander("📖 مقدمة التمرين | Introduction", expanded=True):
    st.markdown("""
    ### 🎯 الهدف | Objectif
    **العربية:** هذا تمرين شامل يغطي جميع عمليات Pandas من التحميل حتى التصدير.
    
    **Français:** Exercice complet couvrant toutes les opérations Pandas.
    
    ### 📋 ما ستتعلمه | Ce que vous allez apprendre:
    1. ✅ تحميل واستكشاف البيانات
    2. ✅ اكتشاف ومعالجة القيم المفقودة
    3. ✅ تنظيف وتحويل البيانات
    4. ✅ التصفية والاختيار المتقدم
    5. ✅ التجميع والتحليل
    6. ✅ التحليل الإحصائي
    7. ✅ التصور البياني
    8. ✅ التصدير والحفظ
    
    ### 📊 Datasets Recommandés:
    - Titanic Dataset
    - House Prices Dataset
    - FIFA Players Dataset
    - Sales Data
    - COVID-19 Dataset
    """)

st.markdown("---")

# ========================================
# UPLOAD FILE
# ========================================
st.header("📁 الجزء 1: تحميل البيانات | Partie 1: Chargement")

uploaded_file = st.file_uploader(
    "ارفع ملف CSV من Kaggle | Téléversez un fichier CSV",
    type=['csv']
)

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ تم تحميل البيانات بنجاح!")
        
        # ========================================
        # EXERCICE 1: EXPLORATION
        # ========================================
        st.markdown("---")
        st.header("🔍 التمرين 1: الاستكشاف الأولي | Exercice 1: Exploration")
        
        tab1, tab2, tab3 = st.tabs(["📊 النتائج", "💻 الكود", "📝 الملاحظات"])
        
        with tab1:
            st.write("### 1️⃣ أول 10 صفوف | First 10 Rows")
            st.dataframe(df.head(10), use_container_width=True)
            
            st.write("### 2️⃣ آخر 10 صفوف | Last 10 Rows")
            st.dataframe(df.tail(10), use_container_width=True)
            
            st.write("### 3️⃣ الشكل | Shape")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("الصفوف | Rows", df.shape[0])
            with col2:
                st.metric("الأعمدة | Columns", df.shape[1])
            with col3:
                st.metric("الخلايا | Cells", df.shape[0] * df.shape[1])
            
            st.write("### 4️⃣ الأعمدة | Columns")
            st.write(df.columns.tolist())
            
            st.write("### 5️⃣ أنواع البيانات | Data Types")
            dtype_df = pd.DataFrame({
                'العمود': df.dtypes.index,
                'النوع': df.dtypes.values
            })
            st.dataframe(dtype_df, use_container_width=True)
            
            st.write("### 6️⃣ معلومات البيانات | Data Info")
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
            
            st.write("### 7️⃣ الملخص الإحصائي | Statistics")
            st.dataframe(df.describe(include='all'), use_container_width=True)
        
        with tab2:
            st.code("""
import pandas as pd
import numpy as np

# تحميل البيانات
df = pd.read_csv('dataset.csv')

# الاستكشاف الأولي
print(df.head(10))
print(df.tail(10))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe(include='all'))
            """, language='python')
        
        with tab3:
            st.markdown("""
            ### 📝 ملاحظات مهمة
            
            - استخدم head() و tail() للتعرف السريع على البيانات
            - shape يعطيك (عدد الصفوف، عدد الأعمدة)
            - info() يعرض أنواع البيانات والقيم المفقودة
            - describe() يعرض إحصائيات للأعمدة الرقمية
            """)
        
        # ========================================
        # EXERCICE 2: MISSING VALUES
        # ========================================
        st.markdown("---")
        st.header("🔍 التمرين 2: اكتشاف المشاكل | Exercice 2: Détection")
        
        tab1, tab2, tab3 = st.tabs(["📊 النتائج", "💻 الكود", "📈 التصور"])
        
        with tab1:
            st.write("### 1️⃣ القيم المفقودة | Missing Values")
            missing = df.isnull().sum()
            missing_percent = (missing / len(df)) * 100
            missing_df = pd.DataFrame({
                'العمود': missing.index,
                'المفقودة': missing.values,
                'النسبة': missing_percent.values.round(2)
            })
            missing_df = missing_df[missing_df['المفقودة'] > 0]
            
            if len(missing_df) > 0:
                st.dataframe(missing_df, use_container_width=True)
            else:
                st.success("✅ لا توجد قيم مفقودة!")
            
            st.write("### 2️⃣ التكرارات | Duplicates")
            duplicates = df.duplicated().sum()
            col1, col2 = st.columns(2)
            with col1:
                st.metric("عدد التكرارات", duplicates)
            with col2:
                st.metric("النسبة", f"{(duplicates/len(df)*100):.2f}%")
        
        with tab2:
            st.code("""
# حساب القيم المفقودة
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100
print(missing[missing > 0])

# اكتشاف التكرارات
duplicates = df.duplicated().sum()
print(f"Duplicate rows: {duplicates}")

# عرض الصفوف المكررة
print(df[df.duplicated(keep=False)])
            """, language='python')
        
        with tab3:
            st.write("### 📊 تصور القيم المفقودة")
            missing = df.isnull().sum()
            missing_data = missing[missing > 0]
            
            if len(missing_data) > 0:
                fig, ax = plt.subplots(figsize=(12, 6))
                missing_data.plot(kind='bar', ax=ax, color='coral', edgecolor='black')
                ax.set_title('القيم المفقودة حسب العمود', fontsize=14, fontweight='bold')
                ax.set_ylabel('العدد')
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
            else:
                st.info("✅ لا توجد قيم مفقودة")
        
        # ========================================
        # EXERCICE 3: CLEANING
        # ========================================
        st.markdown("---")
        st.header("🧹 التمرين 3: تنظيف البيانات | Exercice 3: Nettoyage")
        
        df_clean = df.copy()
        
        tab1, tab2, tab3 = st.tabs(["📊 النتائج", "💻 الكود", "📈 المقارنة"])
        
        with tab1:
            st.write("### 🔧 عملية التنظيف")
            
            # حذف الأعمدة بقيم مفقودة كثيرة
            threshold = 0.5
            missing_percent = df_clean.isnull().sum() / len(df_clean)
            cols_to_drop = missing_percent[missing_percent > threshold].index.tolist()
            if cols_to_drop:
                st.warning(f"⚠️ الأعمدة المحذوفة: {cols_to_drop}")
                df_clean = df_clean.drop(columns=cols_to_drop)
            
            # ملء القيم الرقمية
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                if df_clean[col].isnull().sum() > 0:
                    mean_val = df_clean[col].mean()
                    df_clean[col].fillna(mean_val, inplace=True)
                    st.success(f"✅ {col}: ملء بالمتوسط {mean_val:.2f}")
            
            # ملء القيم النصية
            text_cols = df_clean.select_dtypes(include=['object']).columns
            for col in text_cols:
                if df_clean[col].isnull().sum() > 0:
                    df_clean[col].fillna('Unknown', inplace=True)
                    st.success(f"✅ {col}: ملء بـ Unknown")
            
            # حذف الصفوف المتبقية
            before = len(df_clean)
            df_clean = df_clean.dropna()
            after = len(df_clean)
            if before - after > 0:
                st.warning(f"⚠️ صفوف محذوفة: {before - after}")
            
            st.write("### ✅ البيانات النظيفة")
            st.dataframe(df_clean.head(10))
        
        with tab2:
            st.code("""
# إنشاء نسخة
df_clean = df.copy()

# حذف الأعمدة بقيم مفقودة كثيرة
threshold = 0.5
missing_percent = df_clean.isnull().sum() / len(df_clean)
cols_to_drop = missing_percent[missing_percent > threshold].index
df_clean = df_clean.drop(columns=cols_to_drop)

# ملء القيم الرقمية بالمتوسط
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df_clean[col].fillna(df_clean[col].mean(), inplace=True)

# ملء القيم النصية
text_cols = df_clean.select_dtypes(include=['object']).columns
for col in text_cols:
    df_clean[col].fillna('Unknown', inplace=True)

# حذف الصفوف المتبقية
df_clean = df_clean.dropna()
            """, language='python')
        
        with tab3:
            st.write("### 📊 مقارنة قبل وبعد")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("الصفوف", df_clean.shape[0], delta=df_clean.shape[0] - df.shape[0])
            with col2:
                st.metric("الأعمدة", df_clean.shape[1], delta=df_clean.shape[1] - df.shape[1])
            with col3:
                st.metric("قيم مفقودة", df_clean.isnull().sum().sum(), 
                         delta=df_clean.isnull().sum().sum() - df.isnull().sum().sum())
        
        # ========================================
        # EXERCICE 4: TRANSFORMATION
        # ========================================
        st.markdown("---")
        st.header("🔄 التمرين 4: تحويل البيانات | Exercice 4: Transformation")
        
        tab1, tab2 = st.tabs(["📊 النتائج", "💻 الكود"])
        
        with tab1:
            st.write("### 1️⃣ توحيد أسماء الأعمدة")
            df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_')
            st.success("✅ تم توحيد أسماء الأعمدة")
            st.write(df_clean.columns.tolist())
            
            st.write("### 2️⃣ إنشاء أعمدة جديدة")
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) >= 2:
                col1_name = st.selectbox("العمود الأول:", numeric_cols)
                col2_name = st.selectbox("العمود الثاني:", 
                                        [c for c in numeric_cols if c != col1_name])
                
                if st.button("إنشاء عمود مجموع"):
                    new_col = f"{col1_name}_plus_{col2_name}"
                    df_clean[new_col] = df_clean[col1_name] + df_clean[col2_name]
                    st.success(f"✅ تم إنشاء: {new_col}")
                    st.dataframe(df_clean[[col1_name, col2_name, new_col]].head(10))
            
            st.dataframe(df_clean.head(10))
        
        with tab2:
            st.code("""
# توحيد أسماء الأعمدة
df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_')

# إنشاء عمود من عملية حسابية
df_clean['total'] = df_clean['price'] * df_clean['quantity']

# عمود شرطي
df_clean['category'] = np.where(df_clean['age'] >= 18, 'Adult', 'Minor')

# تحويل أنواع البيانات
df_clean['column'] = df_clean['column'].astype('category')
            """, language='python')
        
        # ========================================
        # EXERCICE 5: FILTERING
        # ========================================
        st.markdown("---")
        st.header("🔍 التمرين 5: التصفية | Exercice 5: Filtrage")
        
        tab1, tab2 = st.tabs(["📊 النتائج", "💻 الكود"])
        
        with tab1:
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                st.write("### تصفية تفاعلية")
                filter_col = st.selectbox("اختر العمود:", numeric_cols)
                
                min_val = float(df_clean[filter_col].min())
                max_val = float(df_clean[filter_col].max())
                
                filter_range = st.slider(f"النطاق:", min_val, max_val, (min_val, max_val))
                
                filtered_df = df_clean[
                    (df_clean[filter_col] >= filter_range[0]) & 
                    (df_clean[filter_col] <= filter_range[1])
                ]
                
                st.write(f"عدد النتائج: {len(filtered_df)} من {len(df_clean)}")
                st.dataframe(filtered_df.head(20))
        
        with tab2:
            st.code("""
# تصفية بشرط واحد
filtered = df_clean[df_clean['age'] > 30]

# تصفية AND
filtered_and = df_clean[(df_clean['age'] > 25) & (df_clean['salary'] > 50000)]

# تصفية OR
filtered_or = df_clean[(df_clean['city'] == 'Paris') | (df_clean['city'] == 'Lyon')]

# استخدام isin()
cities = ['Paris', 'Lyon']
filtered_isin = df_clean[df_clean['city'].isin(cities)]

# استخدام between()
filtered_between = df_clean[df_clean['age'].between(25, 35)]
            """, language='python')
        
        # ========================================
        # EXERCICE 6: GROUPING
        # ========================================
        st.markdown("---")
        st.header("📊 التمرين 6: التجميع | Exercice 6: Groupement")
        
        tab1, tab2 = st.tabs(["📊 النتائج", "💻 الكود"])
        
        with tab1:
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            text_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
            
            if len(text_cols) > 0 and len(numeric_cols) > 0:
                st.write("### التجميع")
                group_col = st.selectbox("عمود التجميع:", text_cols)
                agg_col = st.selectbox("عمود التجميع:", numeric_cols)
                
                grouped = df_clean.groupby(group_col)[agg_col].agg(['mean', 'sum', 'count'])
                st.dataframe(grouped)
                
                fig, ax = plt.subplots(figsize=(12, 6))
                grouped['mean'].plot(kind='bar', ax=ax, color='skyblue')
                ax.set_title(f'متوسط {agg_col} حسب {group_col}')
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig)
        
        with tab2:
            st.code("""
# تجميع بسيط
grouped = df_clean.groupby('category')['value'].mean()

# تجميع بعدة دوال
grouped_multi = df_clean.groupby('category')['value'].agg(['mean', 'sum', 'count'])

# جدول محوري
pivot = pd.pivot_table(df_clean, values='value', index='category', 
                       columns='region', aggfunc='mean')

# value_counts
value_counts = df_clean['category'].value_counts()
            """, language='python')
        
        # ========================================
        # EXERCICE 7: STATISTICS
        # ========================================
        st.markdown("---")
        st.header("📈 التمرين 7: التحليل الإحصائي | Exercice 7: Statistiques")
        
        tab1, tab2, tab3 = st.tabs(["📊 النتائج", "💻 الكود", "📈 التصور"])
        
        with tab1:
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 1:
                st.write("### مصفوفة الارتباط")
                corr_matrix = df_clean[numeric_cols].corr()
                st.dataframe(corr_matrix.style.background_gradient(cmap='coolwarm'))
            
            if len(numeric_cols) > 0:
                st.write("### اكتشاف القيم الشاذة")
                outlier_col = st.selectbox("اختر عمود:", numeric_cols)
                
                Q1 = df_clean[outlier_col].quantile(0.25)
                Q3 = df_clean[outlier_col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                
                outliers = df_clean[(df_clean[outlier_col] < lower) | 
                                   (df_clean[outlier_col] > upper)]
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Q1", f"{Q1:.2f}")
                with col2:
                    st.metric("Q3", f"{Q3:.2f}")
                with col3:
                    st.metric("قيم شاذة", len(outliers))
        
        with tab2:
            st.code("""
# مصفوفة الارتباط
corr = df_clean.corr()

# اكتشاف القيم الشاذة
Q1 = df_clean['column'].quantile(0.25)
Q3 = df_clean['column'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df_clean[(df_clean['column'] < lower) | (df_clean['column'] > upper)]

# إحصائيات
mean = df_clean['column'].mean()
median = df_clean['column'].median()
std = df_clean['column'].std()
            """, language='python')
        
        with tab3:
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 1:
                st.write("### خريطة الارتباط")
                fig, ax = plt.subplots(figsize=(10, 8))
                corr = df_clean[numeric_cols].corr()
                sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
                ax.set_title('مصفوفة الارتباط')
                st.pyplot(fig)
        
        # ========================================
        # EXERCICE 8: VISUALIZATION
        # ========================================
        st.markdown("---")
        st.header("📊 التمرين 8: التصور | Exercice 8: Visualisation")
        
        tab1, tab2 = st.tabs(["📊 الرسوم", "💻 الكود"])
        
        with tab1:
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                st.write("### الهستوغرام")
                hist_col = st.selectbox("اختر عمود:", numeric_cols, key="hist")
                
                fig, ax = plt.subplots(figsize=(12, 6))
                df_clean[hist_col].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
                ax.set_title(f'توزيع {hist_col}')
                ax.set_xlabel(hist_col)
                ax.set_ylabel('التكرار')
                st.pyplot(fig)
        
        with tab2:
            st.code("""
import matplotlib.pyplot as plt

# هستوغرام
plt.figure(figsize=(12, 6))
df_clean['column'].hist(bins=30)
plt.title('Distribution')
plt.show()

# رسم شريطي
df_clean.groupby('category')['value'].mean().plot(kind='bar')
plt.show()

# scatter plot
plt.scatter(df_clean['x'], df_clean['y'])
plt.show()
            """, language='python')
        
        # ========================================
        # EXERCICE 9: EXPORT
        # ========================================
        st.markdown("---")
        st.header("💾 التمرين 9: التصدير | Exercice 9: Export")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("#### CSV")
            csv = df_clean.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ تحميل CSV", csv, "data.csv", "text/csv")
        
        with col2:
            st.write("#### Excel")
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df_clean.to_excel(writer, index=False)
            st.download_button("⬇️ تحميل Excel", buffer.getvalue(), "data.xlsx")
        
        with col3:
            st.write("#### JSON")
            json_str = df_clean.to_json(orient='records', indent=2)
            st.download_button("⬇️ تحميل JSON", json_str, "data.json")
        
        # ========================================
        # FINAL REPORT
        # ========================================
        st.markdown("---")
        st.header("📋 التقرير النهائي | Rapport Final")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### البيانات الأصلية")
            st.metric("الصفوف", df.shape[0])
            st.metric("الأعمدة", df.shape[1])
            st.metric("قيم مفقودة", df.isnull().sum().sum())
        
        with col2:
            st.markdown("#### البيانات النظيفة")
            st.metric("الصفوف", df_clean.shape[0], delta=df_clean.shape[0]-df.shape[0])
            st.metric("الأعمدة", df_clean.shape[1], delta=df_clean.shape[1]-df.shape[1])
            st.metric("قيم مفقودة", df_clean.isnull().sum().sum(), 
                     delta=df_clean.isnull().sum().sum()-df.isnull().sum().sum())
        
        st.balloons()
        
        st.markdown("---")
        st.markdown("## 🎉 تهانينا! أكملت التمرين الشامل")
        st.markdown("### 🎓 مدرسة فيوتشر | Futuro School")
        st.markdown("**الأستاذة: حجار نايلة**")
    
    except Exception as e:
        st.error(f"خطأ: {str(e)}")

else:
    st.info("👆 قم برفع ملف CSV لبدء التمرين")
    
    st.markdown("### 🎯 الأهداف التعليمية")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **ستتعلم:**
        - ✅ تحميل ومعاينة البيانات
        - ✅ اكتشاف المشاكل
        - ✅ تنظيف البيانات
        - ✅ التحويل والتحليل
        - ✅ التصور والتصدير
        """)
    
    with col2:
        st.markdown("""
        **Datasets مقترحة:**
        - 🚢 Titanic
        - 🏠 House Prices
        - ⚽ FIFA Players
        - 🛒 Sales Data
        """)
