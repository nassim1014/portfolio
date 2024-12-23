# views/experience_view.py
import streamlit as st

class ExperienceView:
    @staticmethod
    def display_experience(experience):
        st.subheader(f"{experience['title']} | {experience['company']}")
        st.caption(f"{experience['date']} | {experience['location']}")
        with st.expander("View Details"):
            st.markdown(experience['details'])

    @staticmethod
    def display_all_experiences(experiences):
        st.title("💼 Professional Experience")
        for experience in experiences:
            ExperienceView.display_experience(experience)
