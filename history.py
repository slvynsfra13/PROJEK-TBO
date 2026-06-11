import streamlit as st

def history_page():
    st.title("📜 Riwayat Transaksi")

    history = st.session_state.get("order_history", [])

    if not history:
        st.markdown("""
        <div style="
            text-align: center;
            padding: 50px 20px;
            background: white;
            border-radius: 24px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        ">
            <div style="font-size: 4rem; margin-bottom: 16px;">📭</div>
            <h3 style="color: #1e293b;">Belum Ada Transaksi</h3>
            <p style="color: #64748b;">Riwayat pembelian akan muncul di sini setelah Anda checkout dan bayar.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🛒 Mulai Belanja"):
            st.session_state.nav_menu = "Produk"
            st.rerun()
        return

    for order in reversed(history):
        with st.container(border=True):
            col_header, col_status = st.columns([3, 1])

            with col_header:
                st.subheader(f"📦 Pesanan #{order['id']}")
                st.caption(f"🕒 {order['tanggal']}")
                st.write(f"**👤 {order['nama']}**")
                st.caption(f"📍 {order['alamat']}")
                st.caption(f"📞 {order['telepon']}")

            with col_status:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #10b981, #059669);
                    color: white;
                    padding: 12px 16px;
                    border-radius: 12px;
                    text-align: center;
                    font-weight: 700;
                    font-size: 0.9rem;
                    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.35);
                    margin-top: 24px;
                ">
                    ✅ {order['status']}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("📋 Detail Items")

            for item in order["items"]:
                col_item, col_price = st.columns([3, 1])
                with col_item:
                    st.write(f"• {item['nama']}")
                with col_price:
                    st.caption(f"Rp {item['harga']:,.0f}")

            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #800020, #a0522d);
                color: white;
                padding: 12px 20px;
                border-radius: 14px;
                font-weight: 700;
                font-size: 1.05rem;
                text-align: right;
                margin-top: 10px;
                box-shadow: 0 4px 15px rgba(128, 0, 32, 0.4);
            ">
                💰 Total: Rp {order['total']:,.0f}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.08);
                border-radius: 10px;
                padding: 10px 14px;
                margin-top: 10px;
                font-size: 0.85rem;
                border: 1px solid rgba(255,255,255,0.1);
            ">
                💳 Metode: <strong>{order['metode']}</strong>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🛒 Belanja Lagi", use_container_width=True):
        st.session_state.nav_menu = "Produk"
        st.rerun()