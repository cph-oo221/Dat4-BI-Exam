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
    This helps us to assess the strength of the relationship between the different factors and the carbon emissions. We can use this information to discover important
    factors for further research and analysis.
    """
)
st.image("./graphs/heatmap.png")

st.markdown(
    """
    ## Gender Differences
    Correlation differences males and females seems to be about the same:
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

st.markdown(
    """
    From the correlation matrix, we can see that one of the most important factors for carbon emissions is the vehicle monthly distance km.
    This is also supported by the scatter plot below, where we can see a clear positive correlation between the vehicle monthly distance km and the carbon emissions.
    """
)
st.image("./graphs/frequency_sex.png")

st.markdown(
    """
    From the frequency distribution we can see that there are no significant differences between Male and Female, almost a 50/50 split.

    """
)

st.markdown("""
Other high correlation factors:
            
    - Vehicle Type (0.5)
            
    - Transport (0.4)
            
    - Frequency of Traveling by Air (0.3)
            
Lesser correlating factors:
    
    - Waste bag weekyl count (0.2)
            
    - How many new clothes a month (0.2)
            
Since vehicle type, Transport method and monthly distance are naturally highly correlated, we will focus primarily on the vehicle monthly distance km among these 3.
""")

st.image("./graphs/scatter_vehicle_monthly_distance_km_vs_carbon_emission.png")

col1, col2 = st.columns(2)

col1.image("./graphs/frequency_vehicletype.png")
col2.image("./graphs/frequency_transport.png")

st.markdown(
    """
    In the sample data, the majority of people dont own a car (around 60% ), and more then 33% travel by bike/walk. 
    """
)
            

col1, col2 = st.columns(2)
st.markdown(
    """
    ## Travel Frequency
    """
)
col1, col2 = st.columns(2)
col1.markdown(
    """
    Frequency of traveling by air, with nearly all 4 categories having a similar frequency (25% ish).
    Theres a small majority of people flying very frequently, and a small minority of people flying rarely.
    """
)
col1.image("./graphs/frequency_of_traveling_by_air.png")


col2.markdown(
    """
    ##
    ##
    Mean carbon emissions for people who identify with each category of frequency of traveling by air.
    """)
col2.image("./graphs/frequency_of_traveling_by_air_mean.png")

col1, col2 = st.columns(2)

st.markdown("""
              
**The mean and total sum of carbon emissions for each flight frequence category**
              
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Frequency of Traveling by Air</th>
      <th>mean</th>
      <th>sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>frequently</td>
      <td>2362.866482</td>
      <td>5963875</td>
    </tr>
    <tr>
      <th>1</th>
      <td>never</td>
      <td>1716.337129</td>
      <td>4220473</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rarely</td>
      <td>1945.872830</td>
      <td>4819927</td>
    </tr>
    <tr>
      <th>3</th>
      <td>very frequently</td>
      <td>3026.455906</td>
      <td>7687198</td>
    </tr>
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.text("")

st.markdown("""
The carbon emissions are around 25% higher on average, for people who fly very frequently, compared to the mean across all categories. 
""")

st.text("")

st.markdown(
    """
    ## Key Findings:
    """
)