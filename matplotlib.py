import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import io

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

# Important note about filename
st.warning("⚠️ **مهم جداً | VERY IMPORTANT:** عند حفظ هذا الملف، لا تسميه `matplotlib.py` - استخدم اسم مثل `matplotlib_app.py` أو `viz_app.py` | When saving this file, do NOT name it `matplotlib.py` - use a name like `matplotlib_app.py` or `viz_app.py`")

# ----------------------------
# 📂 OPTIONAL: UPLOAD DATASET
# ----------------------------
st.header("📁 الخطوة 1 (اختياري): تحميل ملف CSV | Step 1 (Optional): Upload a CSV file")
st.write("**العربية:** يمكنك تحميل بياناتك الخاصة أو استخدام بيانات عشوائية")
st.write("**English:** You can upload your own data or use random sample data")

uploaded_file = st.file_uploader("ارفع ملف CSV (اختياري) | Upload a CSV file (optional)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ تم تحميل البيانات بنجاح! | Dataset loaded successfully!")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"فشل قراءة الملف | Failed to read CSV: {e}")
        df = None
else:
    # Generate sample data
    np.random.seed(42)
    df = pd.DataFrame({
        'Month': ['يناير|Jan', 'فبراير|Feb', 'مارس|Mar', 'أبريل|Apr', 'مايو|May', 'يونيو|Jun'],
        'Sales': np.random.randint(100, 500, 6),
        'Profit': np.random.randint(50, 200, 6),
        'Expenses': np.random.randint(80, 300, 6)
    })
    st.info("💡 يتم استخدام بيانات عشوائية | Using sample data")
    st.dataframe(df.head())

# ----------------------------
# 📘 SECTION 1: BASIC PLOTTING
# القسم 1: الرسم الأساسي
# ----------------------------
st.markdown("---")
st.header("📘 القسم 1: الرسم الأساسي | Section 1: Basic Plotting")
st.write("**العربية:** تعلم كيفية إنشاء الرسوم البيانية الأساسية")
st.write("**English:** Learn how to create basic plots")

