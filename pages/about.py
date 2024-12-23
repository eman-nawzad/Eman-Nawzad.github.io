def display():
    import streamlit as st

    st.title("About Local Climate Zones (LCZ)")
    st.markdown(
        """
        Local Climate Zones (LCZ) are a classification of urban and rural land use based on thermal and physical properties.

        #### Why LCZs are Important:
        - **Urban Planning**: Helps design sustainable cities.
        - **Climate Studies**: Assists in understanding the impact of urbanization on local climate.
        - **Disaster Management**: Aids in analyzing risks related to heatwaves and urban flooding.

        This app provides an easy way to explore LCZ data interactively.
        """
    )
    st.info("Learn more about LCZs: [Wikipedia](https://en.wikipedia.org/wiki/Local_climate_zone)")

