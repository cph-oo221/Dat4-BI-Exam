import streamlit as st

st.set_page_config(
    page_title="BI Exam Project",
    page_icon="🧊",
    layout="wide",
)

banner = """
    <body style="background-color:yellow;">
            <div style="background-color:#385c7f ;padding:10px">
                <h2 style="color:white;text-align:center;">Analysis of carbon emissions, based on individual lifestyle factors</h2>
            </div>
    </body>
    """

st.markdown(banner, unsafe_allow_html=True)


st.markdown(
    """
    ###
        
    👈 :green[Select a demo case from the sidebar to experience some of what Streamlit can do for BI!]
    
    ### To learn more
    - Check out [Streamlit Documentation](https://docs.streamlit.io)
    - Contact me by [email](mailto://tdi@cphbusiness.dk)
"""
)