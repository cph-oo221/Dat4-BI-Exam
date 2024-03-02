import streamlit as st
import pandas as pd

st.set_page_config(page_title="MP4", page_icon="🧊")

st.sidebar.header("Menu Options", divider=True)


st.markdown(
    """
    
    ### Calculate Carbon Emissions from Lifestyle Factors:

    """
)

df = pd.read_csv("../data/Carbon-Emission.csv")

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

submit = st.button("Calculate Carbon Emission")

if submit:
    entered_values