with st.expander("1️⃣ plt.plot() — رسم خطي | Line plot"):
    st.code("""
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم خط بين نقاط البيانات")
    st.write("**English:** Draws a line connecting data points")
    
    if st.button("إظهار الرسم | Show Plot", key="plot1"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], marker='o', linewidth=2, color='#2E86AB')
        ax.set_title('المبيعات عبر الأشهر | Sales Across Months', fontsize=16, fontweight='bold')
        ax.set_xlabel('الشهر | Month', fontsize=12)
        ax.set_ylabel('المبيعات | Sales', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("2️⃣ plt.scatter() — رسم نقطي | Scatter plot"):
    st.code("""
plt.scatter(x, y, s=size, c=color, alpha=0.5)
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم نقاط منفصلة في الفضاء ثنائي الأبعاد")
    st.write("**English:** Plots individual points in 2D space")
    
    if st.button("إظهار الرسم | Show Plot", key="plot2"):
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df['Sales'], df['Profit'], 
                           s=df['Expenses'], 
                           c=df.index, 
                           cmap='viridis', 
                           alpha=0.6,
                           edgecolors='black')
        ax.set_title('العلاقة بين المبيعات والأرباح | Sales vs Profit', fontsize=16, fontweight='bold')
        ax.set_xlabel('المبيعات | Sales', fontsize=12)
        ax.set_ylabel('الأرباح | Profit', fontsize=12)
        plt.colorbar(scatter, ax=ax, label='الفهرس | Index')
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot3"):
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(df['Month'], df['Sales'], color='#A23B72', edgecolor='black', alpha=0.7)
        ax.set_title('المبيعات حسب الشهر | Sales by Month', fontsize=16, fontweight='bold')
        ax.set_xlabel('الشهر | Month', fontsize=12)
        ax.set_ylabel('المبيعات | Sales', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("4️⃣ plt.barh() — أعمدة أفقية | Horizontal bar chart"):
    st.code("""
plt.barh(categories, values)
plt.show()
    """, language="python")
    st.write("**العربية:** يرسم أعمدة أفقية")
    st.write("**English:** Draws horizontal bars")
    
    if st.button("إظهار الرسم | Show Plot", key="plot4"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(df['Month'], df['Profit'], color='#F18F01', edgecolor='black', alpha=0.7)
        ax.set_title('الأرباح حسب الشهر | Profit by Month', fontsize=16, fontweight='bold')
        ax.set_xlabel('الأرباح | Profit', fontsize=12)
        ax.set_ylabel('الشهر | Month', fontsize=12)
        ax.grid(axis='x', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📊 SECTION 2: STATISTICAL PLOTS
# القسم 2: الرسوم الإحصائية
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot5"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = np.random.normal(100, 15, 1000)
        ax.hist(data, bins=30, color='#06A77D', edgecolor='black', alpha=0.7)
        ax.set_title('توزيع البيانات | Data Distribution', fontsize=16, fontweight='bold')
        ax.set_xlabel('القيمة | Value', fontsize=12)
        ax.set_ylabel('التكرار | Frequency', fontsize=12)
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot6"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = [df['Sales'], df['Profit'], df['Expenses']]
        box = ax.boxplot(data, labels=['المبيعات|Sales', 'الأرباح|Profit', 'المصروفات|Expenses'],
                        patch_artist=True, notch=True)
        for patch, color in zip(box['boxes'], ['#E63946', '#F1FAEE', '#A8DADC']):
            patch.set_facecolor(color)
        ax.set_title('مقارنة إحصائية | Statistical Comparison', fontsize=16, fontweight='bold')
        ax.set_ylabel('القيمة | Value', fontsize=12)
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot7"):
        fig, ax = plt.subplots(figsize=(10, 6))
        data = [df['Sales'].values, df['Profit'].values]
        parts = ax.violinplot(data, showmeans=True, showmedians=True)
        for pc in parts['bodies']:
            pc.set_facecolor('#D4A5A5')
            pc.set_alpha(0.7)
        ax.set_title('توزيع الكمان | Violin Distribution', fontsize=16, fontweight='bold')
        ax.set_xticks([1, 2])
        ax.set_xticklabels(['المبيعات|Sales', 'الأرباح|Profit'])
        ax.set_ylabel('القيمة | Value', fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🥧 SECTION 3: PIE & AREA CHARTS
# القسم 3: الدوائر والمساحات
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot8"):
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        explode = (0.1, 0, 0, 0, 0, 0)[:len(df)]
        ax.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', 
               colors=colors, explode=explode, shadow=True, startangle=90)
        ax.set_title('توزيع المبيعات | Sales Distribution', fontsize=16, fontweight='bold')
        st.pyplot(fig)
        plt.close()

with st.expander("9️⃣ plt.fill_between() — ملء المساحة | Fill area"):
    st.code("""
plt.fill_between(x, y1, y2, alpha=0.3)
plt.show()
    """, language="python")
    st.write("**العربية:** يملأ المساحة بين منحنيين")
    st.write("**English:** Fills area between two curves")
    
    if st.button("إظهار الرسم | Show Plot", key="plot9"):
        fig, ax = plt.subplots(figsize=(10, 6))
        x = df.index
        ax.plot(x, df['Sales'], label='المبيعات|Sales', color='#2E86AB', linewidth=2)
        ax.plot(x, df['Expenses'], label='المصروفات|Expenses', color='#E63946', linewidth=2)
        ax.fill_between(x, df['Sales'], df['Expenses'], 
                        where=(df['Sales'] >= df['Expenses']), 
                        interpolate=True, alpha=0.3, color='green', label='ربح|Profit')
        ax.fill_between(x, df['Sales'], df['Expenses'], 
                        where=(df['Sales'] < df['Expenses']), 
                        interpolate=True, alpha=0.3, color='red', label='خسارة|Loss')
        ax.set_title('المساحة بين المبيعات والمصروفات | Area Between Sales & Expenses', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('الفهرس | Index', fontsize=12)
        ax.set_ylabel('القيمة | Value', fontsize=12)
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot10"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.stackplot(df.index, df['Sales'], df['Profit'], df['Expenses'],
                    labels=['المبيعات|Sales', 'الأرباح|Profit', 'المصروفات|Expenses'],
                    colors=['#FF6B6B', '#4ECDC4', '#FFA07A'], alpha=0.8)
        ax.set_title('المساحات المكدسة | Stacked Areas', fontsize=16, fontweight='bold')
        ax.set_xlabel('الفهرس | Index', fontsize=12)
        ax.set_ylabel('القيمة | Value', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 🎨 SECTION 4: CUSTOMIZATION
# القسم 4: التخصيص
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
        color = st.color_picker("اختر اللون | Pick color:", "#FF6B6B")
        linestyle = st.selectbox("نمط الخط | Line style:", ['-', '--', '-.', ':'])
    with col2:
        linewidth = st.slider("سمك الخط | Line width:", 1, 10, 2)
        marker = st.selectbox("العلامة | Marker:", ['o', 's', '^', 'D', '*', 'x'])
    
    if st.button("إظهار الرسم | Show Plot", key="plot11"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], color=color, linestyle=linestyle, 
               linewidth=linewidth, marker=marker, markersize=10)
        ax.set_title('رسم مخصص | Custom Plot', fontsize=16, fontweight='bold')
        ax.set_xlabel('الفهرس | Index', fontsize=12)
        ax.set_ylabel('المبيعات | Sales', fontsize=12)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣2️⃣ plt.title() — العنوان | Title"):
    st.code("""
plt.title('My Chart', fontsize=16, fontweight='bold', color='blue')
plt.show()
    """, language="python")
    st.write("**العربية:** إضافة عنوان للرسم")
    st.write("**English:** Add title to the plot")
    
    title_text = st.text_input("النص | Title text:", "الرسم البياني | My Chart")
    title_size = st.slider("حجم الخط | Font size:", 10, 30, 16)
    
    if st.button("إظهار الرسم | Show Plot", key="plot12"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Profit'], marker='o', color='#2E86AB', linewidth=2)
        ax.set_title(title_text, fontsize=title_size, fontweight='bold')
        ax.set_xlabel('الفهرس | Index', fontsize=12)
        ax.set_ylabel('الأرباح | Profit', fontsize=12)
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
    
    xlabel = st.text_input("تسمية X | X label:", "المحور الأفقي | X Axis")
    ylabel = st.text_input("تسمية Y | Y label:", "المحور العمودي | Y Axis")
    
    if st.button("إظهار الرسم | Show Plot", key="plot13"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df['Sales'], df['Profit'], s=100, c=df.index, cmap='viridis', alpha=0.6)
        ax.set_title('رسم نقطي | Scatter Plot', fontsize=16, fontweight='bold')
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
    
    if st.button("إظهار الرسم | Show Plot", key="plot14"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df.index, df['Sales'], label='المبيعات | Sales', marker='o', linewidth=2)
        ax.plot(df.index, df['Profit'], label='الأرباح | Profit', marker='s', linewidth=2)
        ax.plot(df.index, df['Expenses'], label='المصروفات | Expenses', marker='^', linewidth=2)
        ax.set_title('مقارنة البيانات | Data Comparison', fontsize=16, fontweight='bold')
        ax.set_xlabel('الفهرس | Index', fontsize=12)
        ax.set_ylabel('القيمة | Value', fontsize=12)
        ax.legend(loc='best', fontsize=10)
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
    
    grid_style = st.selectbox("نمط الشبكة | Grid style:", ['-', '--', '-.', ':'], key="grid_style")
    grid_alpha = st.slider("شفافية الشبكة | Grid alpha:", 0.0, 1.0, 0.3)
    
    if st.button("إظهار الرسم | Show Plot", key="plot15"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['Month'], df['Sales'], color='#A23B72', alpha=0.7)
        ax.set_title('رسم مع شبكة | Plot with Grid', fontsize=16, fontweight='bold')
        ax.set_xlabel('الشهر | Month', fontsize=12)
        ax.set_ylabel('المبيعات | Sales', fontsize=12)
        ax.grid(True, linestyle=grid_style, alpha=grid_alpha)
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
        plt.close()

# ----------------------------
# 📐 SECTION 5: SUBPLOTS & LAYOUTS
# القسم 5: الرسوم المتعددة
# ----------------------------
st.markdown("---")
st.header("📐 القسم 5: الرسوم المتعددة | Section 5: Subplots & Layouts")
st.write("**العربية:** إنشاء عدة رسوم في شكل واحد")
st.write("**English:** Create multiple plots in one figure")

with st.expander("1️⃣6️⃣ plt.subplot() — رسوم فرعية | Subplots"):
    st.code("""
plt.subplot(2, 2, 1)  # 2 rows, 2 cols, position 1
plt.plot(x, y1)
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.show()
    """, language="python")
    st.write("**العربية:** ينشئ عدة رسوم في شبكة")
    st.write("**English:** Creates multiple plots in a grid")
    
    if st.button("إظهار الرسم | Show Plot", key="plot16"):
        fig = plt.figure(figsize=(12, 10))
        
        # Plot 1
        ax1 = plt.subplot(2, 2, 1)
        ax1.plot(df.index, df['Sales'], marker='o', color='#FF6B6B', linewidth=2)
        ax1.set_title('المبيعات | Sales', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2
        ax2 = plt.subplot(2, 2, 2)
        ax2.bar(df['Month'], df['Profit'], color='#4ECDC4', alpha=0.7)
        ax2.set_title('الأرباح | Profit', fontsize=12, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        ax2.grid(axis='y', alpha=0.3)
        
        # Plot 3
        ax3 = plt.subplot(2, 2, 3)
        ax3.scatter(df['Sales'], df['Profit'], s=100, c=df.index, cmap='viridis', alpha=0.6)
        ax3.set_title('المبيعات مقابل الأرباح | Sales vs Profit', fontsize=12, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4
        ax4 = plt.subplot(2, 2, 4)
        ax4.pie(df['Expenses'], labels=df['Month'], autopct='%1.1f%%', startangle=90)
        ax4.set_title('توزيع المصروفات | Expenses Distribution', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

with st.expander("1️⃣7️⃣ plt.subplots() — إنشاء محاور متعددة | Create multiple axes"):
    st.code("""
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1)
ax2.plot(x, y2)
plt.show()
    """, language="python")
    st.write("**العربية:** طريقة أكثر مرونة لإنشاء رسوم متعددة")
    st.write("**English:** More flexible way to create multiple plots")
    
    if st.button("إظهار الرسم | Show Plot", key="plot17"):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Left plot
        ax1.plot(df.index, df['Sales'], marker='o', color='#E63946', linewidth=2, label='المبيعات|Sales')
        ax1.plot(df.index, df['Profit'], marker='s', color='#06A77D', linewidth=2, label='الأرباح|Profit')
        ax1.set_title('اتجاهات المبيعات والأرباح | Sales & Profit Trends', fontsize=14, fontweight='bold')
        ax1.set_xlabel('الفهرس | Index', fontsize=11)
        ax1.set_ylabel('القيمة | Value', fontsize=11)
        ax1.legend()
        ax1.grid(True, alpha=0.
