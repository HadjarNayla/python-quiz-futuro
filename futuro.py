# 🎓 STREAMLIT APP — Learn Pandas from 0️⃣ to 🦸 Hero
# ---------------------------------------------------
# 🧠 Goal:
# Teach beginners how to explore, clean, and analyze datasets using Pandas interactively.
# Dataset used: Football Players Dataset (2015–2024)
# ---------------------------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 🏁 App Title
st.title("🐼 Pandas From 0️⃣ to Hero — Interactive Learning App")
st.write("""
Welcome! 👋  
This app helps you **learn Pandas** step-by-step using a real dataset.
We’ll explore, clean, and analyze football player data together ⚽.
""")

# 📂 Step 1 — Upload or Use Example Dataset
st.header("📂 Step 1: Load Dataset")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    st.info("No file uploaded — using example football dataset.")
    data = {
        'Player_Name': ['Messi', 'Mbappé', 'Salah', 'Ronaldo', 'De Bruyne', 'Haaland', 'Benzema', 'Neymar'],
        'Club': ['PSG', 'PSG', 'Liverpool', 'Al Nassr', 'Man City', 'Man City', 'Real Madrid', 'Al Hilal'],
        'Goals': [25, 28, 20, 30, 12, 27, 22, 18],
        'Assists': [15, 12, 9, 8, 18, 6, 10, 11],
        'Rating': [9.5, 9.3, 8.8, 9.0, 9.2, 9.1, 8.9, 9.0],
        'Matches': [30, 32, 29, 31, 30, 28, 30, 27]
    }
    df = pd.DataFrame(data)

# Display Data
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# 🔍 Step 2 — Explore the Dataset
st.header("🔍 Step 2: Explore Basic Info")
if st.checkbox("Show Data Info"):
    buffer = []
    df.info(buf=buffer)
    info_str = "\n".join(buffer)
    st.text(info_str)

if st.checkbox("Show Summary Statistics"):
    st.write(df.describe())

if st.checkbox("Show Missing Values"):
    st.write(df.isnull().sum())

# 🧹 Step 3 — Clean the Data
st.header("🧹 Step 3: Data Cleaning")
if st.button("Clean Missing Data"):
    df.fillna({
        'Goals': df['Goals'].mean(),
        'Assists': df['Assists'].mean(),
        'Rating': df['Rating'].mean(),
        'Matches': df['Matches'].median()
    }, inplace=True)
    st.success("✅ Missing data cleaned!")

st.write("Cleaned Data:")
st.dataframe(df.head())

# ⚙️ Step 4 — Create New Columns
st.header("⚙️ Step 4: Create New Columns")
if st.button("Add Goal_Contribution & Efficiency"):
    df['Goal_Contribution'] = df['Goals'] + df['Assists']
    df['Goals_per_Match'] = (df['Goals'] / df['Matches']).round(2)
    df['Efficiency'] = (df['Goals_per_Match'] * df['Rating']).round(2)
    st.success("🆕 Columns added successfully!")
    st.dataframe(df.head())

# 📈 Step 5 — Visualize
st.header("📈 Step 5: Data Visualization")

chart_type = st.selectbox("Choose a chart to visualize:", [
    "Top Players by Goals",
    "Top Players by Rating",
    "Relationship: Goals vs Rating",
    "Goals per Club"
])

if chart_type == "Top Players by Goals":
    top_goals = df.sort_values(by='Goals', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.bar(top_goals['Player_Name'], top_goals['Goals'], color='green')
    ax.set_title("⚽ Top 10 Players by Goals")
    ax.set_ylabel("Goals")
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif chart_type == "Top Players by Rating":
    top_ratings = df.sort_values(by='Rating', ascending=False).head(10)
    fig, ax = plt.subplots()
    ax.barh(top_ratings['Player_Name'], top_ratings['Rating'], color='orange')
    ax.set_title("🌟 Top 10 Players by Rating")
    st.pyplot(fig)

elif chart_type == "Relationship: Goals vs Rating":
    fig, ax = plt.subplots()
    ax.scatter(df['Goals'], df['Rating'], color='purple')
    ax.set_title("⚽ Relationship: Goals vs Rating")
    ax.set_xlabel("Goals")
    ax.set_ylabel("Rating")
    st.pyplot(fig)

elif chart_type == "Goals per Club":
    club_goals = df.groupby('Club')['Goals'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.bar(club_goals.index, club_goals.values, color='skyblue')
    ax.set_title("🏆 Average Goals per Club")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 🧩 Step 6 — Student Challenges
st.header("🧩 Step 6: Try it Yourself!")
st.markdown("""
🎯 **Mini Exercises:**
1️⃣ Show only players with more than 20 goals.  
2️⃣ Show players with rating above 9.  
3️⃣ Find average goals per club.  
4️⃣ Create a new column: `Performance_Level` based on Rating  
   - Rating ≥ 9 → Elite  
   - Rating ≥ 8 → Excellent  
   - Rating ≥ 7 → Good  
   - Else → Average  
""")

if st.button("Show Solutions 💡"):
    df['Performance_Level'] = df['Rating'].apply(
        lambda r: 'Elite' if r >= 9 else 'Excellent' if r >= 8 else 'Good'
    )
    st.dataframe(df[['Player_Name', 'Rating', 'Performance_Level']])

# 💾 Step 7 — Save Results
st.header("💾 Step 7: Save Your Work")
if st.button("Download Clean Data"):
    df.to_csv("clean_football_dataset.csv", index=False)
    st.success("✅ File saved as 'clean_football_dataset.csv'")

# 🏁 End Message
st.success("🎉 Congratulations! You’ve learned Pandas basics interactively 🐼🔥")
