import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler



column_indexes = ['Body Type', 'Sex', 'Diet', 'How Often Shower', 'Heating Energy Source',
       'Transport', 'Vehicle Type', 'Social Activity', 'Monthly Grocery Bill',
       'Frequency of Traveling by Air', 'Vehicle Monthly Distance Km',
       'Waste Bag Size', 'Waste Bag Weekly Count', 'How Long TV PC Daily Hour',
       'How Many New Clothes Monthly', 'How Long Internet Daily Hour',
       'Energy efficiency', 'Recycling', 'Cooking_With']

st.set_page_config(
    page_title="ANN", 
    page_icon="🧊"
)

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

df_loaded = pd.read_csv("../data/Carbon-Emission.csv")
df_loaded = df_loaded.replace(np.nan, 'None')

# df_loaded_encoded = df_loaded.copy()

# label_encoder = LabelEncoder()
# cate_columns = df_loaded.select_dtypes(include=['object']).columns

# for column in cate_columns:
#     df_loaded_encoded[column] = label_encoder.fit_transform(df_loaded[column])

def get_df_columns(df):

    df = df.drop('CarbonEmission', axis=1)

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


entered_values = calculate_carbon_emission(df_loaded)

submit = st.button(":green[Calculate Carbon Emissions]")
    

def get_numeric_df(df) -> pd.DataFrame:
    # Encode/transform data numeric
    encoder = pickle.load(open('../models/encoder.pkl', 'rb')) # Does not work??

    # Making copy of df to a new dataframe called: df_numeric 
    df_numeric = df.copy()

    cate_columns = ['Body Type', 'Sex', 'Diet', 'How Often Shower', 'Heating Energy Source',
       'Transport', 'Vehicle Type', 'Social Activity',
       'Frequency of Traveling by Air', 'Waste Bag Size', 'Energy efficiency',
       'Recycling', 'Cooking_With']

    df_numeric[cate_columns] = encoder.transform(df[cate_columns])

    return df_numeric

if submit:
    loaded_model = pickle.load(open('../models/nn_model.pkl', 'rb'))
    loaded_scaler = pickle.load(open('../models/scaler.pkl', 'rb'))
    df = pd.DataFrame(entered_values, index=[0])

    df = df[column_indexes]

    df_numeric = get_numeric_df(df)

    X = loaded_scaler.transform(df_numeric.values)

    # Predicting the carbon emissions
    prediction = loaded_model.predict(X)
    # value = trans_value(prediction[0])
    st.write(f"**Your predicted carbon emission is:**\n")
    st.write(f"### :blue[{(prediction[0,0] / 12)} in kg CO2 per month]")