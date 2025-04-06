import streamlit as st
import pandas as pd
import datetime
import random

# Title
st.set_page_config(page_title="Aksh's AI Trading Assistant", layout="wide")
st.title("Aksh's AI Trading Assistant")
st.markdown("Your personalized stock options tracker, alerts, and AI-powered insights")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Options Tracker", "News", "BTST Picks", "AI Commentary"])

# Simulated data generators
def get_fake_options_data():
    return pd.DataFrame({
        'Symbol': ['RELIANCE', 'TATASTEEL', 'ICICIBANK', 'SBIN'],
        'Strike Price': [2500, 120, 940, 600],
        'Type': ['CE', 'PE', 'CE', 'PE'],
        'Premium': [45.5, 23.4, 75.2, 15.8],
        'Delta': [0.45, -0.32, 0.52, -0.29],
        'Theta': [-0.12, -0.09, -0.15, -0.06],
        'Gamma': [0.02, 0.03, 0.01, 0.02],
        'Confidence': ['High', 'Medium', 'High', 'Low']
    })

def get_fake_btst():
    return pd.DataFrame({
        'Stock': ['TCS', 'HDFCLIFE', 'VEDL'],
        'Buy Price': [3870, 600, 312],
        'Target Price': [3950, 620, 325],
        'Stop Loss': [3800, 590, 305],
        'Volume Spike': ['Yes', 'No', 'Yes']
    })

def get_fake_news():
    return [
        "Nifty breaks resistance, eyes 23,000 mark.",
        "RVNL gets ₹500 crore project from Indian Railways.",
        "Bank Nifty sees highest OI build-up in 3 weeks.",
        "AI-powered options trading gains traction in India."
    ]

def get_fake_ai_commentary():
    return """
    Price action shows a clear breakout in midcaps. Volume increasing steadily in RVNL indicates potential bullish rally.
    Options data suggests strong CE writing around 2350 in RELIANCE. Wait for confirmation before entering.
    """

# Dashboard
if page == "Dashboard":
    st.subheader("Market Snapshot")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nifty", "22,850", "+150 (0.66%)")
        st.metric("Sensex", "75,100", "+300 (0.40%)")
    with col2:
        st.metric("Bank Nifty", "48,230", "-80 (0.17%)")
        st.metric("India VIX", "10.2", "+0.45 (4.62%)")

    st.subheader("Top Suggestions Today")
    st.write(get_fake_options_data())

# Options Tracker
elif page == "Options Tracker":
    st.subheader("Stock Options Tracker")
    df = get_fake_options_data()
    st.dataframe(df, use_container_width=True)

# News
elif page == "News":
    st.subheader("Personalized Market News")
    for news in get_fake_news():
        st.info(news)

# BTST
elif page == "BTST Picks":
    st.subheader("BTST Trade Suggestions")
    st.write(get_fake_btst())

# AI Commentary
elif page == "AI Commentary":
    st.subheader("Live AI Commentary")
    st.markdown(get_fake_ai_commentary())