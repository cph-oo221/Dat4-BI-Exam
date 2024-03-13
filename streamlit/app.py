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
    
"""
)

st.markdown("""
     ## Table of Contents
    - [Analysis Highlights](/Visualization)
        Visual representations of our analysis
    - [Carbon Emissions Classifier](/Classify)
        Predicting carbon emissions based on categories
    - [Neural Network Prediction](/ANN)
        Predicting carbon emissions with ANN
""")

st.markdown(
"""
    ## Conclusion


In conclusion of our research, we can say it is definetely possible to predict carbon emissions from lifestyle factors.
We found correlating features which has a big impact on the carbon output, transport choices being among the top.
We have created a simple frontend application with streamlit, where a user can get predictions from our models, by inputting their own lifestyle factors

- **H0**
This hypothesis is definetely false, since there is clear correlation between lifestyle factors and carbon emissions

- **H1**
We can conclude that given the same formatted inputs, we can train regression and ANN models to predict an individuals carbon emissions
with a model accuracy of around 97% to 98%

- **H2**
According to our discoveries, the most significant factor
for individual carbon emissions is style of transport (i. e public or private vehicles) and how many kilometers driven in a private vehicle a month. 

- **H3**
Out of all the factors we have available in our data, many of the factors had very little correlation to the total carbon emission output, and a few had a little correlation, and even fewer had a strong correlation.
This gives insight in how the different factors weigh more or less in the total output of carbon emissions, which might be useful for interested parts

- **H4**
We have used 10000 entries of synthetically generated data from research papers, and we have used standard recognized methods of data-analysis for our models, which gives us accuracy of around 97% for predictions. We believe our conclusions accurately represents reality.

- **H5**
We have found a small correlation of daily internet usage, with total carbon output, but we have been unable to find any clear tendency between people who spend a lot of time on the internet, and people who emit a lot of carbon. We therefore conclude, that theres no significant impact from this factor.

"""
)