import streamlit as st
import time
from streamlit_option_menu import option_menu
from views import chat, model, geo
from streamlit_option_menu import option_menu

def show():
    side_bar_options_style = {
        "container": {"padding": "0!important", "background-color": 'transparent'},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin": "0px", "margin-bottom": "15px"},
        "nav-link-selected": {"background-color": "#7B06A6", "font-size": "15px"},
    }
    with st.sidebar:
        st.title("Prediction Apps")
        page = option_menu(
            menu_title=None,
            options=['Chatbot', 'Geospatial visualization',
                     'Predict'],
            icons=['diagram-3-fill', 'bar-chart-line-fill',
                   "graph-up-arrow", "cpu"],

            menu_icon="cast",
            default_index=0,
            styles=side_bar_options_style
        )
    # Page content based on selection
    if page == "Chatbot":
        chat.show()
    elif page == "Geospatial visualization":
        geo.app()
    elif page == "Predict":
        model.show()

