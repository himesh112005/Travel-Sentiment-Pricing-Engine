import pandas as pd
import random
import os

# Ensure directories exist
os.makedirs('data/raw', exist_ok=True)

# Target Cities
cities = ['Goa', 'Manali', 'Jaipur', 'Kerala', 'Agra']

# 1. Generate Dummy Pricing Data
pricing_data = []
for city in cities:
    avg_flight = random.randint(4000, 12000)
    avg_hotel = random.randint(2000, 8000)
    pricing_data.append([city, avg_flight, avg_hotel, avg_flight + avg_hotel])

df_pricing = pd.DataFrame(pricing_data, columns=['City', 'Avg_Flight_Price', 'Avg_Hotel_Price', 'Total_Avg_Cost'])
df_pricing.to_csv('data/raw/pricing.csv', index=False)
print("✅ pricing.csv generated successfully!")

# 2. Generate Dummy Review Data
review_templates = [
    "Amazing experience in {}, loved the vibe!",
    "{} was too crowded and expensive this time.",
    "Decent trip to {}, but hotels could be better.",
    "Absolutely breathtaking views in {}, highly recommended.",
    "Food in {} was terrible, wouldn't go back.",
    "Average stay at {}, nothing special."
]

reviews_data = []
for _ in range(100):
    city = random.choice(cities)
    review = random.choice(review_templates).format(city)
    reviews_data.append([city, review])

df_reviews = pd.DataFrame(reviews_data, columns=['City', 'Review_Text'])
df_reviews.to_csv('data/raw/reviews.csv', index=False)
print("✅ reviews.csv generated successfully!")