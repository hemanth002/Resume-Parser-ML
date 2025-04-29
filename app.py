import streamlit as st
from utils.parser import parse_resume
import os
import json
import pandas as pd

st.title("Resume Parser")

# Upload multiple resumes
st.header("Upload Resumes (PDF or TXT)")
uploaded_files = st.file_uploader("Upload Multiple Resumes", type=["pdf", "txt"], accept_multiple_files=True)

if uploaded_files:
    all_results = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join("data", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner(f"Parsing {uploaded_file.name}..."):
            result = parse_resume(file_path)
            result["FileName"] = uploaded_file.name
            all_results.append(result)

    if all_results:
        df_all = pd.DataFrame(all_results)
        st.success(f"Parsed {len(all_results)} resumes.")
        st.dataframe(df_all)

        # Download buttons
        st.download_button("📥 Download All as CSV", df_all.to_csv(index=False), "all_parsed_resumes.csv", "text/csv")
        st.download_button("🗂️ Download All as JSON", json.dumps(all_results, indent=4), "all_parsed_resumes.json", "application/json")
