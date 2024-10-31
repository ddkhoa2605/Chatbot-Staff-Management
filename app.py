import streamlit as st
from views import  login,register,home

def main():
    st.set_page_config(
    page_title="Chatbot staff management",
    page_icon="🤖",
    layout="wide"
)
    if 'page' not in st.session_state:
        st.session_state.page = "Login"  
    if st.session_state.page == "Login":
        login.show() 
    elif st.session_state.page == "Register":
        register.show() 
    elif st.session_state.page == "Home":
        home.show()  
if __name__ == "__main__":
    main()