import tabula
import pandas as pd
import streamlit as st

st.title('ETL File PDF ke CSV atau Excel')

# File Upload
uploaded_file = st.file_uploader("Upload File PDF", type=["pdf"])

if uploaded_file is not None:
    # Read PDF File
    dfs = tabula.read_pdf(uploaded_file, pages="all", encoding='cp1252')

    # Convert into Excel or CSV Files
    export_as = st.selectbox("Export file as", ["CSV", "Excel"])
    if export_as == "CSV":
        for i, df in enumerate(dfs):
            df.to_csv(f"dataset_{i+1}.csv", index=False)
    else:
        for i, df in enumerate(dfs):
            df.to_excel(f"dataset_{i+1}.xlsx", index=False)

    st.success("File berhasil di ETL!")
