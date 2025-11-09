# Save this file as: matplotlib_app.py (NOT matplotlib.py!)
# Run with: streamlit run matplotlib_app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
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
st.write("**English:** This app teaches Matplotlib step by step with 50 functions. Explore every important visualization function interactively!")
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
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
        'Sales': [150, 230, 180, 320, 280, 390, 350, 420, 380, 450],
        'Profit': [80, 120, 95, 180, 150, 220, 190, 240, 210, 280],
        'Expenses': [120, 180, 140, 250, 210, 300, 270, 320, 290, 350],
        'Growth': [5, 8, 6, 12, 10, 15, 13, 18, 16, 20]
    })
    st.info("💡 يتم استخدام بيانات عشوائية | Using sample data")
    st.dataframe(df.head())

# ----------------------------
# 📘 SECTION 1: BASIC PLOTTING
# ----------------------------
st.markdown("---")
st.header("📘 القسم 1: الرسم الأساسي | Section 1: Basic Plotting")
st.write("**العربية:** تعلم كيفية إنشاء الرسوم البيانية الأساسية")
st.write("**English:** Learn how to create basic plots")

with st.expander("1️⃣ plt.plot() — رسم خطي | Line plot"):
    st.code("""
import matplotlib.pyplot as plt
plt.plot(x, y, marker='o', linewidth=2)
plt.show()
    """, language="python")
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
    st.code("""
plt.scatter(x, y, s=size, c=colors, alpha=0.6)
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم نقاط منفصلة في الفضاء ثنائي الأبعاد")
    st.write("**English:** Plots individual points in 2D space")
    
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
    st.code("""
plt.bar(categories, values, color='skyblue')
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم أعمدة عمودية لمقارنة القيم")
    st.write("**English:** Draws vertical bars to compare values")
    
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
    st.code("""
plt.barh(categories, values)
plt.show()
    """, language="python")
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
st.write("**العربية:** تعلم الرسوم البيانية للتحليل الإحصائي")
st.write("**English:** Learn statistical visualization charts")

with st.expander("5️⃣ plt.hist() — هستوغرام | Histogram"):
    st.code("""
plt.hist(data, bins=20, edgecolor='black')
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم توزيع البيانات في فئات")
    st.write("**English:** Plots data distribution in bins")
    
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
    st.code("""
plt.boxplot([data1, data2, data3])
plt.show()
    """, language="python")
    st.write("**العربية:** يعرض الوسيط والربيعيات والقيم الشاذة")
    st.write("**English:** Shows median, quartiles, and outliers")
    
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

with st.expander("7️⃣ plt.violinplot() — رسم كمانة | Violin plot"):
    st.code("""
plt.violinplot([data1, data2])
plt.show()
    """, language="python")
    st.write("**العربية:** يجمع بين الصندوقي وكثافة التوزيع")
    st.write("**English:** Combines box plot with distribution density")
    
    if st.button("إظهار | Show", key="7"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = [df['Sales'].values, df['Profit'].values]
        parts = ax.violinplot(data, showmeans=True, showmedians=True)
        for pc in parts['bodies']:
            pc.set_facecolor('#D4A5A5')
            pc.set_alpha(0.7)
        ax.set_title('Violin Distribution | توزيع الكمان', fontsize=16, fontweight='bold')
        ax.set_xticks([1, 2])
        ax.set_xticklabels(['Sales', 'Profit'])
        ax.set_ylabel('Value | القيمة', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🥧 SECTION 3: PIE & AREA CHARTS
# ----------------------------
st.markdown("---")
st.header("🥧 القسم 3: الدوائر والمساحات | Section 3: Pie & Area Charts")
st.write("**العربية:** رسوم الدوائر والمساحات")
st.write("**English:** Pie and area charts")

with st.expander("8️⃣ plt.pie() — رسم دائري | Pie chart"):
    st.code("""
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()
    """, language="python")
    st.write("**العربية:** يعرض النسب المئوية في شكل دائري")
    st.write("**English:** Shows percentages in circular format")
    
    if st.button("إظهار | Show", key="8"):
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']
        explode = [0.1] + [0] * (len(df) - 1)
        ax.pie(df['Sales'][:6], labels=df['Month'][:6], autopct='%1.1f%%', 
               colors=colors[:6], explode=explode[:6], shadow=True, startangle=90)
        ax.set_title('Sales Distribution | توزيع المبيعات', fontsize=16, fontweight='bold')
        st.pyplot(fig)
        plt.close()

with st.expander("9️⃣ plt.fill_between() — ملء المساحة | Fill area"):
    st.code("""
plt.fill_between(x, y1, y2, alpha=0.3)
plt.show()
    """, language="python")
    st.write("**العربية:** يملأ المساحة بين منحنيين")
    st.write("**English:** Fills area between curves")
    
    if st.button("إظهار | Show", key="9"):
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

with st.expander("🔟 plt.stackplot() — مساحات مكدسة | Stacked area"):
    st.code("""
plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])
plt.show()
    """, language="python")
    st.write("**العربية:** يكدس عدة مساحات فوق بعضها")
    st.write("**English:** Stacks multiple areas on top of each other")
    
    if st.button("إظهار | Show", key="10"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.stackplot(df.index, df['Profit'], df['Expenses'], df['Growth']*10,
                    labels=['Profit', 'Expenses', 'Growth x10'],
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
st.write("**العربية:** تخصيص الرسوم البيانية")
st.write("**English:** Customize your plots")

with st.expander("1️⃣1️⃣ Colors & Styles — الألوان والأنماط"):
    st.code("""
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o')
plt.show()
    """, language="python")
    st.write("**العربية:** تغيير الألوان، الأنماط، السمك، والعلامات")
    st.write("**English:** Change colors, styles, width, and markers")
    
    col1, col2 = st.columns(2)
    with col1:
        color = st.color_picker("Color | اللون:", "#FF6B6B")
        linestyle = st.selectbox("Line style | نمط الخط:", ['-', '--', '-.', ':'], key="ls1")
    with col2:
        linewidth = st.slider("Width | السمك:", 1, 10, 2)
        marker = st.selectbox("Marker | العلامة:", ['o', 's', '^', 'D', '*', 'x'])
    
    if st.button("إظهار | Show", key="11"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], color=color, linestyle=linestyle, 
               linewidth=linewidth, marker=marker, markersize=10)
        ax.set_title('Custom Plot | رسم مخصص', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index | الفهرس', fontsize=12)
        ax.set_ylabel('Sales | المبيعات', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣2️⃣ plt.title() — العنوان | Title"):
    st.code("""
