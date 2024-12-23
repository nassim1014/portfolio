import streamlit as st

class PrjoectView:

    def display_old_project(project):
        st.subheader(f"{project['title']}")

        with st.container():
            st.markdown(f"""### {project['title']}""")
            col1, col2 = st.columns([2,1])
            with col1:
                st.markdown(project['description'])
        with col2:
            st.image(project['image_path'])

    def display_current_project(project):
        st.subheader(f"{project['title']}")
        st.info(f"{project['description']}")
    
    def display_all_projects(self, old_projects = [], current_projects = []):
        st.title("🚀 Projects")
        for project in old_projects:
            PrjoectView.display_old_project(project)

        st.header("🔨 Current Projects")
        for project in current_projects:
            PrjoectView.display_current_project(project)