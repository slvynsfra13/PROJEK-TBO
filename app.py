import os
import streamlit as st
from datetime import datetime

from login import login_page
from dashboard import dashboard_page
from catalog import catalog_page
from cart import cart_page
from chatbot import chatbot_page
from checkout import checkout_page
from payment import payment_page
from history import history_page

st.set_page_config(
    page_title="SmartPhone Store",
    page_icon="📱",
    layout="wide"
)

css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "login" not in st.session_state:
    st.session_state.login = False

if "cart" not in st.session_state:
    st.session_state.cart = []

if "order_history" not in st.session_state:
    st.session_state.order_history = []

if "checkout_data" not in st.session_state:
    st.session_state.checkout_data = {}

if "nav_menu" not in st.session_state:
    st.session_state.nav_menu = "Dashboard"

if "_last_page" not in st.session_state:
    st.session_state._last_page = "Dashboard"

if not st.session_state.login:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"]{
        display:none;
    }
    </style>
    """, unsafe_allow_html=True)
    login_page()
else:
    with st.sidebar:
        st.markdown("""
        <div style="
            text-align:center;
            padding:24px 20px;
            border-radius:18px;
            background:linear-gradient(135deg,#800020,#a0522d);
            color:white;
            margin-bottom:20px;
            box-shadow:0 6px 24px rgba(128,0,32,0.4),inset 0 1px 0 rgba(255,255,255,0.18);
        ">
            <h2 style="margin:0 0 6px;font-size:1.3rem;font-weight:800;letter-spacing:-0.3px;">SmartPhone Store</h2>
            <p style="margin:0;opacity:0.92;font-size:0.95rem;font-weight:500;">Temukan HP Terbaikmu</p>
        </div>
        """, unsafe_allow_html=True)

        current_option = st.session_state.get("nav_menu", "Dashboard")
        page_options = [
            "Dashboard",
            "Produk",
            "Chatbot AI",
            "Keranjang",
            "Checkout",
            "Pembayaran",
            "Riwayat"
        ]
        radio_index = page_options.index(current_option) if current_option in page_options else 0

        st.radio(
            "",
            page_options,
            index=radio_index,
            key="nav_radio"
        )
        st.session_state.nav_menu = st.session_state["nav_radio"]

        st.divider()

        st.subheader("🛒 Keranjang")

        total = 0
        for item in st.session_state.cart:
            st.markdown(f"<div class='sidebar-cart-item'>• {item['nama']}</div>", unsafe_allow_html=True)
            total += item["harga"]

        if total > 0:
            st.markdown(f"<div class='sidebar-cart-total'>Rp {total:,.0f}</div>", unsafe_allow_html=True)

        st.divider()

        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.login = False

            st.session_state.cart = []
            st.session_state.checkout_data = {}
            st.session_state.menu_override = None

            st.rerun()

    current_page = st.session_state.nav_menu
    prev_page = st.session_state._last_page

    if current_page != prev_page:
        st.session_state._last_page = current_page
        anim_class = "app-page-enter"
    else:
        anim_class = ""

    st.markdown(f'<div class="{anim_class}">', unsafe_allow_html=True)

    if current_page == "Dashboard":
        dashboard_page()
    elif current_page == "Produk":
        catalog_page()
    elif current_page == "Chatbot AI":
        chatbot_page()
    elif current_page == "Keranjang":
        cart_page()
    elif current_page == "Checkout":
        checkout_page()
    elif current_page == "Pembayaran":
        payment_page()
    elif current_page == "Riwayat":
        history_page()

    st.markdown("</div>", unsafe_allow_html=True)