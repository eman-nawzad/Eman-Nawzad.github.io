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

# Set app title
st.title("Local Climate Zones (LCZ) Web App")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Navigation logic
if page == "Home":
    # Home page content
    st.header("Home Page")
    st.write("Welcome to the Local Climate Zones (LCZ) Web App.")

    # Load GeoJSON file
    geojson_path = "LCZ.GeoJson.geojson"

    # Check if the file exists
    if not os.path.exists(geojson_path):
        st.error(f"The file {geojson_path} does not exist. Please check the file path.")
    else:
        # Load the GeoJSON data
        gdf = gpd.read_file(geojson_path)

        # Display GeoJSON map
        st.header("Interactive LCZ Map")
        map_center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        # Add GeoJSON layer to the map
        folium.GeoJson(geojson_path, name="LCZ").add_to(m)
        st_folium(m, width=700, height=500)

        st.write("This map displays the Local Climate Zones (LCZ) data.")

elif page == "About":
    # About page content
    st.header("About")
    st.write("This web application provides an interactive map of Local Climate Zones (LCZ).")
    st.write("You can use this tool to visualize and explore LCZ data effectively.")
