# 🧠 OOP Flow Challenge

> Tujuan:
>
> - Memahami alur eksekusi Constructor
> - Memahami kapan `super()` dipanggil
> - Memahami kapan attribute dibuat
> - Melatih cara berpikir saat debugging
> - Persiapan memahami Page Object Model (Playwright)

---

# 🟢 Challenge 1 - Flow Constructor

Perhatikan kode berikut.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, major):
        super().__init__(name)
        self.major = major


student = Student("Dani", "Informatika")
```

## Pertanyaan

Urutkan proses berikut.

```
A. self.major dibuat

B. Person.__init__()

C. Student.__init__()

D. self.name dibuat
```

### ✍️ Jawaban

```
...
```

---

# 🟡 Challenge 2 - Flow Method

Perhatikan kode berikut.

```python
class Product:

    def show(self):
        print("Product")


class Mobil(Product):

    def show(self):
        super().show()
        print("Mobil")


mobil = Mobil()
mobil.show()
```

## Pertanyaan

Urutkan proses berikut.

```
A. print("Mobil")

B. Mobil.show()

C. Product.show()

D. print("Product")
```

### 💡 Clue

Ingat...

```python
super().show()
```

bukan method parent,

melainkan **perintah untuk memanggil method parent**.

### ✍️ Jawaban

```
...
```

---

# 🔴 Challenge 3 - Debugging

Perhatikan kode berikut.

```python
class Product:

    def __init__(self, name):
        self.name = name


class Mobil(Product):

    def __init__(self, name, brand):
        self.brand = brand


mobil = Mobil("Avanza", "Toyota")

print(mobil.name)
```

## Pertanyaan

1. Error apa yang muncul?
2. Kenapa error tersebut bisa terjadi?
3. Bagaimana cara memperbaikinya?

> Jawab menggunakan bahasamu sendiri.

### 💡 Clue

Siapa yang membuat:

```python
self.name
```

Apakah constructor parent pernah dijalankan?

### ✍️ Jawaban

```
...
```

---

# 🟣 Challenge 4 - Flow Constructor (Playwright)

Perhatikan kode berikut.

```python
class BasePage:

    def __init__(self, page):
        self.page = page


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self):
        print("Login")


login_page = LoginPage(page)
```

## Pertanyaan

Urutkan proses berikut.

```
A. self.page dibuat

B. BasePage.__init__()

C. LoginPage.__init__()

D. login_page berhasil dibuat
```

### ✍️ Jawaban

```
...
```

---

## Pertanyaan Tambahan

Jawab menggunakan bahasamu sendiri.

1. Kapan `self.page` dibuat?
2. Kenapa method `login()` bisa menggunakan `self.page`, padahal `self.page` tidak ada di class `LoginPage`?

---

### 💡 Clue

Ingat...

```python
super().__init__(page)
```

hanya **memanggil constructor parent**.

Yang membuat:

```python
self.page
```

adalah siapa?

---

# 🟠 Challenge 5 - Debugging (Playwright)

Perhatikan kode berikut.

```python
class BasePage:

    def __init__(self, page):
        self.page = page


class LoginPage(BasePage):

    def __init__(self, page):
        pass

    def login(self):
        self.page.goto("https://example.com")


login_page = LoginPage(page)
login_page.login()
```

## Pertanyaan

1. Error apa yang kemungkinan muncul?
2. Kenapa error tersebut bisa terjadi?
3. Bagaimana cara memperbaikinya?

---

### 💡 Clue

Method berikut membutuhkan:

```python
self.page
```

Siapa yang membuat `self.page`?

Apakah constructor parent pernah dijalankan?

---

## 🚀 Bonus Challenge - Flow Program

Tanpa menjalankan program.

Lengkapi alur berikut.

```
LoginPage(page)
        │
        ▼
?
        │
        ▼
?
        │
        ▼
?
        │
        ▼
self.page dibuat
        │
        ▼
?
        │
        ▼
login() bisa menggunakan self.page
```

Isi semua tanda `?`.

---

# 🎯 Checklist

- [ ] Paham constructor dijalankan dari mana.
- [ ] Paham kapan `super()` dipanggil.
- [ ] Paham kapan attribute dibuat.
- [ ] Paham alur program dari child → parent → child.
- [ ] Bisa membaca flow program tanpa menjalankannya.
- [ ] Bisa menebak penyebab error sebelum debugging.
- [ ] Mulai memahami konsep BasePage & LoginPage di Playwright.

---

# 🚀 Goal

Kalau bisa menyelesaikan semua challenge ini tanpa melihat internet, berarti kamu sudah mulai terbiasa membaca **flow program**, bukan hanya menghafal sintaks.

Kemampuan ini akan sangat membantu saat belajar:

- Python OOP
- Pytest
- Playwright
- Page Object Model (POM)
- Debugging Automation Test
- Membangun framework automation yang rapi
