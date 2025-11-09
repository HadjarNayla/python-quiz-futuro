# Save this file as: matplotlib_app.py (NOT matplotlib.py!)
# Run with: streamlit run matplotlib_app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# ----------------------------
# 🏷️ APP CONFIGURATION
# ----------------------------
st.set_page_config(page_title="📊 Matplotlib from 0 to Hero | Futuro School", layout="wide")

# ----------------------------
# 🎓 HEADER & BRANDING
# ----------------------------
st.title("📊 تعلم جميع وظائف Matplotlib — من الصفر إلى الاحتراف")
st.title("📊 Learn All Matplotlib Functions — From 0 to Hero")
st.write("**English:** This app teaches Matplotlib step by step. Explore every important visualization function interactively!")
st.markdown("### 🎓 Futuro School")
st.markdown("**تم التطوير بواسطة الأستاذة: حجار نايلة | Developed by Teacher: Hadjar Nayla**")
st.markdown("---")

# ----------------------------
# 📂 UPLOAD OR USE SAMPLE DATA
# ----------------------------
st.header("📁 الخطوة 1 (اختياري): تحميل ملف CSV | Step 1 (Optional): Upload CSV")
st.write("**العربية:** يمكنك تحميل بياناتك الخاصة أو استخدام بيانات عشوائية")
st.write("**English:** You can upload your own data or use sample data")

uploaded_file = st.file_uploader("ارفع ملف CSV (اختياري) | Upload CSV (optional)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ تم تحميل البيانات بنجاح! | Dataset loaded successfully!")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"فشل قراءة الملف | Failed to read CSV: {e}")
        df = None

if not uploaded_file or df is None:
    np.random.seed(42)
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
        'Sales': [150, 230, 180, 320, 280, 390, 350, 420],
        'Profit': [80, 120, 95, 180, 150, 220, 190, 240],
        'Expenses': [120, 180, 140, 250, 210, 300, 270, 320]
    })
    st.info("💡 يتم استخدام بيانات عشوائية | Using sample data")
    st.dataframe(df.head())

# ----------------------------
# 📘 SECTION 1: BASIC PLOTTING
# ----------------------------
st.markdown("---")
st.header("📘 القسم 1: الرسم الأساسي | Section 1: Basic Plotting")

