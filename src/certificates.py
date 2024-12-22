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


def display_certificates(certificates):
    # Create rows of 3 certificates each
    for i in range(0, len(certificates), 3):
        # Create three columns
        cols = st.columns(3)
        
        # Fill each column with a certificate
        for j in range(3):
            if i + j < len(certificates):  # Check if there's a certificate to display
                with cols[j]:
                    certificates[i + j].return_certificate()

def MyCertificates():
    
    DeepLearning = Simple_certificate( 
        title="Deep Learning",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_Badge20241222-27-1jiqod.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    DeepLearning_gpu_certificate = Simple_certificate( 
        title="Accelerated Deep Learning with GPU",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Accelerated_Deep_Learning_with_GPU_Badge20240125-29-ryed1.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    Docker_certificate = Simple_certificate( 
        title="Docker Essentials: A Developer Introduction",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Docker_Essentials__A_Developer_Introduction_Badge20240123-34-wphi82.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    DeepLearning_ess_certificate = Simple_certificate( 
        title="Deep Learning Essentials",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_Essentials_Badge20240124-31-8mg2fi.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    DeepLearning_tensorflow_certificate = Simple_certificate( 
        title="Deep Learning using TensorFlow",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_using_TensorFlow_Badge20240124-31-qdx95e.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    BigData_certificate = Simple_certificate( 
        title="Réalisez des calculs distribués sur des données massives",
        issued_by="OpenClassrooms",
        date="2022",
        pdf_path="data/certifs/OPEN CLASSROOMS/6518086339.pdf",
        logos=["data/certifs/logos/oc.png" ,"data/certifs/logos/csup.png" ])
    
    DS_lvl1_certificate = Simple_certificate( 
        title="Data Science Foundations - Level 1",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Science_Foundations_-_Level_1_Badge20210622-58-1aaxgev.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])

    python_DS__certificate = Simple_certificate( 
        title="Python for Data Science",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Python_for_Data_Science_Badge20241222-28-gk5faw.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])

    Data_Analysis_certificate = Simple_certificate( 
        title="Data Analysis Using Python",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Analysis_Using_Python_Badge20241222-27-7qej7a.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    
    R_certificate = Simple_certificate( 
        title="Data Visualization with R",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Visualization_with_R_Badge20210622-58-1b8g715.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])

    # Group certificates in rows of 3
    certificates = [
        DeepLearning, DeepLearning_gpu_certificate, Docker_certificate,
        DeepLearning_ess_certificate, DeepLearning_tensorflow_certificate, BigData_certificate,
        DS_lvl1_certificate, python_DS__certificate, Data_Analysis_certificate,
        R_certificate 
    ]

    return display_certificates(certificates)