plt.title('My Chart', fontsize=16, fontweight='bold')
plt.show()
    """, language="python")
    st.write("**العربية:** إضافة عنوان للرسم")
    st.write("**English:** Add title to the plot")
    
    title_text = st.text_input("Title | العنوان:", "My Chart | الرسم البياني")
    title_size = st.slider("Font size | حجم الخط:", 10, 30, 16)
    
    if st.button("إظهار | Show", key="12"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Profit'], marker='o', color='#2E86AB', linewidth=2)
        ax.set_title(title_text, fontsize=title_size, fontweight='bold')
        ax.set_xlabel('Index | الفهرس', fontsize=12)
        ax.set_ylabel('Profit | الأرباح', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣3️⃣ plt.xlabel() & plt.ylabel() — تسميات المحاور | Axis labels"):
    st.code("""
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.show()
    """, language="python")
    st.write("**العربية:** تسمية محاور X و Y")
    st.write("**English:** Label X and Y axes")
    
    xlabel = st.text_input("X label | تسمية X:", "X Axis | المحور الأفقي")
    ylabel = st.text_input("Y label | تسمية Y:", "Y Axis | المحور العمودي")
    
    if st.button("إظهار | Show", key="13"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df['Sales'], df['Profit'], s=100, c=df.index, cmap='viridis', alpha=0.6)
        ax.set_title('Scatter Plot | رسم نقطي', fontsize=16, fontweight='bold')
        ax.set_xlabel(xlabel, fontsize=12)
        ax.set_ylabel(ylabel, fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣4️⃣ plt.legend() — وسيلة الإيضاح | Legend"):
    st.code("""
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend(loc='best')
plt.show()
    """, language="python")
    st.write("**العربية:** إضافة وسيلة إيضاح للتعريف بالخطوط")
    st.write("**English:** Add legend to identify lines")
    
    if st.button("إظهار | Show", key="14"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], label='Sales', marker='o', linewidth=2, color='#E63946')
        ax.plot(df.index, df['Profit'], label='Profit', marker='s', linewidth=2, color='#06A77D')
        ax.plot(df.index, df['Expenses'], label='Expenses', marker='^', linewidth=2, color='#457B9D')
        ax.set_title('Data Comparison | مقارنة البيانات', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index | الفهرس', fontsize=12)
        ax.set_ylabel('Value | القيمة', fontsize=12)
        ax.legend(loc='best', fontsize=11, framealpha=0.9)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣5️⃣ plt.grid() — الشبكة | Grid"):
    st.code("""
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
    """, language="python")
    st.write("**العربية:** إضافة شبكة خلفية")
    st.write("**English:** Add background grid")
    
    grid_style = st.selectbox("Grid style | نمط الشبكة:", ['-', '--', '-.', ':'], key="gs1")
    grid_alpha = st.slider("Grid alpha | شفافية الشبكة:", 0.0, 1.0, 0.3)
    
    if st.button("إظهار | Show", key="15"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['Month'], df['Sales'], color='#A23B72', alpha=0.7)
        ax.set_title('Plot with Grid | رسم مع شبكة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Month | الشهر', fontsize=12)
        ax.set_ylabel('Sales | المبيعات', fontsize=12)
        ax.grid(True, linestyle=grid_style, alpha=grid_alpha)
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📐 SECTION 5: SUBPLOTS & LAYOUTS
# ----------------------------
st.markdown("---")
st.header("📐 القسم 5: الرسوم المتعددة | Section 5: Subplots & Layouts")
st.write("**العربية:** إنشاء عدة رسوم في شكل واحد")
st.write("**English:** Create multiple plots in one figure")

with st.expander("1️⃣6️⃣ plt.subplot() — رسوم فرعية | Multiple plots"):
    st.code("""
