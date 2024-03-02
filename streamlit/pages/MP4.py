import streamlit as st

st.set_page_config(page_title="MP4", page_icon="🧊")

st.sidebar.header("Menu Options", divider=True)




st.markdown(
    """
    
    ### Kmeans Clustering:

    Ditermining the optimal number of clusters for the Kmeans algorithm, using the Elbow method.
"""
)

st.image("./graph/output.png")