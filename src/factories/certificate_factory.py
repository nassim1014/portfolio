import streamlit as st
from abc import ABC, abstractmethod
from utils import display_logos_base64, display_pdf, display_pdf_interactive
import base64
class Certificate(ABC):
    @abstractmethod
    def return_certificate(self):
        pass

class Pdf_certificate(Certificate):
    def __init__(self, title : str, issued_by : str, verification_link : str, pdf_path : str):
        self.title = title
        self.issued_by = issued_by
        self.verification_link = verification_link
        self.pdf_path = pdf_path
    # Function to display a certificate
    def return_certificate(self):
        st.write(f"### {self.title}")
        st.write(f"Issued by: {self.issued_by}")
        st.write(f"[Verify Certificate]({self.verification_link})")

        # PDF Preview (Embedded Viewer)
        st.write("Preview Certificate:")
        display_pdf_interactive(self.pdf_path)

        # Download Button for the PDF
        with open(self.pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(
                label="Download Certificate",
                data=pdf_bytes,
                file_name=self.pdf_path.split("/")[-1],
                mime="application/pdf",
            )
class Simple_certificate(Certificate):
    def __init__(self, title: str, issued_by: str, date: str, pdf_path: str, logos: list):
        self.title = title
        self.issued_by = issued_by
        self.date = date
        self.pdf_path = pdf_path  # Path to the PDF certificate
        self.logos = logos  # List of logos paths or URLs
    
    def return_certificate(self):
        # Display certificate details
        st.write(f"### {self.title}")
        st.write(f"Issued by: {self.issued_by}")
        st.write(f"Date: {self.date}")
        
        # Display logos at the bottom
        display_logos_base64(self.logos)
        
        # "View Certificate" button to open PDF in a new page
        #if st.button("View Certificate"):
            # Create a link to open the PDF in a new tab
        pdf_file = open(self.pdf_path, "rb")
        pdf_bytes = pdf_file.read()
        pdf_file.close()
       #     st.download_button(
       #         label="Download Certificate",
       #         data=pdf_bytes,
       #         file_name=self.pdf_path.split("/")[-1],
       #         mime="application/pdf",
       #     )
        st.markdown(f'<a href="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}" target="_blank">Open Certificate in New Tab</a>', unsafe_allow_html=True)

class CertificateFactory:
    @staticmethod
    def create_certificate(certificate_type = "simple", **kwargs):
        if certificate_type == "simple":
            return Simple_certificate(kwargs["title"], kwargs["issued_by"], kwargs["date"], kwargs["pdf_path"], kwargs["logos"])
        if certificate_type == "pdf":
            return Pdf_certificate(kwargs["title"], kwargs["issued_by"], kwargs["verification_link"], kwargs["pdf_path"])
        else:
            raise ValueError("Invalid certificate type. Please choose 'Simple' or 'Pdf'.")