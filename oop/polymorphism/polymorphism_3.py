class BasePage:

    def open(self):
        print("Open Base Page")


class LoginPage(BasePage):

    def open(self):
        super().open()
        print("Open Login Page")


login = LoginPage()
login.open()

# Pertanyaan 1 :
# Urutkan flow program berikut.

# A. print("Open Login Page")
# B. BasePage.open()
# C. LoginPage.open()
# D. print("Open Base Page")

# Jawaban :

# Urutan :
# C - B - D - A

# Urutan Lengkap :
# 1. LoginPage.open() dijalankan.
# 2. super().open() dipanggil.
# 3. BasePage.open() dijalankan.
# 4. print("Open Base Page")
# 5. Kembali ke LoginPage.open()
# 6. print("Open Login Page")

# ========================================================================

# Pertanyaan 2 :
# Apa output dari program tersebut?

# Jawaban :

# Output :
# Open Base Page
# Open Login Page

# ========================================================================

# Pertanyaan 3 :
# Kenapa output menjadi:

# Open Base Page
# Open Login Page

# Padahal kita hanya memanggil:
# login.open()

# Jawaban :
# Karena object yang dipanggil adalah LoginPage, maka Python
# menjalankan method open() milik LoginPage terlebih dahulu.
#
# Di dalam method tersebut terdapat super().open() yang
# memanggil method open() milik BasePage.
#
# Setelah BasePage.open() selesai dijalankan, program kembali
# ke LoginPage.open() untuk melanjutkan sisa kode yang ada,
# yaitu print("Open Login Page").