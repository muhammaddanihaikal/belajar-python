# 🧠 OOP Polymorphism Challenge

> Tujuan:
>
> - Memahami apa itu Polymorphism
> - Memahami Method Overriding
> - Memahami bagaimana Python memilih method yang dijalankan
> - Persiapan memahami Page Object Model (Playwright)

---

# 🟢 Challenge 1 - Basic Polymorphism

Perhatikan kode berikut.

```python
class Product:

    def show(self):
        print("Ini Product")


class Mobil(Product):

    def show(self):
        print("Ini Mobil")


mobil = Mobil()

mobil.show()
```

## Pertanyaan

1. Outputnya apa?
2. Kenapa yang dijalankan adalah `show()` milik `Mobil`, bukan milik `Product`?

> Jawab menggunakan bahasamu sendiri.

---

### 💡 Clue

`Mobil` memiliki method dengan nama yang sama seperti `Product`.

Python akan memilih method milik class mana?

---

### ✍️ Jawaban

```
...
```

---

# 🟣 Challenge 2 - Playwright Polymorphism

Perhatikan kode berikut.

```python
class BasePage:

    def open(self):
        print("Open Base Page")


class LoginPage(BasePage):

    def open(self):
        print("Open Login Page")


login = LoginPage()

login.open()
```

## Pertanyaan

1. Outputnya apa?
2. Kenapa yang dipanggil bukan method milik `BasePage`?

---

### 💡 Clue

Method dengan nama yang sama di child akan...

```
...
```

---

### ✍️ Jawaban

```
...
```

---

# 🔴 Challenge 3 - Playwright + super()

Perhatikan kode berikut.

```python
class BasePage:

    def open(self):
        print("Open Base Page")


class LoginPage(BasePage):

    def open(self):
        super().open()
        print("Open Login Page")


login = LoginPage()

login.open()
```

## Pertanyaan 1

Urutkan flow program berikut.

```
A. print("Open Login Page")

B. BasePage.open()

C. LoginPage.open()

D. print("Open Base Page")
```

### ✍️ Jawaban

```
...
```

---

## Pertanyaan 2

Apa output dari program tersebut?

### ✍️ Jawaban

```
...
```

---

## Pertanyaan 3

Kenapa output menjadi:

```
Open Base Page
Open Login Page
```

Padahal kita hanya memanggil:

```python
login.open()
```

> Jawab menggunakan bahasamu sendiri.

---

### 💡 Clue

Ingat...

```python
super().open()
```

tidak menjalankan method parent secara otomatis,

melainkan **memanggil method parent** terlebih dahulu.

---

# 🎯 Checklist

- [ ] Paham apa itu Polymorphism.
- [ ] Paham Method Overriding.
- [ ] Paham kenapa child dapat mengganti perilaku parent.
- [ ] Paham kapan `super()` diperlukan.
- [ ] Bisa membaca flow program tanpa menjalankannya.
- [ ] Siap memahami struktur BasePage & LoginPage di Playwright.

---

# 🚀 Goal

Kalau bisa menyelesaikan semua challenge ini tanpa melihat internet, berarti kamu sudah memahami tiga konsep OOP yang paling sering digunakan dalam Automation Testing:

- ✅ Inheritance
- ✅ Method Overriding (Polymorphism)
- ✅ super()

Setelah materi ini, kamu akan jauh lebih siap mempelajari:

- Playwright Page Object Model (POM)
- BasePage
- LoginPage
- DashboardPage
- Framework Automation Testing