plt.subplot(2, 2, 1)  # row, col, position
plt.plot(x, y1)
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.show()
    """, language="python")
    st.write("**العربية:** ينشئ عدة رسوم في شبكة")
    st.write("**English:** Creates multiple plots in a grid")
    
    if st.button("إظهار | Show", key="16"):
        fig = plt.figure(figsize=(14, 10))
        
        ax1 = plt.subplot(2, 2, 1)
        ax1.plot(df.index, df['Sales'], marker='o', color='#FF6B6B', linewidth=2)
        ax1.set_title('Sales | المبيعات', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylabel('Value', fontsize=10)
        
        ax2 = plt.subplot(2, 2, 2)
        ax2.bar(df['Month'], df['Profit'], color='#4ECDC4', alpha=0.7)
        ax2.set_title('Profit | الأرباح', fontsize=13, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(axis='y', alpha=0.3)
        
        ax3 = plt.subplot(2, 2, 3)
        ax3.scatter(df['Sales'], df['Profit'], s=100, c=df.index, cmap='plasma', alpha=0.6)
        ax3.set_title('Sales vs Profit', fontsize=13, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        ax3.set_xlabel('Sales', fontsize=10)
        ax3.set_ylabel('Profit', fontsize=10)
        
        ax4 = plt.subplot(2, 2, 4)
        ax4.pie(df['Expenses'][:5], labels=df['Month'][:5], autopct='%1.1f%%', startangle=90)
        ax4.set_title('Expenses | المصروفات', fontsize=13, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣7️⃣ plt.subplots() — إنشاء محاور متعددة | Create axes"):
    st.code("""
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1)
ax2.plot(x, y2)
plt.show()
    """, language="python")
    st.write("**العربية:** طريقة أكثر مرونة لإنشاء رسوم متعددة")
    st.write("**English:** More flexible way to create multiple plots")
    
    if st.button("إظهار | Show", key="17"):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        ax1.plot(df.index, df['Sales'], marker='o', color='#E63946', linewidth=2, label='Sales')
        ax1.plot(df.index, df['Profit'], marker='s', color='#06A77D', linewidth=2, label='Profit')
        ax1.set_title('Trends | الاتجاهات', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Index', fontsize=11)
        ax1.set_ylabel('Value', fontsize=11)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        x_pos = np.arange(len(df))
        width = 0.35
        ax2.bar(x_pos - width/2, df['Sales'], width, label='Sales', color='#457B9D')
        ax2.bar(x_pos + width/2, df['Expenses'], width, label='Expenses', color='#F1FAEE')
        ax2.set_title('Comparison | المقارنة', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Month', fontsize=11)
        ax2.set_ylabel('Value', fontsize=11)
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(df['Month'], rotation=45)
        ax2.legend()
        ax2.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣8️⃣ plt.tight_layout() — ضبط المسافات | Adjust spacing"):
    st.code("""
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.tight_layout()  # Prevents overlapping
plt.show()
    """, language="python")
    st.write("**العربية:** يضبط المسافات تلقائياً لمنع التداخل")
    st.write("**English:** Automatically adjusts spacing to prevent overlap")
    
    if st.button("إظهار | Show", key="18"):
        fig = plt.figure(figsize=(12, 5))
        
        ax1 = plt.subplot(1, 2, 1)
        ax1.plot(df.index, df['Sales'], marker='o', linewidth=2)
        ax1.set_title('Without tight_layout', fontsize=12)
        ax1.set_xlabel('Very Long X Label That Might Overlap')
        
        ax2 = plt.subplot(1, 2, 2)
        ax2.plot(df.index, df['Profit'], marker='s', linewidth=2, color='green')
        ax2.set_title('With tight_layout', fontsize=12)
        ax2.set_xlabel('Very Long X Label That Fits Well')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📈 SECTION 6: ADVANCED PLOTS
# ----------------------------
st.markdown("---")
st.header("📈 القسم 6: رسوم متقدمة | Section 6: Advanced Plots")
st.write("**العربية:** رسوم بيانية متقدمة واحترافية")
st.write("**English:** Advanced and professional plots")

with st.expander("1️⃣9️⃣ Multiple Lines — خطوط متعددة"):
    st.code("""
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.plot(x, y3, label='Line 3')
plt.show()
    """, language="python")
    st.write("**العربية:** رسم عدة خطوط في نفس الرسم")
    st.write("**English:** Plot multiple lines in the same chart")
    
    if st.button("إظهار | Show", key="19"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#E63946', label='Sales')
        ax.plot(df.index, df['Profit'], marker='s', linewidth=2, color='#06A77D', label='Profit')
        ax.plot(df.index, df['Expenses'], marker='^', linewidth=2, color='#457B9D', label='Expenses')
        ax.plot(df.index, df['Growth']*20, marker='D', linewidth=2, color='#F4A261', label='Growth x20')
        ax.set_title('Multi-line Comparison | مقارنة متعددة الخطوط', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣0️⃣ ax.twinx() — محوران عموديان | Dual Y-axes"):
    st.code("""
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='blue')
ax2 = ax1.twinx()
ax2.plot(x, y2, color='red')
plt.show()
    """, language="python")
    st.write("**العربية:** إنشاء محورين Y لرسم بيانات بمقاييس مختلفة")
    st.write("**English:** Create two Y-axes to plot data with different scales")
    
    if st.button("إظهار | Show", key="20"):
        fig, ax1 = plt.subplots(figsize=(10, 6))
        
        ax1.bar(df['Month'], df['Sales'], color='#FF6B6B', alpha=0.7, label='Sales')
        ax1.set_xlabel('Month', fontsize=12)
        ax1.set_ylabel('Sales', fontsize=12, color='#FF6B6B')
        ax1.tick_params(axis='y', labelcolor='#FF6B6B')
        ax1.tick_params(axis='x', rotation=45)
        
        ax2 = ax1.twinx()
        ax2.plot(df['Month'], df['Growth'], color='#06A77D', marker='o', linewidth=3, label='Growth %')
        ax2.set_ylabel('Growth %', fontsize=12, color='#06A77D')
        ax2.tick_params(axis='y', labelcolor='#06A77D')
        
        ax1.set_title('Dual Axis Plot | رسم بمحورين', fontsize=16, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣1️⃣ Grouped Bar Chart — أعمدة مجمعة | Grouped bars"):
    st.code("""
