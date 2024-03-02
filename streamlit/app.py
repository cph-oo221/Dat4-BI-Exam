import streamlit as st

st.set_page_config(
    page_title="BI Exam Project",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:tdi@cphbusiness.dk',
        'About': "https://docs.streamlit.io"
    }
)

st.sidebar.header("Menu Options", divider=True)

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
    ### Discritption of the project:    
    
    "Since carbon emissions have such a big impact on the greenhouse effect, every caution must be made to try and minimize these as mush as possible.
    In this analysis we will try to identify patterns in normal individual peoples 
    lifestyle factors, that contribute to their total carbon emissions, to make people more aware of how their lifestyle affects the climate."
    
    ### Check out
    - [Carbon Emissions Calculator](/Calculate)
"""
)