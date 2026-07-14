class Product:

    def show(self):
        print("Product")


class Mobil(Product):

    def show(self):
        super().show()
        print("Mobil")


mobil = Mobil()
mobil.show()


# Urutkan proses berikut :
# A. print("Mobil")
# B. Mobil.show()
# C. Product.show()
# D. print("Product")

# jawaban :
# B - C - D - A

# Urutan lengkap
# 1. Mobil.show() dijalankan
# 2. super().show() dipanggil
# 3. Product.show() dijalankan
# 4. print("Product")
# 5. kembali ke Mobil.show()
# 6. print("Mobil")