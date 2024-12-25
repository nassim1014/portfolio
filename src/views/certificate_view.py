from io import BytesIO
import requests
import streamlit as st
from utils import get_direct_download_link
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
        # image = Image.open(r"images\OC\4815824035-1.png")
        direct_link = get_direct_download_link(certificate['pdf_path'])
        response = requests.get(direct_link)
        image = Image.open(BytesIO(response.content))
        
            #with col1:
            #    st.image(image, caption="Click to zoom", use_column_width=True)
        st.image(image, use_container_width =True)
        #st.markdown("----")
            #with col2:
            #    image_zoom(image, size=400, zoom_factor=2.5)
       # if st.button('📄 View Certificate' , key=f"{certificate['title']} + {certificate['issued_by']} + {certificate['date']}"):
       #     open_pdf(certificate['pdf_path'])
        
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