x = np.arange(len(categories))
width = 0.35
plt.bar(x - width/2, values1, width, label='Group 1')
plt.bar(x + width/2, values2, width, label='Group 2')
plt.show()
    """, language="python")
    st.write("**العربية:** رسم أعمدة مجمعة للمقارنة")
    st.write("**English:** Plot grouped bars for comparison")
    
    if st.button("إظهار | Show", key="21"):
        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(df))
        width = 0.25
        
        ax.bar(x - width, df['Sales'], width, label='Sales', color='#E63946')
        ax.bar(x, df['Profit'], width, label='Profit', color='#06A77D')
        ax.bar(x + width, df['Expenses'], width, label='Expenses', color='#457B9D')
        
        ax.set_title('Grouped Bar Chart | رسم أعمدة مجمعة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(df['Month'], rotation=45)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣2️⃣ Stacked Bar Chart — أعمدة مكدسة | Stacked bars"):
    st.code("""
plt.bar(x, values1, label='Part 1')
plt.bar(x, values2, bottom=values1, label='Part 2')
plt.show()
    """, language="python")
    st.write("**العربية:** رسم أعمدة مكدسة فوق بعضها")
    st.write("**English:** Plot stacked bars on top of each other")
    
    if st.button("إظهار | Show", key="22"):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.bar(df['Month'], df['Profit'], label='Profit', color='#06A77D', alpha=0.8)
        ax.bar(df['Month'], df['Expenses'], bottom=df['Profit'], 
               label='Expenses', color='#E63946', alpha=0.8)
        
        ax.set_title('Stacked Bar Chart | رسم أعمدة مكدسة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Month', fontsize=12)
        ax.set_ylabel('Total Value', fontsize=12)
        ax.legend()
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🎯 SECTION 7: ANNOTATIONS & TEXT
# ----------------------------
st.markdown("---")
st.header("🎯 القسم 7: التعليقات والنصوص | Section 7: Annotations & Text")
st.write("**العربية:** إضافة نصوص وتعليقات للرسوم")
st.write("**English:** Add text and annotations to plots")

with st.expander("2️⃣3️⃣ plt.text() — إضافة نص | Add text"):
    st.code("""
