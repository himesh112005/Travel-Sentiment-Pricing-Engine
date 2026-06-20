import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm
import os

# Ensure processed directory exists
os.makedirs('data/processed', exist_ok=True)

print("Downloading lightweight NLTK VADER lexicon (just a few KBs)...")
nltk.download('vader_lexicon', quiet=True)

print("Loading VADER Sentiment Analyzer...")
sid = SentimentIntensityAnalyzer()

print("Reading raw reviews...")
df_reviews = pd.read_csv('data/raw/reviews.csv')

print("Analyzing sentiment for reviews...")
results = []
for review in tqdm(df_reviews['Review_Text']):
    # VADER gives a compound score between -1 (negative) and 1 (positive)
    score = sid.polarity_scores(review)['compound']
    results.append(score)

df_reviews['Sentiment_Score'] = results

print("\nAggregating data by City...")
city_sentiment = df_reviews.groupby('City')['Sentiment_Score'].mean().reset_index()

# Scale sentiment to 0-10 for easier UI visualization
# VADER compound is -1 to 1, scaling it to 0-10
city_sentiment['Avg_Sentiment_Score'] = ((city_sentiment['Sentiment_Score'] + 1) / 2) * 10
city_sentiment = city_sentiment.drop(columns=['Sentiment_Score'])

city_sentiment.to_csv('data/processed/sentiment_results.csv', index=False)
print("✅ AI Sentiment Analysis Complete (Plan B Successful)!")
print("✅ data/processed/sentiment_results.csv saved successfully!")