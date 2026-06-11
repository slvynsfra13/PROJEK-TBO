import streamlit as st
from products import cari_produk


def chatbot_page():

    st.title("🤖 Asisten Rekomendasi HP")

    if "state" not in st.session_state:
        st.session_state.state = "START"

    if st.session_state.state == "START":

        st.info(
            "Halo 👋 Saya akan membantu memilih HP yang sesuai kebutuhan Anda."
        )

        if st.button("Mulai Konsultasi"):

            st.session_state.state = "BUDGET"
            st.rerun()

    elif st.session_state.state == "BUDGET":

        st.subheader("💰 Budget")

        budget = st.number_input(
            "Masukkan budget Anda",
            min_value=1000000,
            step=500000
        )

        if st.button("Lanjut"):

            st.session_state.budget = budget
            st.session_state.state = "KEBUTUHAN"
            st.rerun()

    elif st.session_state.state == "KEBUTUHAN":

        kebutuhan = st.selectbox(
            "HP digunakan untuk apa?",
            [
                "Gaming",
                "Kamera",
                "Kuliah/Kerja",
                "Flagship"
            ]
        )

        if st.button("Lihat Rekomendasi"):

            st.session_state.kebutuhan = kebutuhan
            st.session_state.state = "REKOMENDASI"
            st.rerun()

    elif st.session_state.state == "REKOMENDASI":

        budget = st.session_state.budget
        kebutuhan = st.session_state.kebutuhan

        hasil = cari_produk(
            budget,
            kebutuhan
        )

        st.subheader("📱 Rekomendasi Untuk Anda")

        if len(hasil) == 0:

            st.warning(
                "Tidak ditemukan produk yang sesuai."
            )

        else:

            for hp in hasil:

                with st.container(border=True):

                    col1, col2 = st.columns([1, 2])

                    with col1:

                        st.image(
                            hp["gambar"],
                            width=180
                        )

                    with col2:

                        st.markdown(
                            f"## {hp['nama']}"
                        )

                        st.write(
                            hp["deskripsi"]
                        )

                        st.write(
                            f"⭐ Rating : {hp['rating']}"
                        )

                        st.write(
                            f"💾 RAM : {hp['ram']}"
                        )

                        st.write(
                            f"📦 Storage : {hp['storage']}"
                        )

                        st.write(
                            f"📸 Kamera : {hp['kamera']}"
                        )

                        st.write(
                            f"🔋 Baterai : {hp['baterai']}"
                        )

                        st.success(
                            f"Harga Rp {hp['harga']:,.0f}"
                        )

        if st.button("Konsultasi Lagi"):

            st.session_state.state = "START"
            st.rerun()
    elif st.session_state.state == "DETAIL":

        hp = st.session_state.selected_product

        st.title("📱 Detail Produk")

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(
                hp["gambar"],
                width=250
            )

        with col2:

            st.subheader(
                hp["nama"]
            )

            st.write(
                hp["deskripsi"]
            )

            st.write(
                f"RAM : {hp['ram']}"
            )

            st.write(
                f"Storage : {hp['storage']}"
            )

            st.write(
                f"Kamera : {hp['kamera']}"
            )

            st.write(
                f"Baterai : {hp['baterai']}"
            )

            st.success(
                f"Rp {hp['harga']:,.0f}"
            )

        if st.button("Checkout"):

            st.session_state.state = "CHECKOUT"
            st.rerun()
    elif st.session_state.state == "CHECKOUT":

        st.title("🛒 Checkout")

        nama = st.text_input(
            "Nama Pembeli"
        )

        alamat = st.text_area(
            "Alamat"
        )

        if st.button("Lanjut Pembayaran"):

            st.session_state.nama = nama
            st.session_state.alamat = alamat

            st.session_state.state = "PEMBAYARAN"
            st.rerun()
    elif st.session_state.state == "PEMBAYARAN":

        metode = st.selectbox(
            "Metode Pembayaran",
            [
                "Transfer Bank",
                "E-Wallet",
                "COD"
            ]
        )

        if st.button("Bayar"):

            st.session_state.metode = metode
            st.session_state.state = "SELESAI"
            st.rerun()
    elif st.session_state.state == "SELESAI":

        hp = st.session_state.selected_product

        st.balloons()

        st.success(
            "Pesanan Berhasil Dibuat"
        )

        st.write(
            f"Produk : {hp['nama']}"
        )

        st.write(
            f"Pembeli : {st.session_state.nama}"
        )

        st.write(
            f"Pembayaran : {st.session_state.metode}"
        )

        if st.button("Belanja Lagi"):

            keys = list(st.session_state.keys())

            for key in keys:
                del st.session_state[key]

            st.rerun()