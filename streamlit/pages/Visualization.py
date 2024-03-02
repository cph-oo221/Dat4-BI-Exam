import streamlit as st

st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide"
)

st.sidebar.header("Menu Options", divider=True)


st.title("Analysis of carbon emissions")

st.markdown(
    """
    ### Data Exploration:
    
    Heatmap of the correlation between the different lifestyle factors and the total carbon emissions.
"""
)


st.image("./graphs/heatmap.png")

st.markdown(
    """
    ## Key Findings:
    Highest correlation between the different lifestyle factors and carbon emissions are:
    - Vehicle Monthly Distance Km (0.6)
    - Vehicle Type (0.5)
    - Transport (0.4)
    """
)

st.markdown(
    """
    Scatter plot of Vehicle Monthly Distance Km and Carbon Emissions:
    """
)

st.image("./graphs/scatter_vehicle_monthly_distance_km_vs_carbon_emission.png")


st.markdown(
    """
    ## Gender Differences
    Correlation differences males and females are pretty much the same:
    """
)

col1, col2 = st.columns(2)

col1.markdown(
    """
    ## Male
    """
)
col1.image("./graphs/male_correlation.png")

col2.markdown(
    """
    ## Female
    """
)
col2.image("./graphs/female_correlation.png")



col1.markdown(
    """
    ## Travel Frequency
    Frequency of traveling by air, with nearly all 4 categories having a similar frequency (25% ish).
    """
)
col1.image("./graphs/frequency_of_traveling_by_air.png")

col2.markdown(
    """
    ##
    ##
    Carbon Emssions are around 22% higher for people who travel very frequently by air.
    """)
col2.image("./graphs/frequency_of_traveling_by_air_mean.png")