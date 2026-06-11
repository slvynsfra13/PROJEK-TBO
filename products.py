PRODUCTS = [

    {
        "id": 1,
        "nama": "iPhone 15",
        "harga": 15000000,
        "kategori": ["Kamera", "Flagship"],
        "ram": "8 GB",
        "storage": "256 GB",
        "kamera": "48 MP",
        "baterai": "3349 mAh",
        "rating": 4.9,
        "gambar": "assets/iphone15.jpg",
        "deskripsi": "Performa premium dengan kamera berkualitas tinggi."
    },

    {
        "id": 2,
        "nama": "Samsung Galaxy S24",
        "harga": 13000000,
        "kategori": ["Kamera", "Flagship"],
        "ram": "8 GB",
        "storage": "256 GB",
        "kamera": "50 MP",
        "baterai": "4000 mAh",
        "rating": 4.8,
        "gambar": "assets/s24.jpg",
        "deskripsi": "Layar AMOLED dan kamera AI terbaik."
    },

    {
        "id": 3,
        "nama": "Xiaomi 14",
        "harga": 8000000,
        "kategori": ["Kuliah/Kerja"],
        "ram": "12 GB",
        "storage": "256 GB",
        "kamera": "50 MP",
        "baterai": "4610 mAh",
        "rating": 4.7,
        "gambar": "assets/xiaomi14.jpg",
        "deskripsi": "Performa tinggi untuk produktivitas harian."
    },

    {
        "id": 4,
        "nama": "ROG Phone 9",
        "harga": 12000000,
        "kategori": ["Gaming"],
        "ram": "16 GB",
        "storage": "512 GB",
        "kamera": "50 MP",
        "baterai": "5800 mAh",
        "rating": 4.9,
        "gambar": "assets/rog9.jpg",
        "deskripsi": "Gaming flagship dengan refresh rate tinggi."
    }
]


def cari_produk(budget, kebutuhan):

    hasil = []

    for produk in PRODUCTS:

        if (
            produk["harga"] <= budget
            and kebutuhan in produk["kategori"]
        ):
            hasil.append(produk)

    return hasil