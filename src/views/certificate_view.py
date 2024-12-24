import base64
from io import BytesIO
import requests
import streamlit as st

from utils import get_direct_download_link

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

        direct_link = get_direct_download_link(certificate['pdf_path'])
        response = requests.get(direct_link)
        
        if response.status_code == 200:
            pdf_file = BytesIO(response.content)
            pdf_bytes = pdf_file.read()
            # Display the PDF file using Streamlit's st.download_button or any other method
            st.markdown(
                    f'<a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}" target="_blank"><button style="width: 100%; padding: 10px; background-color: #0066cc; color: white; border: none; border-radius: 5px; cursor: pointer;">📄 View Certificate</button></a>',
                    unsafe_allow_html=True
                )
        else:
            st.error("Failed to download the PDF file.")
       # pdf_file = open(certificate['pdf_path'], "rb")
       # pdf_bytes = pdf_file.read()
       # pdf_file.close()
            
#        st.markdown(
#                f'<a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}" target="_blank"><button style="width: 100%; padding: 10px; background-color: #0066cc; color: white; border: none; border-radius: 5px; cursor: pointer;">📄 View Certificate</button></a>',
#                unsafe_allow_html=True
#            )
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