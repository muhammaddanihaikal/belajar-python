# 🧠 OOP Challenge - Inheritance & `super()`

> Tujuan:
>
> - Memahami Inheritance
> - Memahami `super()`
> - Memahami Parent & Child
> - Memahami alur Constructor

---

# 🟢 Challenge 1 - Parent & Child

## Parent

Buat class:

```python
Product
```

### Attribute

- name
- price

### Method

```python
show_product()
```

Output contoh:

```
Nama  : Avanza
Harga : 250000000
```

---

## Child

Buat class:

```python
Mobil(Product)
```

### Attribute tambahan

- brand

Gunakan:

```python
super().__init__(...)
```

Tambahkan method:

```python
show_brand()
```

---

## Tugas

Buat object:

```text
Nama  : Avanza
Harga : 250000000
Brand : Toyota
```

Kemudian tampilkan:

```
Nama  : Avanza
Harga : 250000000
Brand : Toyota
```

---

### 💡 Clue

Parent menerima:

```python
(name, price)
```

Child menerima:

```python
(?, ?, ?)
```

Pikirkan parameter apa saja yang harus diterima child.

---

# 🟡 Challenge 2 - Menggunakan Method Parent

Tambahkan method pada parent:

```python
discount(percent)
```

Method tersebut menghitung harga setelah diskon.

Contoh:

```
Harga Awal

250000000

↓

Diskon 10%

↓

225000000
```

## Tugas

Panggil method tersebut dari object `Mobil`.

> Jangan membuat ulang method `discount()` di child.

---

### 💡 Clue

Karena `Mobil` mewarisi `Product`, apakah method parent bisa langsung dipanggil?

---

# 🟠 Challenge 3 - Pemahaman `super()`

Setelah object dibuat, coba tampilkan:

```python
mobil.name
mobil.price
mobil.brand
```

## Pertanyaan

Kenapa

```python
mobil.name
```

bisa dipanggil,

padahal di class `Mobil` kamu **tidak pernah menulis**

```python
self.name = name
```

Jawab menggunakan bahasamu sendiri (1–2 kalimat).

---

# 🔴 Challenge 4 - Hapus `super()`

Hapus kode berikut:

```python
super().__init__(name, price)
```

Lalu jalankan:

```python
mobil.show_product()
```

## Pertanyaan

1. Error apa yang muncul?
2. Kenapa bisa terjadi?

---

### 💡 Clue

Siapa yang sebenarnya membuat:

```python
self.name
self.price
```

---

# 🔥 Challenge 5 - Urutan Eksekusi

Perhatikan kode berikut.

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Mobil(Product):

    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
```

Object dibuat:

```python
mobil = Mobil(
    "Avanza",
    250000000,
    "Toyota"
)
```

## Urutkan proses berikut.

```
A. self.brand dibuat

B. Product.__init__()

C. Mobil.__init__()

D. self.name dibuat

E. self.price dibuat
```

Tulis urutannya.

---

# 🎯 Checklist

- [ ] Paham Parent
- [ ] Paham Child
- [ ] Paham Inheritance
- [ ] Paham `super()`
- [ ] Paham Constructor
- [ ] Paham kenapa Child tetap menerima parameter Parent
- [ ] Paham alur object → child → parent

---

## 🚀 Bonus Challenge

Tambahkan method berikut pada parent:

```python
show_product()
```

Kemudian di child buat method dengan nama yang sama.

Di dalam method child:

1. Panggil method parent menggunakan:

```python
super().show_product()
```

2. Setelah itu tampilkan:

```
Brand : Toyota
```

### Pertanyaan

Mengapa hasil akhirnya menampilkan:

```
Nama
Harga
Brand
```

padahal method parent hanya menampilkan:

```
Nama
Harga
```

> Jawab menggunakan bahasamu sendiri tanpa melihat internet.
