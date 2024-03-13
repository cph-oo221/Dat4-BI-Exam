import streamlit as st

st.set_page_config(
    page_title="BI Exam Project",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

banner = """
    <body style="background-color:yellow;">
            <div style="background-color:#385c7f;padding:10px">
                <h2 style="color:white;text-align:center;">Analysis of carbon emissions, based on individual lifestyle factors</h2>
            </div>
    </body>
    """

st.markdown(banner, unsafe_allow_html=True)

st.markdown(
    """
    ###
    ### Discription of the project:    
    
    Since carbon emissions have such a big impact on the greenhouse effect, every caution must be made to try and minimize these as mush as possible.
    In this analysis we will try to identify patterns in normal individual peoples 
    lifestyle factors, that contribute to their total carbon emissions, to make people more aware of how their lifestyle affects the climate.

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
    
    ### Check out
    - [Our research](/Visualization)
    - [Carbon Emissions Classifier](/Classify)
    - [Neural Network Prediction](/ANN)
"""
)