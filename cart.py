import streamlit as st

def cart_page():
    st.title("🛒 Keranjang Belanja")

    cart = st.session_state.get("cart", [])

    if not cart:
        st.markdown("""
        <div style="
            text-align: center;
            padding: 60px 20px;
            background: white;
            border-radius: 24px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        ">
            <div style="font-size: 4rem; margin-bottom: 16px;">🛒</div>
            <h2 style="color: #1e293b; margin-bottom: 8px;">Keranjang Masih Kosong</h2>
            <p style="color: #64748b;">Yuk, lihat katalog produk dan tambahkan HP favoritmu!</p>
        </div>
        """, unsafe_allow_html=True)

        return

    st.subheader(f"📦 {len(cart)} Produk di Keranjang")

    total = 0

    for idx, item in enumerate(cart):
        with st.container(border=True):
            col_img, col_info, col_action = st.columns([1, 2, 1])

            with col_img:
                st.image(item.get("gambar", ""), width=90)

            with col_info:
                st.markdown(f"### {item['nama']}")
                st.caption(item.get("deskripsi", ""))
                st.markdown(
                    f"""
                    <div class="price-badge" style="display:inline-block; margin:0;">
                        Rp {item['harga']:,.0f}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col_action:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button(
                    "🗑️ Hapus",
                    key=f"remove_{idx}_{item['id']}",
                    use_container_width=True
                ):
                    st.session_state.cart.pop(idx)
                    st.session_state.page_transition = not st.session_state.get("page_transition", False)
                    st.rerun()

            total += item["harga"]

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #800020, #a0522d);
            color: white;
            padding: 14px 20px;
            border-radius: 14px;
            font-weight: 700;
            font-size: 1.1rem;
            text-align: center;
            margin: 20px 0 16px;
            box-shadow: 0 4px 15px rgba(128, 0, 32, 0.4);
        ">
            💰 Total Belanja: Rp {total:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

    col_checkout, col_clear = st.columns(2)

    with col_checkout:
        if st.button("💳 Lanjut ke Checkout", type="primary", use_container_width=True):
            st.session_state.nav_menu = "Checkout"
            st.session_state.page_transition = not st.session_state.get("page_transition", False)
            st.rerun()

    with col_clear:
        if st.button("🗑️ Kosongkan Keranjang", use_container_width=True):
            st.session_state.cart = []
            st.session_state.nav_menu = "Keranjang"
            st.session_state.page_transition = not st.session_state.get("page_transition", False)
            st.rerun()