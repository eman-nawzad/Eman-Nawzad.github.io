def display():
    import streamlit as st

    st.title("Welcome to the Local Climate Zones (LCZ) Web App 🌎")
    st.subheader("Analyze and Explore LCZ Data with Ease!")
    st.markdown(
        """
        ### Features:
        - Interactive map of Local Climate Zones.
        - Detailed analysis and visualizations.
        - Easy-to-use interface for professionals and researchers.
        """
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/e/ef/LCZ_Classification_Example.png",
        caption="Example of LCZ Classification (Source: Wikipedia)",
        use_column_width=True
    )
    st.write("Use the sidebar to navigate through the app.")

