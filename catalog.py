import streamlit as st
from products import PRODUCTS

if "cart" not in st.session_state:
    st.session_state.cart = []


def catalog_page():

    st.title("📱 Katalog Produk")

    cols = st.columns(2)

    for i, hp in enumerate(PRODUCTS):

        with cols[i % 2]:

            with st.container(border=True):

                st.image(
                hp["gambar"],
                width=250
                )

            st.subheader(
                hp["nama"]
            )

            st.caption(
                hp["deskripsi"]
            )

            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #2563eb, #7c3aed);
                    color: white;
                    padding: 10px 16px;
                    border-radius: 12px;
                    font-weight: 700;
                    font-size: 16px;
                    text-align: center;
                    margin: 10px 0;
                ">
                    Rp {hp['harga']:,.0f}
                    <br>
                    <small style="opacity:0.9">⭐ {hp['rating']}</small>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "🛒 Tambah ke Keranjang",
                key=f"cart_{hp['id']}",
                use_container_width=True
            ):

                if hp not in st.session_state.cart:
                    st.session_state.cart.append(hp)

                    st.toast(
                        f"✅ {hp['nama']} ditambahkan ke keranjang",
                        icon="✅"
                    )
                else:
                    st.toast(
                        f"⚠️ {hp['nama']} sudah ada di keranjang",
                        icon="⚠️"
                    )