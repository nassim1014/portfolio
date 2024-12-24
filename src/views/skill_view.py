import streamlit as st

class SkillView:
    @staticmethod
    def display_skill(skill):
        st.markdown(f"**{skill['name']}**: {skill['level']}")

    @staticmethod
    def display_all_skills(skills):
        for skill in skills:
            SkillView.display_skill(skill)