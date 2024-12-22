import streamlit as st
from src.factories.experience_factory import ExperienceFactory

experiences = [
    ExperienceFactory.create_experience( experience_type = "internship",
        title="AI Engineer Intern", 
        company="ASTEK", 
        date="February 2024 - August 2024", 
        location="Boulogne-Billancourt, France", 
        details="- Developed a drone route planning system using Reinforcement Learning, Machine Learning, and Deep Learning\n"
        "- Achieved 80-100% success rate and 40% reduction in training time\n"
        "- Technologies: Python, PyTorch, Gym, MLflow, PostgreSQL, Docker\n- Worked in an AI team using Scrum methodology"
        ),

    ExperienceFactory.create_experience( experience_type = "internship",
        title="Machine Learning Engineer Intern",
        company="AXA France",
        date="March 2023 - August 2023",
        location="Nantes, France",
        details="- Developed predictive analytics for agent recruitment zones\n"
        "- Created Streamlit application for customer potential forecasting\n"
        "- Automated workflows using Power Automate\n- Built reports using Power BI"
        ),

    ExperienceFactory.create_experience( experience_type = "internship",
        title="Data Analyst Intern",
        company="Electroplanet",
        date="July 2022 - September 2022",
        location="Casablanca, Morocco",
        details="- Analyzed sales data using R/RStudio to uncover optimization strategies\n"
            "- Developed dashboards in Excel for tracking sales KPIs, aiding decision-making\n"
            "- Provided actionable insights to improve commercial performance"
        ),

    ExperienceFactory.create_experience( experience_type = "internship",
        title="Software Developer Intern",
        company="Omnishore Groupe MedTech",
        date="July 2021 - September 2021",
        location="Casablanca, Morocco",
        details="- Created a platform for managing applications and projects for the Pôle Régie using SharePoint and Power Apps\n"
                "- Designed and implemented custom interfaces using HTML, CSS, and JavaScript\n"
                "- Enhanced team efficiency by streamlining workflows and automating processes"
        )
]
def display_experience():
    st.title("💼 Professional Experience")
    for experience in experiences:
        experience.return_experience()