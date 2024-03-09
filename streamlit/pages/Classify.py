import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

column_indexes = ['Body Type', 'Diet', 'How Often Shower', 'Heating Energy Source',
       'Transport', 'Social Activity', 'Monthly Grocery Bill',
       'Frequency of Traveling by Air', 'Vehicle Monthly Distance Km',
       'Waste Bag Size', 'Waste Bag Weekly Count',
       'How Many New Clothes Monthly']

st.set_page_config(
    page_title="MP4", 
    page_icon="🧊"
)

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

    df = df[column_indexes]

    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    df_object = df.select_dtypes(include=['object'])

    return df_numeric.columns, df_object.columns


def calculate_carbon_emission(df):
    num_cols, obj_cols = get_df_columns(df)



    input_fields = {}

    for col in num_cols:
        input_fields[col] = st.number_input(f"Enter {col}", value=0)

        
    for col in obj_cols:
        input_fields[col] = st.selectbox(f"Select {col}", df[col].unique())

    
    return input_fields


entered_values = calculate_carbon_emission(df)

submit = st.button(":green[Calculate Carbon Emission]")

def trans_value(category) -> str:
    dic = {
        0: 'Low',
        1: 'Medium',
        2: 'High',
        3: 'Very High'
    }
    return dic[category]
    

def get_numeric_df(df) -> pd.DataFrame:
     # Encode/transform data numeric
    label_encoder = LabelEncoder()

    # Making copy of df to a new dataframe called: df_numeric 
    df_numeric = df

    # Gettning all columns that has object type:
    cate_columns = df.select_dtypes(include=['object']).columns

    for column in cate_columns:
        df_numeric[column] = label_encoder.fit_transform(df[column])

    return df_numeric

if submit:
    # ofc should actually calculate the carbon emission here
    # for now just print the entered values
    loaded_model = pickle.load(open('../models/forest_model.pkl', 'rb'))
    df = pd.DataFrame(entered_values, index=[0])

    df = df[column_indexes]

    df_numeric = get_numeric_df(df)



    # Predicting the carbon emission
    prediction = loaded_model.predict(df_numeric)
    value = trans_value(prediction[0])
    st.write(f"**Your predicted carbon emission is {value}**")