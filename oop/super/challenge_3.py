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
        super().__init__(name, price)
        self.brand = brand
    
    def show_produk(self):
        super().show_produk()
        print("brand : ", self.brand)
    
    
brand1 = Mobil("Avanza", 250000000, "Toyota")
print(brand1.name)


# Jawaban Challenge 3 :
# Kenapa mobil.name bisa dipanggil?

# Karena di constructor class Mobil ada super().__init__(name, price).

# super() akan memanggil constructor parent (Produk),
# lalu parent membuat self.name dan self.price.

# Jadi walaupun di class Mobil tidak ada
# self.name = name,
# object Mobil tetap memiliki attribute name
# karena attribute tersebut sudah dibuat oleh parent.
