class BasePage:

    def __init__(self, page):
        self.page = page


class LoginPage(BasePage):

    def __init__(self, page):
        # super().__init__(page)
        pass

    def login(self):
        self.page.goto("https://example.com")


login_page = LoginPage(page)
login_page.login()

# Pertanyaan :
# 1. Error apa yang kemungkinan muncul?
# 2. Kenapa error tersebut bisa terjadi?
# 3. Bagaimana cara memperbaikinya?

# Jawaban :
# aku ga tau nama errornya tapi kalo dilihat dari kodenya emang ga ada super di init login pagenya yang mana harusnya ada karena dia child dari base page, cara fixnya yaitu dengan menambahkan super.__init__(page)
# dan mungkin error satu lagi, ini ga ada kaitanya sm super sh, tapi emang harus import page dari playwright dulu biar dipake di class login kwkw

# perbaikan Chat GPT :
# Karena constructor parent (BasePage.__init__())
# tidak pernah dijalankan.

# Akibatnya self.page tidak pernah dibuat.

# Saat login() dijalankan,
# self.page.goto() mencoba memakai self.page,
# tetapi object LoginPage belum memiliki attribute tersebut.
