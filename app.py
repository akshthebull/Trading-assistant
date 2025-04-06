import streamlit as st from ai_engine import get_ai_response from price_fetcher import get_option_prices from tracker import TradeTracker from greeks_calculator import calculate_greeks from news_feed import fetch_news from charting import live_chart_with_ai

st.set_page_config(page_title="Aksh's AI Trading Assistant", layout="wide") st.title("Aksh's AI Trading Assistant")

Sidebar

st.sidebar.header("Preferences") capital = st.sidebar.number_input("Capital (INR)", value=40000) confident_tag = st.sidebar.checkbox("Show Highly Confident Trades Only")

Tabs

tabs = st.tabs(["Live Dashboard", "AI Analysis", "Track Trades", "News Feed", "Live Chart Commentary"])

Live Dashboard

with tabs[0]: st.subheader("Live Prices & Greeks") prices = get_option_prices(capital) st.dataframe(prices)

st.subheader("Option Greeks")
greeks = calculate_greeks(prices)
st.dataframe(greeks)

AI Analysis

with tabs[1]: st.subheader("Ask AI anything about market") user_input = st.text_input("Enter your query") if user_input: response = get_ai_response(user_input) st.write(response)

Track Trades

with tabs[2]: st.subheader("Trade Tracker") tracker = TradeTracker() tracker.show_ui(confident_tag)

News Feed

with tabs[3]: st.subheader("Personalized News Feed") news = fetch_news() for article in news: st.markdown(f"- {article['title']}")

Live Chart Commentary

with tabs[4]: st.subheader("AI Commentary on Live Chart") live_chart_with_ai()