plt.plot(x, y)
plt.text(x_pos, y_pos, 'Text here', fontsize=12)
plt.show()
    """, language="python")
    st.write("**العربية:** يضيف نص في موقع محدد")
    st.write("**English:** Adds text at a specific location")
    
    if st.button("إظهار | Show", key="23"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#2E86AB')
        
        max_idx = df['Sales'].idxmax()
        max_val = df['Sales'].max()
        ax.text(max_idx, max_val + 20, f'Peak: {max_val}', 
                fontsize=12, ha='center', color='red', fontweight='bold')
        
        ax.set_title('Plot with Text | رسم مع نص', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Sales', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣4️⃣ plt.annotate() — سهم تعليق | Annotation arrow"):
    st.code("""
plt.annotate('Important point', xy=(x, y), 
             xytext=(x+1, y+10),
             arrowprops=dict(arrowstyle='->'))
plt.show()
    """, language="python")
    st.write("**العربية:** يضيف تعليق مع سهم يشير إلى نقطة")
    st.write("**English:** Adds annotation with arrow pointing to a point")
    
    if st.button("إظهار | Show", key="24"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Profit'], marker='o', linewidth=2, color='#06A77D')
        
        max_idx = df['Profit'].idxmax()
        max_val = df['Profit'].max()
        ax.annotate(f'Maximum\n{max_val}', 
                   xy=(max_idx, max_val), 
                   xytext=(max_idx-2, max_val+40),
                   fontsize=12, fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color='red', lw=2),
                   bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7))
        
        ax.set_title('Annotation Example | مثال على التعليق', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Profit', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣5️⃣ plt.axhline() & plt.axvline() — خطوط مرجعية | Reference lines"):
    st.code("""
