class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, major):
        super().__init__(name)
        self.major = major


student = Student("Dani", "Informatika")

# Urutkan proses berikut :
# A. self.major dibuat
# B. Person.__init__()
# C. Student.__init__()
# D. self.name dibuat

# jawaban :
# Urutan :
# C - B - D - A

# Urutan Lengkap :
# 1. Student.__init__() dijalankan.
# 2. super().__init__() dipanggil.
# 3. Person.__init__() dijalankan.
# 4. self.name dibuat.
# 5. Kembali ke Student.__init__().
# 6. self.major dibuat.