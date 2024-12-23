import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import os

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="LCZ Web App",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Custom CSS for changing fonts
custom_css = """
    <style>
    body {
        font-family: 'Arial', sans-serif;  /* Change the default font for the whole page */
        background-color: #f8f9fa;  /* Light background color */
    }
    .header-font {
        font-family: 'Georgia', serif;  /* Custom font for headers */
        font-size: 2rem; /* Increase header font size */
        color: #4CAF50; /* Green color for headers */
        font-weight: bold;
        margin-bottom: 20px;
    }
    .text-font {
        font-family: 'Verdana', sans-serif; /* Custom font for text */
        font-size: 1.2rem; /* Slightly larger text size */
        color: #333; /* Dark text color */
        line-height: 1.6; /* Add spacing between lines */
    }
    </style>
"""
# Inject custom CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)

# Navigation logic
if page == "Home":
    # Home page content
    st.markdown("<h2 class='header-font'>Home Page</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='text-font'>Welcome to the Local Climate Zones (LCZ) Web App. This platform allows you to interactively explore LCZ data for different regions. You can visualize the data on a map and gain insights about local climate zones.</p>",
        unsafe_allow_html=True
    )

    # Load GeoJSON file
    geojson_path = "LCZ.GeoJson.geojson"

    # Check if the file exists
    if not os.path.exists(geojson_path):
        st.error(f"The file {geojson_path} does not exist. Please check the file path.")
    else:
        # Load the GeoJSON data
        gdf = gpd.read_file(geojson_path)

        # Display GeoJSON map
        st.markdown("<h3 class='header-font'>Interactive LCZ Map</h3>", unsafe_allow_html=True)
        map_center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        # Add GeoJSON layer to the map
        folium.GeoJson(geojson_path, name="LCZ").add_to(m)
        st_folium(m, width=700, height=500)

        st.markdown(
            "<p class='text-font'>This map displays the Local Climate Zones (LCZ) data for the selected region. Use this tool to better understand urban climate zones and their characteristics.</p>",
            unsafe_allow_html=True
        )

elif page == "About":
    # About page content
    st.markdown("<h2 class='header-font'>About This App</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='text-font'>This web application was built to provide an interactive visualization of Local Climate Zones (LCZ). It is designed for researchers, urban planners, and anyone interested in understanding how different zones are categorized based on urban and natural landscapes.</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='text-font'>The data is sourced from GeoJSON files, and the app leverages the power of <strong>Streamlit</strong> for creating interactive user interfaces and <strong>Folium</strong> for map visualizations.</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='text-font'>Feel free to explore the map and learn more about the climate zones in your region.</p>",
        unsafe_allow_html=True
    )
