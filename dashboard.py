import streamlit as st
from fsm import chatbot_diagram

def dashboard_page():

    st.markdown("""
    <div class="hero">
        <h1>Smartphone Store</h1>
        <p>
            E-Commerce Smartphone berbasis Streamlit dengan
            implementasi Finite State Machine (FSM) Chatbot
            untuk membantu proses pembelian produk.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <h2>12</h2>
            <p>Produk Tersedia</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        cart_count = len(st.session_state.get("cart", []))

        st.markdown(f"""
        <div class="stat-card">
            <h2>{cart_count}</h2>
            <p>Keranjang</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        total = sum(
            item["harga"]
            for item in st.session_state.get("cart", [])
        )

        st.markdown(f"""
        <div class="stat-card">
            <h2>Rp {total:,}</h2>
            <p>Total Belanja</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown("""
        <div class="banner-card">
            <h2>Promo Smartphone Terbaru</h2>
            <p>
                Dapatkan berbagai smartphone flagship dengan
                harga terbaik dan proses pembelian yang dibantu
                oleh FSM Chatbot.
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.image(
        "assets/xiaomi14.png",
        width=900
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.success(
        "Selamat datang di E-Commerce Smartphone. Silakan pilih menu di sidebar untuk memulai transaksi."
    )