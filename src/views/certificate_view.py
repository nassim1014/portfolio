import base64
from io import BytesIO
import requests
import streamlit as st
from streamlit.components.v1 import html
from utils import open_pdf


class CertificateView:
    @staticmethod
    def display_simple_certificate(certificate): 
        with st.container(height= 200):
            # Title and details
            st.markdown(f"#### {certificate['title']}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Issued by:** {certificate['issued_by']}")
            with col2:
                st.markdown(f"**Date:** {certificate['date']}")

        if st.button('📄 View Certificate' , key=f"{certificate['title']} + {certificate['issued_by']} + {certificate['date']}"):
            open_pdf(certificate['pdf_path'])

    @staticmethod
    def display_all_certificates(certificates):
        st.title("📜 Certificates & Courses")
        # Create rows of 3 certificates each
        for i in range(0, len(certificates), 3):
            # Create three columns
            cols = st.columns(3)
            # Fill each column with a certificate
            for j in range(3):
                if i + j < len(certificates):  # Check if there's a certificate to display
                    with cols[j]:
                        CertificateView.display_simple_certificate(certificates[i + j])