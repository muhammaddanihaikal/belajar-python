class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Mobil(Product):

    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

mobil = Mobil(
    "Avanza",
    250000000,
    "Toyota"
)

# A. self.brand dibuat
# B. Product.__init__()
# C. Mobil.__init__()
# D. self.name dibuat
# E. self.price dibuat

# jawaban challenge 5 :

# Urutan :
# C → B → D → E → A

# Penjelasan:
# 1. Mobil.__init__() dijalankan.
#         ↓
# 2. super().__init__() dipanggil.
#         ↓
# 3. Product.__init__() dijalankan.
#         ↓
# 4. self.name & self.price dibuat.
#         ↓
# 5. Kembali ke Mobil.__init__().
#         ↓
# 6. self.brand dibuat.