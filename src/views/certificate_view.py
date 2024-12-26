
import streamlit as st
from utils import get_direct_download_link, load_image
from PIL import Image 
class CertificateView:
    @staticmethod
    def display_simple_certificate(certificate): 
        with st.container(height= 120):
            # Title and details
            st.markdown(f"**{certificate['title']}**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Issued by:** {certificate['issued_by']}")
            with col2:
                st.markdown(f"**Date:** {certificate['date']}")
        # Load and display the certificate image
        direct_link = get_direct_download_link(certificate['pdf_path'])
        image = load_image(direct_link)
        st.image(image, use_container_width =True)

        
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