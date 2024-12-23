def display():
    import streamlit as st
    import geopandas as gpd
    import folium
    from streamlit_folium import st_folium
    import os

    st.title("Explore the LCZ Map")

    # Define the file path for the GeoJSON file
    geojson_path = "LCZ.GeoJson.geojson"

    # Check if GeoJSON file exists
    if not os.path.exists(geojson_path):
        st.error(f"The file {geojson_path} does not exist. Please check the file path.")
    else:
        # Load GeoJSON data
        gdf = gpd.read_file(geojson_path)

        # Display map
        map_center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        # Add GeoJSON layer to the map
        folium.GeoJson(geojson_path, name="LCZ").add_to(m)
        st_folium(m, width=700, height=500)

        st.write("This map displays the Local Climate Zones (LCZ) data.")
