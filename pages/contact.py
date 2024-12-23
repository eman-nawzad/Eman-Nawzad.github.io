def display():
    import streamlit as st

    st.title("Contact Us")
    st.markdown(
        """
        ### Reach out for inquiries or feedback:
        - **Email**: your_email@example.com
        - **GitHub**: [Your Repository](https://github.com/your_username/LCZ-WebApp)
        - **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your_profile)
        """
    )
    st.success("We’d love to hear from you!")