plt.plot(x, y)
plt.axhline(y=50, color='r', linestyle='--', label='Threshold')
plt.axvline(x=5, color='g', linestyle=':', label='Target')
plt.show()
    """, language="python")
    st.write("**العربية:** يضيف خطوط أفقية وعمودية مرجعية")
    st.write("**English:** Adds horizontal and vertical reference lines")
    
    if st.button("إظهار | Show", key="25"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#2E86AB', label='Sales')
        
        avg_sales = df['Sales'].mean()
        ax.axhline(y=avg_sales, color='red', linestyle='--', linewidth=2, label=f'Average: {avg_sales:.0f}')
        ax.axvline(x=5, color='green', linestyle=':', linewidth=2, label='Mid Point')
        
        ax.set_title('Reference Lines | الخطوط المرجعية', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Sales', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣6️⃣ plt.axhspan() & plt.axvspan() — مناطق ملونة | Colored regions"):
    st.code("""
plt.plot(x, y)
plt.axhspan(ymin, ymax, alpha=0.3, color='red')
plt.axvspan(xmin, xmax, alpha=0.3, color='blue')
plt.show()
    """, language="python")
    st.write("**العربية:** يلون مناطق معينة في الرسم")
    st.write("**English:** Colors specific regions in the plot")
    
    if st.button("إظهار | Show", key="26"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Profit'], marker='o', linewidth=2, color='#2E86AB', label='Profit')
        
        # Highlight profitable region
        ax.axhspan(150, df['Profit'].max()+50, alpha=0.2, color='green', label='High Profit Zone')
        ax.axhspan(0, 100, alpha=0.2, color='red', label='Low Profit Zone')
        ax.axvspan(4, 7, alpha=0.1, color='yellow', label='Peak Season')
        
        ax.set_title('Highlighted Regions | المناطق المميزة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Profit', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🌈 SECTION 8: COLORS & COLORMAPS
# ----------------------------
st.markdown("---")
st.header("🌈 القسم 8: الألوان والخرائط اللونية | Section 8: Colors & Colormaps")
st.write("**العربية:** العمل مع الألوان والخرائط اللونية")
st.write("**English:** Working with colors and colormaps")

with st.expander("2️⃣7️⃣ Colormaps — خرائط لونية | Color gradients"):
    st.code("""
plt.scatter(x, y, c=values, cmap='viridis')
plt.colorbar()
plt.show()
    """, language="python")
    st.write("**العربية:** استخدام خرائط لونية متدرجة")
    st.write("**English:** Using color gradient maps")
    
    cmap_choice = st.selectbox("اختر خريطة لونية | Choose colormap:", 
                               ['viridis', 'plasma', 'inferno', 'magma', 'coolwarm', 'rainbow', 'jet'])
    
    if st.button("إظهار | Show", key="27"):
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df['Sales'], df['Profit'], s=df['Expenses']*2, 
                           c=df['Growth'], cmap=cmap_choice, alpha=0.7, edgecolors='black', linewidth=1.5)
        ax.set_title(f'Colormap: {cmap_choice} | خريطة لونية', fontsize=16, fontweight='bold')
        ax.set_xlabel('Sales', fontsize=12)
        ax.set_ylabel('Profit', fontsize=12)
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Growth %', fontsize=11)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣8️⃣ Color Names — أسماء الألوان | Named colors"):
    st.code("""
