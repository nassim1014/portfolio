import streamlit as st
def display_certificates():
    st.title("📜 Certificates & Courses")
    
    certificates = [
        {
            "name": "Machine Learning Specialization",
            "platform": "Coursera",
            "date": "2023"
        },
        {
            "name": "Deep Learning Specialization",
            "platform": "Coursera",
            "date": "2023"
        }
    ]
    
    for cert in certificates:
        st.markdown(f"""
        ### {cert['name']}
        **Platform**: {cert['platform']}  
        **Completed**: {cert['date']}
        """)
        st.image("/api/placeholder/400/200", caption=f"{cert['name']} Certificate")
