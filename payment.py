import streamlit as st
from datetime import datetime

def payment_page():
    st.title("💳 Pembayaran")

    checkout_data = st.session_state.get("checkout_data", {})
    cart = st.session_state.get("cart", [])

    if not cart or not checkout_data.get("nama"):
        st.warning("Silakan lengkapi data checkout terlebih dahulu.")
        if st.button("📦 Ke Checkout"):
            st.session_state.nav_menu = "Checkout"
            st.session_state.page_transition = True
            st.rerun()
        return

    total = checkout_data.get("total", sum(item["harga"] for item in cart))

    with st.container(border=True):
        st.subheader("👤 Data Pemesan")
        st.write(f"**Nama:** {checkout_data.get('nama', '-')}")
        st.write(f"**Email:** {checkout_data.get('email', '-')}")
        st.write(f"**Telepon:** {checkout_data.get('telepon', '-')}")
        st.caption(f"📍 {checkout_data.get('alamat', '-')}")
        if checkout_data.get("catatan"):
            st.caption(f"📝 Catatan: {checkout_data.get('catatan')}")

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("🛒 Ringkasan Pesanan")
        for item in cart:
            col_img, col_info = st.columns([1, 3])
            with col_img:
                st.image(item.get("gambar", ""), width=60)
            with col_info:
                st.write(f"**{item['nama']}**")
                st.caption(f"Rp {item['harga']:,.0f}")

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #800020, #a0522d);
            color: white;
            padding: 14px 20px;
            border-radius: 14px;
            font-weight: 700;
            font-size: 1.1rem;
            text-align: center;
            margin-top: 12px;
            box-shadow: 0 4px 15px rgba(128, 0, 32, 0.4);
        ">
            💰 Total: Rp {total:,.0f}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("💳 Metode Pembayaran")

        metode = st.selectbox(
            "Pilih Metode",
            ["Transfer Bank", "QRIS", "E-Wallet"],
            index=["Transfer Bank", "QRIS", "E-Wallet"].index(
                checkout_data.get("metode", "Transfer Bank")
            )
        )

        st.session_state.checkout_data["metode"] = metode

        if metode == "Transfer Bank":
            st.info("🏦 **BCA**\nNo. Rekening: 1234567890\nAtas Nama: SmartPhone Store")
        elif metode == "QRIS":
            st.info("📱 Scan QRIS menggunakan aplikasi e-wallet atau mobile banking Anda.")
        else:
            st.info("📲 Dana / GoPay / OVO / ShopeePay\nNomor: 081234567890")

    st.markdown("<br>", unsafe_allow_html=True)

    if "paid" not in st.session_state:
        st.session_state.paid = False

    if not st.session_state.paid:
        col_kembali, col_bayar = st.columns(2)
        with col_kembali:
            if st.button("⬅️ Kembali ke Checkout", use_container_width=True):
                st.session_state.nav_menu = "Checkout"
                st.session_state.page_transition = True
                st.rerun()

        with col_bayar:
            if st.button("✅ Bayar Sekarang", type="primary", use_container_width=True):
                st.session_state.paid = True
                st.session_state.page_transition = True
                st.rerun()
    else:
        order = {
            "id": len(st.session_state.order_history) + 1,
            "tanggal": datetime.now().strftime("%d %B %Y, %H:%M"),
            "nama": checkout_data.get("nama", "-"),
            "email": checkout_data.get("email", "-"),
            "telepon": checkout_data.get("telepon", "-"),
            "alamat": checkout_data.get("alamat", "-"),
            "metode": checkout_data.get("metode", "-"),
            "items": [
                {"nama": item["nama"], "harga": item["harga"]}
                for item in cart
            ],
            "total": total,
            "status": "Berhasil",
        }

        st.session_state.order_history.append(order)

        st.session_state.cart.clear()
        st.session_state.checkout_data.clear()
        st.session_state.pop("paid", None)

        st.markdown("""
        <div style="
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            border: 2px solid #f59e0b;
        ">
            <div style="font-size: 3.5rem; margin-bottom: 12px;">🎉</div>
            <h2 style="color: #78350f; margin-bottom: 8px;">Pembayaran Berhasil!</h2>
            <p style="color: #78350f; font-size: 1.05rem;">Terima kasih, pesanan Anda sedang diproses.</p>
        </div>
        """, unsafe_allow_html=True)

        st.success(f"📋 No. Pesanan: #{order['id']}")
        st.caption(f"🕒 {order['tanggal']}")

        col_riwayat, col_baru = st.columns(2)

        with col_riwayat:
            if st.button("📜 Lihat Riwayat", use_container_width=True):
                st.session_state.nav_menu = "Riwayat"
                st.rerun()

        with col_baru:
            if st.button("🛒 Belanja Lagi", use_container_width=True):
                st.session_state.nav_menu = "Produk"
                st.rerun()
