class Produk:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_produk(self):
        print("nama : ", self.name)
        print("harga : ", self.price)
    

class Mobil(Produk):

    def __init__(self,name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    
    def show_produk(self):
        super().show_produk()
        print("brand : ", self.brand)

brand1 = Mobil("Avanza", "250000000", "Toyota")
brand1.show_produk()
