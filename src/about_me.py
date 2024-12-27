import streamlit as st

from utils import create_circular_image, get_direct_download_link, load_image
#from src.contact import display_contact
def display_about_me(image_url):

        with st.container():
                left_column, right_column = st.columns([1, 2])
                with right_column:
                        st.title("👋 Hello, I'm Nassim ")
                        st.markdown("""
                        Young graduate with solid training in Data Science and Software Development. 
                        Passionate about creating innovative solutions and leveraging data for business impact.
                        
                        - Exploratory Data Analysis and Predictive Model Development | **AI - Python - Pytorch - Tensorflow**.     
                        - Front-end and Back-end Development  | **React - Java - Python - SQL**.     
                                """)
                with left_column:
                        if image_url:
                                direct_link = get_direct_download_link(image_url)
                                image = load_image(direct_link)
                                img = create_circular_image(image, 250)
                                st.image(img, use_container_width =False)
                        else:
                                st.warning("Image URL not found in environment variables.")

        st.markdown("---")
        with st.container():
                left_column, right_column = st.columns([2, 1])
                with left_column:
                        st.title("🎓 Education")
                        st.subheader("Master's Degree @ **University of Technology of Compiègne**")
                        #st.write("**University of Technology of Compiègne**")
                        st.write("Machine Learning and Complex Systems Optimization")
                        st.write("2023 - 2024 | Compiègne, France")

                        st.subheader("Academic Exchange Program @ **University of Technology of Compiègne**")
                        #st.write("**University of Technology of Compiègne**")
                        st.write("Artificial Intelligence and Data Science")
                        st.write("2022 - 2023 | Compiègne, France")

                        st.subheader("Engineering Degree @ **Mohammadia School of Engineers**")
                        #st.write("**Mohammadia School of Engineers**")
                        st.write("Computer Science")
                        st.write("2020 - 2023 | Rabat, Morocco")
                
                with right_column:
                        st.markdown("""
                        ### Languages
                        - French (Bilingual)
                        - English (Bilingual)
                        - Arabic (Native) """)
                        st.markdown("""
                        ### Professional Values
                        - Team Collaboration
                        - Adaptability
                        - Autonomy
                        - Problem-Solving
                        """)
        st.markdown("---")