plt.plot(x, y1, color='crimson')
plt.plot(x, y2, color='dodgerblue')
plt.plot(x, y3, color='forestgreen')
plt.show()
    """, language="python")
    st.write("**العربية:** استخدام أسماء الألوان المعرفة")
    st.write("**English:** Using predefined color names")
    
    if st.button("إظهار | Show", key="28"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], color='crimson', linewidth=2, marker='o', label='Sales')
        ax.plot(df.index, df['Profit'], color='dodgerblue', linewidth=2, marker='s', label='Profit')
        ax.plot(df.index, df['Expenses'], color='forestgreen', linewidth=2, marker='^', label='Expenses')
        ax.plot(df.index, df['Growth']*20, color='gold', linewidth=2, marker='D', label='Growth x20')
        ax.set_title('Named Colors | ألوان مسماة', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣9️⃣ Hex Colors — ألوان سداسية عشرية | Hex colors"):
    st.code("""
plt.plot(x, y, color='#FF6B6B')  # Hex color code
plt.show()
    """, language="python")
    st.write("**العربية:** استخدام رموز الألوان السداسية عشرية")
    st.write("**English:** Using hexadecimal color codes")
    
    if st.button("إظهار | Show", key="29"):
        fig, ax = plt.subplots(figsize=(10, 6))
        colors_hex = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        
        for i, col in enumerate(df.columns[1:5]):
            ax.plot(df.index, df[col], color=colors_hex[i], 
                   linewidth=2, marker='o', label=col)
        
        ax.set_title('Hex Colors | ألوان Hex', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📊 SECTION 9: SPECIAL PLOTS
# ----------------------------
st.markdown("---")
st.header("📊 القسم 9: رسوم خاصة | Section 9: Special Plots")
st.write("**العربية:** رسوم بيانية متخصصة")
st.write("**English:** Specialized plots")

with st.expander("3️⃣0️⃣ plt.errorbar() — أعمدة الخطأ | Error bars"):
    st.code("""
plt.errorbar(x, y, yerr=errors, fmt='o')
plt.show()
    """, language="python")
    st.write("**العربية:** يضيف أعمدة تمثل هامش الخطأ")
    st.write("**English:** Adds bars representing error margins")
    
    if st.button("إظهار | Show", key="30"):
        fig, ax = plt.subplots(figsize=(10, 6))
        errors = df['Sales'] * 0.1  # 10% error
        ax.errorbar(df.index, df['Sales'], yerr=errors, fmt='o', 
                   linewidth=2, markersize=8, capsize=5, capthick=2,
                   color='#2E86AB', ecolor='#E63946', label='Sales ± 10%')
        ax.set_title('Error Bars | أعمدة الخطأ', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Sales', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("3️⃣1️⃣ plt.stem() — رسم عصوي | Stem plot"):
    st.code("""
