from src.factories.project_factory import ProjectFactory
import streamlit as st

project_1 = ProjectFactory.create_project("old",
        title="Medical Self-Diagnosis Web Application",
        description="""
            - Developed a web application with 95% prediction accuracy
            - **Technologies**: React JS, Flask, SQLite, Python
            - **Features**:
                * Interactive user interface
                * Machine learning-based diagnosis
                * Secure data storage
            """,
        image_path="data/projects_pics/cov_tracker.png"
        )
current_projects = ProjectFactory.create_project( "current",
        title="Portfolio",
        description="I'm currently working on:\n1. Enhanced Portfolio Website (Streamlit)\n2. Advanced Data Analysis Projects\n3. Contributing to Open Source"
        )
    
def display_projects():
    st.title("🚀 Projects")
    project_1.return_project()
    st.header("🔨 Current Projects")
    current_projects.return_project()

