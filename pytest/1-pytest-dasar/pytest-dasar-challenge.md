# 🧠 Pytest Basic Challenge

> Tujuan:
>
> - Memahami struktur dasar pytest.
> - Memahami fungsi `assert`.
> - Memahami PASS dan FAIL.
> - Memahami cara menjalankan test.
> - Mulai berpikir seperti QA Automation Engineer.

---

# 🟢 Challenge 1 - Assertion Dasar

Buat file:

```text
tests/test_math.py
```

Buat 3 test berikut.

```python
def test_penjumlahan():
    ...

def test_pengurangan():
    ...

def test_perkalian():
    ...
```

## Kondisi

Pastikan ketiga test tersebut menggunakan `assert`.

Contoh:

```
2 + 3 = 5
10 - 5 = 5
5 * 5 = 25
```

---

## Pertanyaan

1. Berapa jumlah test yang berhasil dijalankan?
2. Apa output yang muncul di terminal?

---

### ✍️ Jawaban

```text
...
```

---

# 🟡 Challenge 2 - PASS & FAIL

Perhatikan kode berikut.

```python
def test_username():
    username = "admin"

    assert username == "admin"


def test_password():
    password = "123456"

    assert password == "password"
```

## Pertanyaan

1. Test mana yang PASS?
2. Test mana yang FAIL?
3. Kenapa bisa FAIL?
4. Kira-kira pesan error apa yang ditampilkan pytest?

> Jawab menggunakan bahasamu sendiri.

---

### 💡 Clue

Ingat...

`assert` digunakan untuk **memvalidasi** apakah kondisi bernilai **True**.

---

### ✍️ Jawaban

```text
...
```

---

# 🔴 Challenge 3 - Menjalankan Test

Perhatikan struktur project berikut.

```text
project/
│
├── tests/
│   ├── test_math.py
│   ├── test_login.py
│   └── test_product.py
│
└── pyproject.toml
```

Misalnya di dalam `test_math.py` terdapat:

```python
def test_penjumlahan():
    ...

def test_pengurangan():
    ...
```

## Pertanyaan

Tuliskan perintah terminal untuk:

1. Menjalankan semua test.
2. Menjalankan semua test dengan mode verbose.
3. Menjalankan hanya file `test_math.py`.
4. Menjalankan hanya test yang mengandung kata `penjumlahan`.

---

### ✍️ Jawaban

```text
...
```

---

# 🎯 Checklist

- [ ] Paham apa itu pytest.
- [ ] Paham fungsi `assert`.
- [ ] Paham perbedaan PASS dan FAIL.
- [ ] Bisa membaca hasil test di terminal.
- [ ] Bisa menjalankan test tertentu menggunakan pytest.

---

# 🚀 Goal

Kalau bisa menyelesaikan semua challenge ini tanpa melihat internet, berarti kamu sudah memiliki fondasi dasar pytest.

Setelah ini kamu siap belajar materi yang paling penting di pytest, yaitu:

⭐ **Fixture (`@pytest.fixture`)**

Karena hampir semua project Playwright menggunakan fixture untuk mengelola setup, teardown, browser, page, dan object yang digunakan dalam automation testing.
