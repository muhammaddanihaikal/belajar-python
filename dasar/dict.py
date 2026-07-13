# membuat dict
produk = {
    "nama" : "avanza",
    "harga" : 20000000,
    "stok" : 10
}

# 1. print nama produk
print("nama produk : ", produk["nama"])

# 2. print harga
print("harga : ", produk["harga"])

# 3. ubah stok menjadi 20
produk["stok"] = 20

# 4. tambahkan kategori
produk["warna"] = "hitam"

# 5. hapus kategori
del produk["warna"]

# 6. Loop semua data produk
for key, value in produk.items():
    print(key,value)