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

# Custom CSS using Times New Roman with uniform boldness
custom_css = """
    <style>
    body {
        font-family: 'Times New Roman', serif;  /* Set Times New Roman for the whole page */
        background-color: #FAFAFA;  /* Light gray background for better contrast */
        color: #333333;  /* Slightly lighter black for readability */
    }

    .header-font {
        font-family: 'Times New Roman', serif;  /* Times New Roman for headers */
        font-size: 2.5rem;  /* Large font size for headers */
        color: #4A4A4A;  /* Dark gray for header text */
        font-weight: bold;
        margin-bottom: 20px;
    }

    .text-font {
        font-family: 'Times New Roman', serif; /* Times New Roman for text */
        font-size: 1.3rem;  /* Slightly larger text for readability */
        color: #333333; /* Dark gray for text color */
        line-height: 1.8; /* Increase line spacing for readability */
        font-weight: bold; /* Make all text bold for uniformity */
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
        "<p class='text-font'>Welcome to the Local Climate Zones (LCZ) Web App. This platform provides an interactive way to explore LCZ data for different regions. You can visualize the data on a map and gain insights into the local climate zones.</p>",
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
        "<p class='text-font'>This web application was created to provide an interactive visualization of Local Climate Zones (LCZ). It is designed for researchers, urban planners, and anyone interested in understanding how different zones are categorized based on urban and natural landscapes.</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='text-font'>The app leverages <strong>Streamlit</strong> for user-friendly interfaces and <strong>Folium</strong> for map visualizations. The LCZ data is sourced from GeoJSON files, which allows for accurate spatial mapping and analysis.</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='text-font'>Feel free to explore the map and gain valuable insights into the climate zones in your region.</p>",
        unsafe_allow_html=True
    )

