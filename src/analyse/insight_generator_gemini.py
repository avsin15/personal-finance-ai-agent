# src/analyze/insight_generator_gemini.py
import pandas as pd
import streamlit as st
from .gemini_client import model

@st.cache_data(show_spinner=False)
def generate_insights_with_gemini(df_summary: pd.DataFrame) -> str:
    """Generate actionable financial insights from a spending summary using Gemini 2.5 Flash."""
    if df_summary is None or df_summary.empty:
        return "⚠️ No summary data available for insights."

    prompt = (
        "You are a professional personal finance advisor. "
        "Here is the user's categorized spending summary (amounts are expenses in INR):\n\n"
        f"{df_summary.to_string(index=False)}\n\n"
        "Provide 3 short, data-driven insights about their spending habits "
        "and 1 clear suggestion for saving or reallocation."
    )

    try:
        response = model.generate_content(prompt)
        # Gemini returns response.text for convenience
        return response.text.strip() if response and hasattr(response, "text") else "⚠️ No response from Gemini."
    except Exception as e:
        return f"⚠️ Gemini insight generation failed: {e}"
