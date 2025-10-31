# 🐼 PANDAS TUTORIAL FOR BEGINNERS — FOOTBALL DATASET (2015–2024)
# ---------------------------------------------------------------
# 🎯 Goal:
# Learn how to use Pandas for data loading, exploration, cleaning,
# analysis, and saving results — using a real Football dataset.
# ---------------------------------------------------------------

# Step 1️⃣: Import Pandas
import pandas as pd

# Step 2️⃣: Load the Dataset
# (Make sure the file 'football_players.csv' is in your working directory)
df = pd.read_csv("football_players.csv")

# Step 3️⃣: First Look at the Data
print("✅ First 5 rows of the dataset:\n", df.head())
print("\n📏 Shape of dataset (rows, columns):", df.shape)
print("\n📋 Columns available:\n", df.columns.tolist())

# Step 4️⃣: Basic Info
print("\nℹ️ Dataset Info:")
print(df.info())
print("\n📈 Numeric Summary:")
print(df.describe())

# Step 5️⃣: Check Missing Values
print("\n❓ Missing values in each column:\n", df.isnull().sum())

# Step 6️⃣: Clean the Data
# Replace missing numeric values with mean and text with 'Unknown'
df['Goals'].fillna(df['Goals'].mean(), inplace=True)
df['Assists'].fillna(df['Assists'].mean(), inplace=True)
df['Rating'].fillna(df['Rating'].mean(), inplace=True)
df['Matches'].fillna(df['Matches'].median(), inplace=True)
df['Player_Name'].fillna('Unknown', inplace=True)
df['Club'].fillna('Unknown', inplace=True)
print("\n🧹 Cleaned all missing values!")

# Step 7️⃣: View Clean Data
print("\n✅ Sample of Clean Data:")
print(df.head())

# Step 8️⃣: Simple Selection
print("\n🎯 Select Player Names and Clubs:")
print(df[['Player_Name', 'Club']].head())

print("\n⚽ Top 5 Players by Goals:")
print(df[['Player_Name', 'Goals']].sort_values(by='Goals', ascending=False).head())

# Step 9️⃣: Filtering Data
print("\n🔥 Players who scored more than 20 goals:")
print(df[df['Goals'] > 20][['Player_Name', 'Goals', 'Club']])

print("\n⭐ Players with Rating above 9.0:")
print(df[df['Rating'] > 9.0][['Player_Name', 'Rating', 'Club']])

# Step 🔟: Grouping and Aggregation
print("\n📊 Average Goals per Club:")
print(df.groupby('Club')['Goals'].mean())

print("\n🎯 Total Assists per Club:")
print(df.groupby('Club')['Assists'].sum())

# Step 1️⃣1️⃣: Add New Columns
df['Goal_Contribution'] = df['Goals'] + df['Assists']
df['Goals_per_Match'] = (df['Goals'] / df['Matches']).round(2)
df['Efficiency'] = (df['Goals_per_Match'] * df['Rating']).round(2)
print("\n🆕 Added new columns: Goal_Contribution, Goals_per_Match, Efficiency")
print(df.head())

# Step 1️⃣2️⃣: Sorting and Ranking
print("\n🥇 Top 10 Players by Goals:")
print(df.sort_values(by='Goals', ascending=False)[['Player_Name', 'Goals', 'Club']].head(10))

print("\n💪 Top 10 Players by Efficiency:")
print(df.sort_values(by='Efficiency', ascending=False)[['Player_Name', 'Efficiency', 'Club']].head(10))

# Step 1️⃣3️⃣: Descriptive Statistics by Club
print("\n📈 Statistics per Club:")
print(df.groupby('Club')[['Goals', 'Assists', 'Rating']].mean().round(2))

# Step 1️⃣4️⃣: Apply Function
def performance_level(rating):
    if rating >= 9:
        return 'Elite'
    elif rating >= 8:
        return 'Excellent'
    elif rating >= 7:
        return 'Good'
    else:
        return 'Average'

df['Performance_Level'] = df['Rating'].apply(performance_level)
print("\n🏅 Added Performance_Level based on Rating:")
print(df[['Player_Name', 'Rating', 'Performance_Level']].head())

# Step 1️⃣5️⃣: Filtering Example with Multiple Conditions
print("\n🎯 Top Elite Players (Rating ≥ 9 & Goals ≥ 15):")
elite = df[(df['Rating'] >= 9) & (df['Goals'] >= 15)]
print(elite[['Player_Name', 'Goals', 'Rating', 'Club']])

# Step 1️⃣6️⃣: Save Cleaned Data
df.to_csv("football_players_clean.csv", index=False)
print("\n💾 Clean dataset saved as 'football_players_clean.csv'")

# Step 1️⃣7️⃣: End Summary
print("\n✅ Tutorial completed successfully!")
print("You have learned:")
print("1️⃣ Load data  2️⃣ Clean data  3️⃣ Analyze with Pandas")
print("4️⃣ Create new columns  5️⃣ Save your results")
