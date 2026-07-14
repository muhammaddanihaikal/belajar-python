class BasePage:

    def open(self):
        print("Open Base Page")


class LoginPage(BasePage):

    def open(self):
        print("Open Login Page")


login = LoginPage()

login.open()

# Pertanyaan :
# 1. Outputnya apa?
# 2. Kenapa yang dipanggil bukan method milik `BasePage`?

# Jawaban :
# 1. Output:
# Open Login Page

# 2. Karena LoginPage memiliki method open() sendiri yang meng-override method open() milik BasePage.

# Saat object LoginPage memanggil open(),
# Python akan mencari method tersebut di LoginPage terlebih dahulu.
# Karena ketemu, Python tidak menjalankan method open() milik BasePage.