class BasePage:

    def __init__(self, page):
        self.page = page


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self):
        print("Login")


login_page = LoginPage(page)

# urutkan proses berikut :
# A. self.page dibuat
# B. BasePage.__init__()
# C. LoginPage.__init__()
# D. login_page berhasil dibuat

# jawaban :
 
# Urutan :
# C - B - A - D

# Urutan Lengkap :
# 1. LoginPage.__init__() dijalankan
# 2. super().__init__() dipanggil
# 3. BasePage.__init__() dijalankan
# 4. self.page dibuat
# 5. kembali ke LoginPage.__init__()
# 6. login_page berhasil dibuat