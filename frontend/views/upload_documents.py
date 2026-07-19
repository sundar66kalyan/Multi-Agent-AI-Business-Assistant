import os
import streamlit as st
from dashboard.api import DashboardAPI

st.write("Running file:")
st.code(os.path.abspath(__file__))

def show_upload_documents():

    st.title("📄 Upload Documents")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "docx", "txt", "pptx"]
    )

    if uploaded_file is not None:

        st.success(uploaded_file.name)

        if st.button("Upload"):

            # Debug: Show the endpoint being used
        

            response = DashboardAPI.upload_pdf(uploaded_file)

            st.json(response)

            if response.get("success"):
                st.success("Document uploaded successfully.")
            else:
                st.error(response.get("detail") or response.get("error") or "Upload failed.")