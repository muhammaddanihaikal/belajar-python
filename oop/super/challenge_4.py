class Produk:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_produk(self):
        print("nama : ", self.name)
        print("harga : ", self.price)
    
    def discount(self, percent):
        self.price = self.price - (self.price*percent/100)
    

class Mobil(Produk):

    def __init__(self,name, price, brand):
        # super().__init__(name, price)
        self.brand = brand
    
    def show_produk(self):
        super().show_produk()
        print("brand : ", self.brand)
    
    
brand1 = Mobil("Avanza", 250000000, "Toyota")
brand1.show_produk()

# Jawaban Challenge 4
# Muncul error:
# AttributeError: 'Mobil' object has no attribute 'name'

# Karena constructor parent tidak dijalankan
# (super().__init__(name, price) dihapus).

# Akibatnya self.name dan self.price tidak pernah dibuat.

# Saat super().show_produk() dijalankan,
# method tersebut mencoba mengakses self.name dan self.price,
# tetapi object Mobil belum memiliki kedua attribute itu.

# Ibaratnya fungsi show_produk() sudah ada,
# tapi bahan yang dibutuhkan (name & price) belum pernah dibuat,
# jadi fungsi tersebut gagal dijalankan.