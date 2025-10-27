# src/ui/dashboard.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
import pandas as pd

from src.extract.csv_parser import load_csv
from src.utils.clean import normalize
from src.categorize.categorizer_agent import categorize_df
from src.analyze.budget_analyzer import totals_by_category, monthly_summary, savings_estimate
from src.analyze.insight_generator_gemini import generate_insights_with_gemini

# -------------------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------------------
st.set_page_config(page_title="Personal Finance AI Agent", page_icon="💰", layout="wide")
st.markdown(
    "<h2 style='text-align:center; color:#4CAF50;'>💰 AI-Powered Personal Finance Dashboard</h2>",
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------------------------------------------
# File Upload Section
# -------------------------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload your bank statement (CSV)", type=["csv"])

if uploaded_file is not None:
    # -------------------------------------------------------------------
    # Data Loading & Cleaning
    # -------------------------------------------------------------------
    df = load_csv(uploaded_file)
    df = normalize(df)
    df = categorize_df(df)

    st.success(f"✅ Parsed {len(df)} transactions successfully.")
    st.dataframe(df.head(20), use_container_width=True)

    # -------------------------------------------------------------------
    # Analytics and Charts
    # -------------------------------------------------------------------
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("💸 Spending by Category")
        cat_summary = totals_by_category(df)
        st.bar_chart(cat_summary, x="Category", y="amount")

    with col2:
        st.subheader("📆 Monthly Spending Trend")
        monthly = monthly_summary(df)
        pivot = monthly.pivot(index="month", columns="Category", values="amount").fillna(0)
        st.line_chart(pivot)

    # -------------------------------------------------------------------
    # Summary Statistics
    # -------------------------------------------------------------------
    st.divider()
    st.markdown("### 💹 Summary Stats")

    total_spent = df[df["amount"] > 0]["amount"].sum()
    total_income = df[df["amount"] < 0]["amount"].sum() * -1

    col3, col4, col5 = st.columns(3)
    col3.metric("Total Income", f"₹ {total_income:,.2f}")
    col4.metric("Total Expenses", f"₹ {total_spent:,.2f}")
    col5.metric("Suggested Savings (10%)", f"₹ {savings_estimate(df):,.2f}")

    # -------------------------------------------------------------------
    # AI-Generated Insights (Gemini)
    # -------------------------------------------------------------------
    st.divider()
    st.subheader("🧠 AI-Generated Insights (Gemini 2.5 Flash)")
    with st.spinner("Generating personalized financial insights..."):
        try:
            insights = generate_insights_with_gemini(cat_summary)
            st.write(insights)
        except Exception as e:
            st.error(f"⚠️ Could not generate insights: {e}")

    # -------------------------------------------------------------------
    # Export Processed Data
    # -------------------------------------------------------------------
    st.divider()
    st.download_button(
        label="📥 Download Processed Data as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="processed_finance_data.csv",
        mime="text/csv"
    )

else:
    # No file uploaded yet
    st.info("Please upload a CSV file to begin analysis.")

