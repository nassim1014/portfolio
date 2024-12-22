import streamlit as st
from src.factories.certificate_factory import CertificateFactory

certificates = [
    
    CertificateFactory.create_certificate( 
        "simple",
        title="Deep Learning",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_Badge20241222-27-1jiqod.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Accelerated Deep Learning with GPU",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Accelerated_Deep_Learning_with_GPU_Badge20240125-29-ryed1.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Docker Essentials: A Developer Introduction",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Docker_Essentials__A_Developer_Introduction_Badge20240123-34-wphi82.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Deep Learning Essentials",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_Essentials_Badge20240124-31-8mg2fi.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Deep Learning using TensorFlow",
        issued_by="IBM",
        date="2024",
        pdf_path="data/certifs/IBM/Deep_Learning_using_TensorFlow_Badge20240124-31-qdx95e.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Réalisez des calculs distribués sur des données massives",
        issued_by="OpenClassrooms",
        date="2022",
        pdf_path="data/certifs/OPEN CLASSROOMS/6518086339.pdf",
        logos=["data/certifs/logos/oc.png" ,"data/certifs/logos/csup.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Data Science Foundations - Level 1",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Science_Foundations_-_Level_1_Badge20210622-58-1aaxgev.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),

    CertificateFactory.create_certificate( 
        title="Python for Data Science",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Python_for_Data_Science_Badge20241222-28-gk5faw.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),

    CertificateFactory.create_certificate( 
        title="Data Analysis Using Python",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Analysis_Using_Python_Badge20241222-27-7qej7a.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ]),
    
    CertificateFactory.create_certificate( 
        title="Data Visualization with R",
        issued_by="IBM",
        date="2021",
        pdf_path="data/certifs/IBM/Data_Visualization_with_R_Badge20210622-58-1b8g715.pdf",
        logos=["data/certifs/logos/ibm_logo.png" ])
    ]
def display_certificates():
    st.title("📜 Certificates & Courses")
    # Create rows of 3 certificates each
    for i in range(0, len(certificates), 3):
        # Create three columns
        cols = st.columns(3)
        
        # Fill each column with a certificate
        for j in range(3):
            if i + j < len(certificates):  # Check if there's a certificate to display
                with cols[j]:
                    certificates[i + j].return_certificate()
    # Group certificates in rows of 3
#    certificates = [
#        DeepLearning, DeepLearning_gpu_certificate, Docker_certificate,
#        DeepLearning_ess_certificate, DeepLearning_tensorflow_certificate, BigData_certificate,
#        DS_lvl1_certificate, python_DS__certificate, Data_Analysis_certificate,
#        R_certificate 
#    ]

#    return display_certificates(certificates)

