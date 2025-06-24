import streamlit as st

st.set_page_config(page_title="Pro Se Legal Assistant", layout="wide")
st.title("⚖️ Pro Se Legal Assistant (Texas Federal Court)")

st.write("""
Welcome! Upload your documents or enter your case details.
AI will assist you in organizing your case, drafting legal documents, and preparing filings.
""")

summary = st.text_area("📝 Case Summary", "")
violations = st.text_area("🚨 Legal Violations", "")
remedies = st.text_area("🎯 Requested Remedies", "")

if st.button("💾 Save Case"):
    st.success("✅ Case saved successfully (simulated).")
