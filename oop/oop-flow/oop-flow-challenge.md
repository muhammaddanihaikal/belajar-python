# 🧠 OOP Flow Challenge

> Tujuan:
>
> - Memahami alur eksekusi Constructor
> - Memahami kapan `super()` dipanggil
> - Memahami kapan attribute dibuat
> - Melatih cara berpikir saat debugging

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

# 🎯 Checklist

- [ ] Paham constructor dijalankan dari mana.
- [ ] Paham kapan `super()` dipanggil.
- [ ] Paham kapan attribute dibuat.
- [ ] Paham alur program dari child → parent → child.
- [ ] Bisa menebak penyebab error tanpa menjalankan program.

---

# 🚀 Goal

Kalau bisa menyelesaikan 3 challenge ini tanpa melihat internet, berarti kamu sudah mulai terbiasa membaca **flow program**, bukan hanya menghafal sintaks.

Kemampuan ini akan sangat membantu saat belajar:

- Playwright
- Pytest
- Page Object Model (POM)
- Debugging automation test
