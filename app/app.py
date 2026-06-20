import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

# 1. Page Configuration
st.set_page_config(page_title="AI Travel Engine", page_icon="🌍", layout="wide")
st.title("🌍 AI-Powered Travel & Sentiment Engine")
st.markdown("Find the best value travel destinations blending real-time costs and AI sentiment analysis.")

# 2. Database Connection
@st.cache_data
def load_data():
    db_path = 'data/processed/travel_insights.db'
    if not os.path.exists(db_path):
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_path)
    query = """
    SELECT 
        p.City, 
        p.Total_Avg_Cost AS Price, 
        ROUND(s.Avg_Sentiment_Score, 2) AS Sentiment
    FROM pricing p
    JOIN sentiment s ON p.City = s.City
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

df = load_data()

if df.empty:
    st.error("Database not found! Please run the SQL pipeline first.")
else:
    # 3. Sidebar UI for Inputs
    st.sidebar.header("⚙️ User Preferences")
    max_budget = st.sidebar.slider("Maximum Budget (₹)", min_value=5000, max_value=20000, value=15000, step=500)

    # 4. Filter Logic
    filtered_df = df[df['Price'] <= max_budget]

    # 5. Dashboard Layout (2 Columns)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Cost vs. Sentiment Quadrant")
        if not filtered_df.empty:
            # Interactive Plotly Chart
            fig = px.scatter(
                filtered_df, 
                x="Price", 
                y="Sentiment", 
                text="City",
                size="Sentiment",
                color="Sentiment",
                color_continuous_scale="Tealgrn",
                title="Target the Top-Left: Low Cost, High Sentiment"
            )
            fig.update_traces(textposition='top center', marker=dict(line=dict(width=2, color='DarkSlateGrey')))
            # Clean layout
            fig.update_layout(xaxis_title="Total Cost (₹)", yaxis_title="AI Sentiment Score (0-10)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No cities found within this budget. Try increasing the slider!")

    with col2:
        st.subheader("🏆 AI Recommendation")
        if not filtered_df.empty:
            # Core Business Logic: Highest Sentiment within Budget
            best_city = filtered_df.loc[filtered_df['Sentiment'].idxmax()]
            
            st.success(f"**Top Pick: {best_city['City']}**")
            st.metric(label="Estimated Cost", value=f"₹{best_city['Price']}")
            st.metric(label="AI Vibe Score", value=f"{best_city['Sentiment']} / 10")
            
            st.markdown("---")
            st.write("📋 **Available Data Table**")
            st.dataframe(filtered_df.sort_values('Sentiment', ascending=False), hide_index=True)