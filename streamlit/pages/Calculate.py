import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="MP4", page_icon="🧊")

st.sidebar.header("Menu Options", divider=True)

st.markdown(
    """
    ### Calculate Carbon Emissions from Lifestyle Factors:
    <style>
        .stButton>button:focus:not(:active) {
            border: none !important;
        }
        .stButton>button:hover {
            border-color: green !important;
        }

    </style>
    """
, unsafe_allow_html=True)

df = pd.read_csv("../data/Carbon-Emission.csv")
df = df.replace(np.nan, 'None')

def get_df_columns(df):
    
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    df_object = df.select_dtypes(include=['object'])

    return df_numeric.columns[:-1], df_object.columns


def calculate_carbon_emission(df):
    num_cols, obj_cols = get_df_columns(df)

    input_fields = {}

    for col in num_cols:
        input_fields[col] = st.number_input(f"Enter {col}", value=0)

        
    for col in obj_cols:
        input_fields[col] = st.selectbox(f"Select {col}", df[col].unique())

    # calculate the carbon emission
    return input_fields


entered_values = calculate_carbon_emission(df)

submit = st.button(":green[Calculate Carbon Emission]")

if submit:
    # ofc should actually calculate the carbon emission here
    # for now just print the entered values
    entered_values