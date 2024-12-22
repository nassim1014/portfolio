import streamlit as st
def display_contact():
    st.title("📫 Contact Me")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Contact Information
        - 📧 Email: zaari.nassim@gmail.com
        - 📱 Phone: +33 6 99 38 30 36
        - 📍 Location: Paris, France
        """)
    
    with col2:
        st.markdown("""
        ### Professional Profiles
        - [LinkedIn](https://linkedin.com/in/nassim-zaari/)
        - [GitHub](https://github.com/nassim1014)
        - [Credly](https://credly.com/users/nassim-zaari/badges)
        """)
    
    # Contact Form
    st.header("Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success("Thank you for your message! I'll get back to you soon.")