plt.stem(x, y)
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم خطوط عمودية من المحور إلى النقاط")
    st.write("**English:** Draws vertical lines from axis to points")
    
    if st.button("إظهار | Show", key="31"):
        fig, ax = plt.subplots(figsize=(10, 6))
        markerline, stemlines, baseline = ax.stem(df.index, df['Growth'], 
                                                   linefmt='#2E86AB', markerfmt='o',
                                                   basefmt='k-')
        markerline.set_markerfacecolor('#E63946')
        markerline.set_markersize(10)
        stemlines.set_linewidth(2)
        ax.set_title('Stem Plot | رسم عصوي', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Growth %', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("3️⃣2️⃣ plt.step() — رسم درجي | Step plot"):
    st.code("""
plt.step(x, y, where='mid')
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم خطاً درجياً (سلمياً)")
    st.write("**English:** Draws a step-like (staircase) line")
    
    if st.button("إظهار | Show", key="32"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.step(df.index, df['Sales'], where='mid', linewidth=2, color='#2E86AB', label='Sales')
        ax.step(df.index, df['Profit'], where='mid', linewidth=2, color='#06A77D', label='Profit')
        ax.set_title('Step Plot | رسم درجي', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("3️⃣3️⃣ Heatmap — خريطة حرارية | Heat map"):
    st.code("""
plt.imshow(data, cmap='hot', aspect='auto')
plt.colorbar()
plt.show()
    """, language="python")
    st.write("**العربية:** يعرض البيانات كخريطة حرارية ملونة")
    st.write("**English:** Displays data as a colored heat map")
    
    if st.button("إظهار | Show", key="33"):
        fig, ax = plt.subplots(figsize=(10, 8))
        # Create correlation matrix
        data_matrix = df[['Sales', 'Profit', 'Expenses', 'Growth']].T.values
        im = ax.imshow(data_matrix, cmap='RdYlGn', aspect='auto')
        
        ax.set_xticks(np.arange(len(df)))
        ax.set_yticks(np.arange(len(['Sales', 'Profit', 'Expenses', 'Growth'])))
        ax.set_xticklabels(df['Month'], rotation=45)
        ax.set_yticklabels(['Sales', 'Profit', 'Expenses', 'Growth'])
        
        plt.colorbar(im, ax=ax, label='Value')
        ax.set_title('Heatmap | خريطة حرارية', fontsize=16, fontweight='bold')
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🎭 SECTION 10: STYLES & THEMES
# ----------------------------
st.markdown("---")
st.header("🎭 القسم 10: الأنماط والثيمات | Section 10: Styles & Themes")
st.write("**العربية:** تطبيق أنماط جاهزة على الرسوم")
st.write("**English:** Apply pre-made styles to plots")

with st.expander("3️⃣4️⃣ plt.style.use() — تطبيق نمط | Apply style"):
    st.code("""
plt.style.use('ggplot')
plt.plot(x, y)
plt.show()
    """, language="python")
    st.write("**العربية:** يطبق نمط تصميم جاهز")
    st.write("**English:** Applies a pre-made design style")
    
    style_choice = st.selectbox("اختر نمط | Choose style:", 
                               ['default', 'ggplot', 'seaborn', 'bmh', 'fivethirtyeight', 'dark_background'])
    
    if st.button("إظهار | Show", key="34"):
        with plt.style.context(style_choice):
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df.index, df['Sales'], marker='o', linewidth=2, label='Sales')
            ax.plot(df.index, df['Profit'], marker='s', linewidth=2, label='Profit')
            ax.set_title(f'Style: {style_choice} | نمط', fontsize=16, fontweight='bold')
            ax.set_xlabel('Index', fontsize=12)
            ax.set_ylabel('Value', fontsize=12)
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
            plt.close()

# ----------------------------
# 🔧 SECTION 11: FIGURE & AXES PROPERTIES
# ----------------------------
st.markdown("---")
st.header("🔧 القسم 11: خصائص الشكل والمحاور | Section 11: Figure & Axes Properties")
st.write("**العربية:** التحكم في خصائص الشكل والمحاور")
st.write("**English:** Control figure and axes properties")

with st.expander("3️⃣5️⃣ fig.savefig() — حفظ الرسم | Save figure"):
    st.code("""
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig('myplot.png', dpi=300, bbox_inches='tight')
    """, language="python")
    st.write("**العربية:** يحفظ الرسم كملف صورة")
    st.write("**English:** Saves the plot as an image file")
    
    if st.button("إنشاء وتنزيل | Create & Download", key="35"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#2E86AB')
        ax.set_title('Sales Chart | رسم المبيعات', fontsize=16, fontweight='bold')
        ax.set_xlabel('Index', fontsize=12)
        ax.set_ylabel('Sales', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Save to buffer
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        buf.seek(0)
        
        st.pyplot(fig)
        st.download_button(
            label="⬇️ تحميل الصورة | Download PNG",
            data=buf,
            file_name="matplotlib_chart.png",
            mime="image/png"
        )
        plt.close()

with st.expander("3️
