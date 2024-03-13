# Dat4-BI-Exam

## Analysis of carbon emissions, based on individual lifestyle factors

### Group:

- Lasse Hansen - Github: **[kotteletfisk](https://github.com/kotteletfisk)**
- Oskar Olsen - Github: **[cph-oo221](https://github.com/cph-oo221)**

## Problem Statement:

Since carbon emissions have such a big impact on the greenhouse effect, every caution must be made to try and minimize these as mush as possible.
In this analysis we will try to identify patterns in individual peoples lifestyle factors, that contribute to their total carbon emissions, to make people more aware of how their lifestyle affects the climate.

## Context and Purpose:

In a world of climate change, it is important to reflect on the different things that affect this phenomena,
to understand it better, and realize it's consequences

The purpose of this analysis, is to better understand how the indivual lifestyles affect total
carbon emissions.
to understand how individual people can help the environment by being aware of how their lifestyle
affect these carbon emissions.
Make it easier for normal people to make educated decisions on how to have a more positive impact on the climate.

It can help researchers understand how and how much individals traits and/or lifestyle choices, affect total carbon
emissions

It can help society educate people on lifestyle choices and discourage harmful behaviours.

## Research Questions and Hypotheses:

- Can an individuals carbon emissions be predicted by their lifestyle factors?
- Which lifestyle factor have the biggest impact on carbon emissions?
- How can this information be used by individuals and the society for reducing carbon emissions?

H0 = an individuals carbon emissions have no relation to their lifestyle factors

H1 = an individuals carbon emissions can be predicted by their lifestyle factors

H2 = The most important factor for an individuals carbon emission is their style of transport

H3 = The information have clear tendencies, and can make it easy for people to understand how their lifestyle
affects their carbon emissions

H4 = Society can rely on the accuracy of this information for encouraging and/or discouraging behaviours of
individuals

H5 = Time spent on the internet has a significant impact on an individuals carbon emissions

## Expected Solution:

We expect that the information this analysis provides will create insight for individuals and instances in society,
to better understand how their lifestyle contributes to total carbon emissions

## Potential Impact and Users:

In correctly identifying lifestyle factors, it might be easier for individuals to make educated choices, which have lower carbon emissions.
Society would benefit from this information, because it would make it more clear to campaign what behaviours should be encouraged and discouraged.

## Data Source:

[Individual Carbon Footprint Calculation](https://www.kaggle.com/datasets/dumanmesut/individual-carbon-footprint-calculation)

## Execution Plan:

This project will be executed in 4 sprints, a sprint is 1. week period (approximately):

- **Sprint 1:** Problem Formulation
- **Sprint 2:** Data Collection and Preprocessing
- **Sprint 3:** Model Development and Testing
- **Sprint 4:** Deployment and Usability Evaluation

| Sprint | Start Date | End Date   | Goal                                |
| :----: | ---------- | ---------- | ----------------------------------- |
|   1    | 12-02-2024 | 19-02-2024 | Problem Formulation                 |
|   2    | 19-02-2024 | 26-02-2024 | Data Collection and Preprocessing   |
|   3    | 26-02-2024 | 11-03-2024 | Model Development and Testing       |
|   4    | 11-03-2024 | 14-03-2024 | Deployment and Usability Evaluation |

## Development Platform

- **IDE:** Visual Studio Code (VSCode) & Jupyter Notebook

- **Software Tools:** Git, GitHub, Anaconda, Streamlit & Python (Pandas, Numpy, Matplotlib, Seaborn, Plotly, Scikit-learn, TensorFlow, Keras, XGBoost, Yellowbrick, Graphviz)

- **Visualization and interaction** Streamlit

## Conclusion of research

In conclusion of our research, we can say it is definetely possible to predict carbon emissions from lifestyle factors.
We found correlating features which has a big impact on the carbon output, transport choices being among the top.
We have created a simple frontend application with streamlit, where a user can get predictions from our models, by inputting their own lifestyle factors. Additionally the streamlit app has a page (visualization), that gose through the highligts of our analysis, and shows the most important features/findings.

**H0**
This hypothesis is definetely false, since there is clear correlation between lifestyle factors and carbon emissions

**H1**
We can conclude that given the same formatted inputs, we can train regression and ANN models to predict an individuals carbon emissions
with a model accuracy of around 97% to 98%

**H2**
According to our discoveries, the most significant factor
for individual carbon emissions is style of transport (i. e public or private vehicles) and how many kilometers driven in a private vehicle a month.

**H3**
Out of all the factors we have available in our data, many of the factors had very little correlation to the total carbon emission output, and a few had a little correlation, and even fewer had a strong correlation.
This gives insight in how the different factors weigh more or less in the total output of carbon emissions, which might be useful for interested parts

**H4**
We have used 10000 entries of synthetically generated data from research papers, and we have used standard recognized methods of data-analysis for our models, which gives us accuracy of around 97% for predictions. We believe our conclusions accurately represents reality.

**H5**
We have found a small correlation of daily internet usage, with total carbon output, but we have been unable to find any clear tendency between people who spend a lot of time on the internet, and people who emit a lot of carbon. We therefore conclude, that theres no significant impact from this factor.
