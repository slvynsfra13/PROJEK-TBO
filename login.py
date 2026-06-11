import streamlit as st

def login_page():
    st.title("🔐 Login")

    with st.container():
        col1, col2, col3 = st.columns([1, 2.2, 1])
        with col2:
            username = st.text_input("Username", max_chars=30)
            password = st.text_input("Password", type="password", max_chars=30)

            if st.button("Login", use_container_width=True):
                if username == "admin" and password == "123":
                    st.session_state.login = True
                    st.success("Login Berhasil")
                    st.rerun()
                else:
                    st.error("Username atau Password Salah")