class Product:

    def __init__(self, name):
        self.name = name


class Mobil(Product):

    def __init__(self, name, brand):
        self.brand = brand


mobil = Mobil("Avanza", "Toyota")

print(mobil.name)

# Jawaban

# 1. Error:
# AttributeError: 'Mobil' object has no attribute 'name'

# 2. Penyebab:
# Karena constructor parent (Product.__init__()) tidak pernah dipanggil.
# Akibatnya self.name tidak pernah dibuat.

# 3. Solusi:
# Tambahkan:
# super().__init__(name)
# di constructor Mobil agar constructor parent dijalankan.