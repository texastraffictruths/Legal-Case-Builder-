import streamlit as st
import os
import io

# Create the folder if it doesn't exist
os.makedirs("uploads", exist_ok=True)

st.set_page_config(page_title="Pro Se Legal Assistant", layout="wide")
st.title("⚖️ Pro Se Legal Assistant (Texas Federal Court)")
st.write("Upload your documents and enter your case details. AI will assist you in organizing and preparing filings.")

summary = st.text_area("📝 Case Summary", "")
violations = st.text_area("🚨 Legal Violations", "")
remedies = st.text_area("🎯 Requested Remedies", "")

if st.button("💾 Save Case"):
    st.success("✅ Case saved successfully (simulated).")
    import os
import io

st.markdown("---")
st.header("📁 Upload Case Documents")

uploaded_files = st.file_uploader(
    "Upload PDFs, images, Word docs, or text files",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")
    for file in uploaded_files:
        st.write(f"📄 {file.name}")
        # Optional: display preview for image/text
        if file.type.startswith("image/"):
            st.image(file, use_column_width=True)
        elif file.type == "text/plain":
            text = file.read().decode("utf-8")
            st.text_area(f"📝 Preview: {file.name}", text, height=150)
        elif file.type == "application/pdf":
            st.info("📕 PDF uploaded (preview not shown here).")

        # Optional: Save file to local app session folder
        with open(os.path.join("uploads", file.name), "wb") as f:
            f.write(file.getbuffer())
