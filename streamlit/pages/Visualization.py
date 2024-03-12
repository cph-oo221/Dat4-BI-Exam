import streamlit as st

st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide"
)

st.sidebar.header("Menu Options", divider=True)


st.title("Analysis of carbon emissions")

st.markdown("""
    ## Introduction

In this project, we will apply different stastistical methods, to try to analyse patterns and correlation in different lifestyle factors. This will involve trying to train different machine learning models, to see how precisely these patterns can be used to predict how much carbon is emitted based on the correlating factors.
We will try to answer the following questions: 

- Can an individuals carbon emissions be predicted by their lifestyle factors?
- Which lifestyle factor have the biggest impact on carbon emissions?
- How can this information be used by individuals and the society for reducing carbon emissions?

#### We have formulated the following hypothesises, to help us answer these questions:

H0 = an individuals carbon emissions have no relation to their lifestyle factors

H1 = an individuals carbon emissions can be predicted by their lifestyle factors

H2 = The most important factor for an individuals carbon emission is their style of transport

H3 = The information have clear tendencies, and can make it easy for people to understand how their lifestyle
affects their carbon emissions

H4 = Society can rely on the accuracy of this information for encouraging and/or discouraging behaviours of
individuals

H5 = Time spent on the internet has a significant impact on an individuals carbon emissions        
            """)

st.markdown(
    """
    ### Data Exploration:
    
    Heatmap of the correlation between the different lifestyle factors and the total carbon emissions.
    This helps us to assess the strength of the relationship between the different factors and the carbon emissions. We can use this information to decide
    what factors to focus on when trying to predict carbon emissions.
"""
)

st.image("./graphs/heatmap.png")

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

st.markdown(
    """
    ## Key Findings:
    Highest correlation between the different lifestyle factors and carbon emissions are:
    - Vehicle Monthly Distance Km (0.6)
    - Vehicle Type (0.5)
    - Transport (0.4)
    """
)