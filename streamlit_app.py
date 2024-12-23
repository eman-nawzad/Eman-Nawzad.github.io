import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="LCZ Web App",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Help", "Contact", "Feedback"])

# Sidebar - Quick Links
st.sidebar.markdown("### Quick Links")
st.sidebar.markdown("[Streamlit Documentation](https://docs.streamlit.io/)")
st.sidebar.markdown("[Folium Documentation](https://python-visualization.github.io/folium/)")

# Sidebar - Dark Mode Toggle (checkbox for light/dark mode)
dark_mode = st.sidebar.checkbox("Dark Mode", value=False)

# Set custom styles based on dark mode selection
if dark_mode:
    custom_css = """
        <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .header-font {
            color: #ffffff;
        }
        .text-font {
            color: #cccccc;
        }
        </style>
    """
else:
    custom_css = """
        <style>
        body {
            background-color: #FAFAFA;
            color: #333333;
        }
        .header-font {
            color: #4A4A4A;
        }
        .text-font {
            color: #333333;
        }
        </style>
    """
st.markdown(custom_css, unsafe_allow_html=True)

# Navigation logic
if page == "Home":
    st.markdown("<h2 class='header-font'>Home Page</h2>", unsafe_allow_html=True)
    st.markdown("<p class='text-font'>Welcome to the Local Climate Zones (LCZ) Web App. This platform provides an interactive way to explore LCZ data for different regions. You can visualize the data on a map and gain insights into the local climate zones.</p>", unsafe_allow_html=True)

elif page == "About":
    st.markdown("<h2 class='header-font'>About This App</h2>", unsafe_allow_html=True)
    st.markdown("<p class='text-font'>This web application was created to provide an interactive visualization of Local Climate Zones (LCZ). It is designed for researchers, urban planners, and anyone interested in understanding how different zones are categorized based on urban and natural landscapes.</p>", unsafe_allow_html=True)

elif page == "Help":
    st.markdown("<h2 class='header-font'>Help Section</h2>", unsafe_allow_html=True)
    st.markdown("<p class='text-font'>For any queries or help, please refer to the documentation or get in touch with us.</p>", unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("<h2 class='header-font'>Contact Us</h2>", unsafe_allow_html=True)
    st.markdown("<p class='text-font'>For inquiries, please email us at <strong>support@lczwebapp.com</strong></p>", unsafe_allow_html=True)

elif page == "Feedback":
    # User Feedback Form
    st.markdown("<h2 class='header-font'>User Feedback</h2>", unsafe_allow_html=True)
    st.markdown("<p class='text-font'>We value your feedback! Please fill out the form below to share your thoughts on the app.</p>", unsafe_allow_html=True)
    
    # Create a feedback form
    with st.form("feedback_form"):
        # Collect user feedback
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        feedback = st.text_area("Your Feedback")
        
        # Submit button
        submit_button = st.form_submit_button(label="Submit Feedback")
        
        if submit_button:
            # Display a confirmation message
            if name and email and feedback:
                st.success("Thank you for your feedback!")
                # Here, you could add functionality to save the feedback to a file or database.
            else:
                st.error("Please fill out all fields.")




