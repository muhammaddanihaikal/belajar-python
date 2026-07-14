class Product:

    def show(self):
        print("Ini Product")


class Mobil(Product):

    def show(self):
        print("Ini Mobil")


mobil = Mobil()

mobil.show()

# Pertanyaan :
# 1. Outputnya apa?
# 2. Kenapa yang dijalankan adalah `show()` milik `Mobil`, bukan milik `Product`?

# Jawaban :

# 1. Output:
# Ini Mobil

# 2. Karena object yang dibuat adalah Mobil.
# Class Mobil memiliki method show() sendiri yang menimpa (override) method show() milik Product.
# Oleh karena itu Python menjalankan method show() milik Mobil.