with st.expander("1️⃣ plt.plot() — رسم خطي | Line plot"):
    st.code("plt.plot(x, y, marker='o', linewidth=2)", language="python")
    st.write("**العربية:** يرسم خط بين نقاط البيانات")
    st.write("**English:** Draws a line connecting data points")
    
    if st.button("إظهار | Show", key="1"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#2E86AB', label='Sales')
        ax.set_title('Sales Trend | اتجاه المبيعات', fontsize=16, fontweight='bold')
        ax.set_xlabel('Month | الشهر', fontsize=12)
        ax.set_ylabel('Sales | المبيعات', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣ plt.scatter() — رسم نقطي | Scatter plot"):
    st.code("plt.scatter(x, y, s=size, c=colors, alpha=0.6)", language="python")
    st.write("**العربية:** يرسم نقاط منفصلة")
    st.write("**English:** Plots individual points")
    
    if st.button("إظهار | Show", key="2"):
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df['Sales'], df['Profit'], s=df['Expenses'], 
                           c=df.index, cmap='viridis', alpha=0.6, edgecolors='black')
        ax.set_title('Sales vs Profit | المبيعات مقابل الأرباح', fontsize=16, fontweight='bold')
        ax.set_xlabel('Sales | المبيعات', fontsize=12)
        ax.set_ylabel('Profit | الأرباح', fontsize=12)
        plt.colorbar(scatter, ax=ax, label='Index')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("3️⃣ plt.bar() — رسم أعمدة | Bar chart"):
    st.code("plt.bar(categories, values, color='skyblue')", language="python")
    st.write("**العربية:** يرسم أعمدة عمودية")
    st.write("**English:** Draws vertical bars")
    
    if st.button("إظهار | Show", key="3"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['Month'], df['Sales'], color='#A23B72', edgecolor='black', alpha=0.7)
        ax.set_title('Sales by Month | المبيعات حسب الشهر', fontsize=16, fontweight='bold')
        ax.set_xlabel('Month | الشهر', fontsize=12)
        ax.set_ylabel('Sales | المبيعات', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("4️⃣ plt.barh() — أعمدة أفقية | Horizontal bar"):
    st.code("plt.barh(categories, values)", language="python")
    st.write("**العربية:** يرسم أعمدة أفقية")
    st.write("**English:** Draws horizontal bars")
    
    if st.button("إظهار | Show", key="4"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(df['Month'], df['Profit'], color='#F18F01', edgecolor='black', alpha=0.7)
        ax.set_title('Profit by Month | الأرباح حسب الشهر', fontsize=16, fontweight='bold')
        ax.set_xlabel('Profit | الأرباح', fontsize=12)
        ax.set_ylabel('Month | الشهر', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📊 SECTION 2: STATISTICAL PLOTS
# ----------------------------
st.markdown("---")
st.header("📊 القسم 2: الرسوم الإحصائية | Section 2: Statistical Plots")

with st.expander("5️⃣ plt.hist() — هستوغرام | Histogram"):
    st.code("plt.hist(data, bins=20, edgecolor='black')", language="python")
    st.write("**العربية:** يرسم توزيع البيانات")
    st.write("**English:** Plots data distribution")
    
    if st.button("إظهار | Show", key="5"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = np.random.normal(200, 40, 1000)
        ax.hist(data, bins=30, color='#06A77D', edgecolor='black', alpha=0.7)
        ax.set_title('Data Distribution | توزيع البيانات', fontsize=16, fontweight='bold')
        ax.set_xlabel('Value | القيمة', fontsize=12)
        ax.set_ylabel('Frequency | التكرار', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("6️⃣ plt.boxplot() — رسم صندوقي | Box plot"):
    st.code("plt.boxplot([data1, data2, data3])", language="python")
    st.write("**العربية:** يعرض الوسيط والقيم الشاذة")
    st.write("**English:** Shows median and outliers")
    
    if st.button("إظهار | Show", key="6"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = [df['Sales'], df['Profit'], df['Expenses']]
        box = ax.boxplot(data, labels=['Sales', 'Profit', 'Expenses'],
                        patch_artist=True, notch=True)
        colors = ['#E63946', '#06A77D', '#457B9D']
        for patch, color in zip(box['boxes'], colors):
            patch.set_facecolor(color)
        ax.set_title('Statistical Comparison | مقارنة إحصائية', fontsize=16, fontweight='bold')
        ax.set_ylabel('Value | القيمة', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🥧 SECTION 3: PIE & AREA CHARTS
# ----------------------------
st.markdown("---")
st.header("🥧 القسم 3: الدوائر والمساحات | Section 3: Pie & Area Charts")

with st.expander("7️⃣ plt.pie() — رسم دائري | Pie chart"):
    st.code("plt.pie(values, labels=labels, autopct='%1.1f%%')", language="python")
    st.write("**العربية:** يعرض النسب المئوية")
    st.write("**English:** Shows percentages")
    
    if st.button("إظهار | Show", key="7"):
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']
        explode = [0.1] + [0] * (len(df) - 1)
        ax.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', 
               colors=colors[:len(df)], explode=explode, shadow=True, startangle=90)
        ax.set_title('Sales Distribution | توزيع المبيعات', fontsize=16, fontweight='bold')
        st.pyplot(fig)
        plt.close()

with st.expander("8️⃣ plt.fill_between() — ملء المساحة | Fill area"):
    st.code("plt.fill_between(x, y1, y2, alpha=0.3)", language="python")
    st.write("**العربية:** يملأ المساحة بين منحنيين")
    st.write("**English:** Fills area between curves")
    
    if st.button("إظهار | Show", key="8"):
        fig, ax = plt.subplots(figsize=(10, 6))
        x = df.index
        ax.plot(x, df['Sales'], label='Sales', color='#2E86AB', linewidth=2)
        ax.plot(x, df['Expenses'], label='Expenses', color='#E63946', linewidth=2)
        ax.fill_between(x, df['Sales'], df['Expenses'], 
                        where=(df['Sales'] >= df['Expenses']), 
                        interpolate=True, alpha=0.3, color='green', label='Profit')
        ax.fill_between(x, df['Sales'], df['Expenses'], 
                        where=(df['Sales'] < df['Expenses']), 
                        interpolate=True, alpha=0.3, color='red', label='Loss')
        ax.set_title('Sales vs Expenses | المبيعات مقابل المصروفات', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index | الفهرس', fontsize=12)
        ax.set_ylabel('Value | القيمة', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("9️⃣ plt.stackplot() — مساحات مكدسة | Stacked area"):
    st.code("plt.stackplot(x, y1, y2, y3)", language="python")
    st.write("**العربية:** يكدس عدة مساحات")
    st.write("**English:** Stacks multiple areas")
    
    if st.button("إظهار | Show", key="9"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.stackplot(df.index, df['Sales'], df['Profit'], df['Expenses'],
                    labels=['Sales', 'Profit', 'Expenses'],
                    colors=['#FF6B6B', '#4ECDC4', '#FFA07A'], alpha=0.8)
        ax.set_title('Stacked Areas | المساحات المكدسة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index | الفهرس', fontsize=12)
        ax.set_ylabel('Value | القيمة', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🎨 SECTION 4: CUSTOMIZATION
# ----------------------------
st.markdown("---")
st.header("🎨 القسم 4: التخصيص | Section 4: Customization")

with st.expander("🔟 Colors & Styles — الألوان والأنماط"):
    st.code("plt.plot(x, y, color='red', linestyle='--', marker='o')", language="python")
    
    col1, col2 = st.columns(2)
    with col1:
        color = st.color_picker("Color | اللون:", "#FF6B6B")
        linestyle = st.selectbox("Line style | نمط الخط:", ['-', '--', '-.', ':'])
    with col2:
        linewidth = st.slider("Width | السمك:", 1, 10, 2)
        marker = st.selectbox("Marker | العلامة:", ['o', 's', '^', 'D', '*'])
    
    if st.button("إظهار | Show", key="10"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], color=color, linestyle=linestyle, 
               linewidth=linewidth, marker=marker, markersize=10)
        ax.set_title('Custom Plot | رسم مخصص', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣1️⃣ plt.legend() — وسيلة الإيضاح | Legend"):
    st.code("plt.legend(loc='best')", language="python")
    
    if st.button("إظهار | Show", key="11"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], label='Sales', marker='o', linewidth=2)
        ax.plot(df.index, df['Profit'], label='Profit', marker='s', linewidth=2)
        ax.plot(df.index, df['Expenses'], label='Expenses', marker='^', linewidth=2)
        ax.set_title('Data Comparison | مقارنة البيانات', fontsize=16, fontweight='bold')
        ax.legend(loc='best', fontsize=11)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📐 SECTION 5: SUBPLOTS
# ----------------------------
st.markdown("---")
st.header("📐 القسم 5: الرسوم المتعددة | Section 5: Subplots")

with st.expander("1️⃣2️⃣ plt.subplot() — رسوم فرعية | Multiple plots"):
    st.code("plt.subplot(2, 2, 1)  # row, col, position", language="python")
    
    if st.button("إظهار | Show", key="12"):
        fig = plt.figure(figsize=(12, 10))
        
        ax1 = plt.subplot(2, 2, 1)
        ax1.plot(df.index, df['Sales'], marker='o', color='#FF6B6B', linewidth=2)
        ax1.set_title('Sales | المبيعات', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        ax2 = plt.subplot(2, 2, 2)
        ax2.bar(df['Month'], df['Profit'], color='#4ECDC4', alpha=0.7)
        ax2.set_title('Profit | الأرباح', fontsize=12, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        
        ax3 = plt.subplot(2, 2, 3)
        ax3.scatter(df['Sales'], df['Profit'], s=100, alpha=0.6)
        ax3.set_title('Sales vs Profit', fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        
        ax4 = plt.subplot(2, 2, 4)
        ax4.pie(df['Expenses'][:5], labels=df['Month'][:5], autopct='%1.1f%%')
        ax4.set_title('Expenses | المصروفات', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📈 SECTION 6: ADVANCED PLOTS
# ----------------------------
st.markdown("---")
st.header("📈 القسم 6: رسوم متقدمة | Section 6: Advanced Plots")

with st.expander("1️⃣3️⃣ Multiple Lines — خطوط متعددة"):
    if st.button("إظهار | Show", key="13"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], label='Sales', marker='o', linewidth=2, color='#E63946')
        ax.plot(df.index, df['Profit'], label='Profit', marker='s', linewidth=2, color='#06A77D')
        ax.plot(df.index, df['Expenses'], label='Expenses', marker='^', linewidth=2, color='#457B9D')
        ax.set_title('Multi-line Comparison | مقارنة متعددة الخطوط', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣4️⃣ Dual Axis — محوران | Two Y-axes"):
    st.code("ax2 = ax1.twinx()", language="python")
    
    if st.button("إظهار | Show", key="14"):
        fig, ax1 = plt.subplots(figsize=(10, 6))
        
        ax1.bar(df['Month'], df['Sales'], color='#FF6B6B', alpha=0.7, label='Sales')
        ax1.set_xlabel('Month', fontsize=12)
        ax1.set_ylabel('Sales', fontsize=12, color='#FF6B6B')
        ax1.tick_params(axis='y', labelcolor='#FF6B6B')
        ax1.tick_params(axis='x', rotation=45)
        
        ax2 = ax1.twinx()
        ax2.plot(df['Month'], df['Profit'], color='#06A77D', marker='o', linewidth=2, label='Profit')
        ax2.set_ylabel('Profit', fontsize=12, color='#06A77D')
        ax2.tick_params(axis='y', labelcolor='#06A77D')
        
        ax1.set_title('Dual Axis Plot | رسم بمحورين', fontsize=16, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🎓 FINAL SECTION
# ----------------------------
st.markdown("---")
st.header("🎉 تهانينا! | Congratulations!")
st.write("**العربية:** لقد أكملت جميع وظائف Matplotlib الأساسية")
st.write("**English:** You've completed all basic Matplotlib functions")

st.markdown("---")
st.markdown("**تم التطوير بواسطة الأستاذة: حجار نايلة**")
st.markdown("**Developed by Teacher: Hadjar Nayla**")
st.markdown("### 🎓 Futuro School")
st.markdown("*تمكين الطلاب بمهارات التصور البياني | Empowering students with data visualization skills*")

# Quick Reference
with st.expander("📚 مرجع سريع | Quick Reference"):
    st.markdown("""
    ### Basic Plots | الرسوم الأساسية
    - `plt.plot()` - Line plot | رسم خطي
    - `plt.scatter()` - Scatter plot | رسم نقطي
    - `plt.bar()` - Bar chart | رسم أعمدة
    - `plt.hist()` - Histogram | هستوغرام
    - `plt.pie()` - Pie chart | رسم دائري
    
    ### Customization | التخصيص
    - `plt.title()` - Add title | إضافة عنوان
    - `plt.xlabel()` - X label | تسمية X
    - `plt.ylabel()` - Y label | تسمية Y
    - `plt.legend()` - Add legend | إضافة وسيلة إيضاح
    - `plt.grid()` - Add grid | إضافة شبكة
    
    ### Layout | التخطيط
    - `plt.subplot()` - Multiple plots | رسوم متعددة
    - `plt.tight_layout()` - Adjust spacing | ضبط المسافات
    """)
