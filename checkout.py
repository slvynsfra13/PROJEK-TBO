import streamlit as st

def checkout_page():
    st.title("📦 Checkout")

    checkout_data = st.session_state.get("checkout_data", {})

    cart = st.session_state.get("cart", [])

    if not cart:
        st.warning("Keranjang masih kosong. Silakan tambahkan produk terlebih dahulu.")
        if st.button("🛒 Lihat Katalog"):
            st.session_state.nav_menu = "Produk"
            st.rerun()
        return

    with st.container(border=True):
        st.subheader("📋 Detail Pesanan")

        nama = st.text_input("Nama Lengkap *", value=checkout_data.get("nama", ""))
        email = st.text_input("Email *", value=checkout_data.get("email", ""))
        alamat = st.text_area("Alamat Pengiriman *", value=checkout_data.get("alamat", ""), height=100)
        telepon = st.text_input("Nomor Telepon *", value=checkout_data.get("telepon", ""))
        catatan = st.text_area("Catatan Tambahan (Opsional)", value=checkout_data.get("catatan", ""), height=80)

        st.session_state.checkout_data = {
            "nama": nama,
            "email": email,
            "alamat": alamat,
            "telepon": telepon,
            "catatan": catatan,
        }

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("🛒 Ringkasan Belanja")

        total = 0
        for item in cart:
            col_img, col_info = st.columns([1, 3])
            with col_img:
                st.image(item.get("gambar", ""), width=60)
            with col_info:
                st.write(f"**{item['nama']}**")
                st.caption(f"Rp {item['harga']:,.0f}")
            total += item["harga"]

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

    col_kembali, col_lanjut = st.columns(2)

    with col_kembali:
        if st.button("⬅️ Kembali ke Keranjang", use_container_width=True):
            st.session_state.nav_menu = "Keranjang"
            st.session_state.page_transition = True
            st.rerun()

    with col_lanjut:

        lanjut_disabled = not (
            nama.strip()
            and email.strip()
            and alamat.strip()
            and telepon.strip()
        )

        if st.button(
            "💳 Lanjut ke Pembayaran",
            type="primary",
            use_container_width=True,
            disabled=lanjut_disabled
        ):

            st.session_state.checkout_data["total"] = total

            st.session_state.checkout_data["items"] = (
                st.session_state.cart.copy()
            )

            st.session_state.nav_menu = "Pembayaran"
            st.session_state.page_transition = True

            st.toast(
                "✅ Data checkout tersimpan. Lanjut ke pembayaran.",
                icon="✅"
            )

            st.rerun()