import streamlit as st
def display_projects():
    st.title("🚀 Projects")
    
    # Medical Self-Diagnosis Web App
    with st.container():
        st.markdown("""
        ### Medical Self-Diagnosis Web Application
        """)
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            - Developed a web application with 95% prediction accuracy
            - **Technologies**: React JS, Flask, SQLite, Python
            - **Features**:
                * Interactive user interface
                * Machine learning-based diagnosis
                * Secure data storage
            """)
        with col2:
            st.image("/api/placeholder/300/200", caption="Medical App Interface")
    
    # Current Projects
    st.header("🔨 Current Projects")
    st.info("""
    I'm currently working on:
    1. Enhanced Portfolio Website (Streamlit)
    2. Advanced Data Analysis Projects
    3. Contributing to Open Source
    """)
