import streamlit as st

def navigate(page):
    if "nav_menu" in st.session_state:
        st.session_state.nav_menu = page
    st.session_state.transition_flash = not st.session_state.get("transition_flash", False)
    st.rerun()