import sqlite3
import pandas as pd
import os

print("Connecting to local SQLite database...")
os.makedirs('data/processed', exist_ok=True)
# This will create a .db file automatically
conn = sqlite3.connect('data/processed/travel_insights.db')

print("Loading data into SQL Tables...")
# Read CSVs
df_pricing = pd.read_csv('data/raw/pricing.csv')
df_sentiment = pd.read_csv('data/processed/sentiment_results.csv')

# Push DataFrames to SQLite Tables
df_pricing.to_sql('pricing', conn, if_exists='replace', index=False)
df_sentiment.to_sql('sentiment', conn, if_exists='replace', index=False)

print("Executing Master SQL JOIN to blend data...")
# Write the SQL Query to blend Pricing and Sentiment data
query = """
SELECT 
    p.City, 
    p.Avg_Flight_Price, 
    p.Avg_Hotel_Price, 
    p.Total_Avg_Cost, 
    ROUND(s.Avg_Sentiment_Score, 2) AS AI_Sentiment_Score
FROM pricing p
JOIN sentiment s ON p.City = s.City
ORDER BY AI_Sentiment_Score DESC;
"""

# Execute query and pull into a final DataFrame
master_df = pd.read_sql_query(query, conn)

print("\n🚀 --- FINAL MASTER VIEW --- 🚀")
print(master_df.to_string(index=False))

# Optional: Save a CSV copy of the master view for easy debugging
master_df.to_csv('data/processed/master_view.csv', index=False)

print("\n✅ SQL Blending Complete!")
print("✅ Database saved at data/processed/travel_insights.db")

conn.close()