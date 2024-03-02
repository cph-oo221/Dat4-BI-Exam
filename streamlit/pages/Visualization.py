import streamlit as st

st.set_page_config(page_title="Visualization", page_icon="🧊")

st.sidebar.header("Menu Options", divider=True)

st.markdown(
    """
    ### Data Exploration:
    
    Heatmap of the correlation between the different lifestyle factors and the total carbon emissions.
"""
)

st.image("./graphs/heatmap.png")


st.markdown(
    """
    
    Heatmap of the correlation between the different lifestyle factors and the total carbon emissions.
"""
)