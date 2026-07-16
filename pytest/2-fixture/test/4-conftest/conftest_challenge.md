# 🧠 Pytest conftest.py Challenge

---

# 🟢 Challenge 1 - Flow conftest.py

Perhatikan struktur project berikut.

```text
tests/
│
├── conftest.py
└── test_login.py
```

### conftest.py

```python
import pytest

@pytest.fixture
def user():
    return "Dani"
```

### test_login.py

```python
def test_login(user):
    assert user == "Dani"
```

## Pertanyaan

1. Kenapa fixture `user` bisa digunakan tanpa di-import?
2. Siapa yang mencari fixture tersebut?
3. Jelaskan flow programnya.

---

### ✍️ Jawaban

```text
1. karena pytest akan mencari fixture secara otomatis dimanapun itu, salah satunya di conftest.py
2. yang mencari adalah pytest
3. flow :
# Flow Program :

# 1. Pytest menjalankan test_login(user).
# 2. Pytest melihat bahwa test membutuhkan fixture 'user'.
# 3. Pytest mencari fixture 'user'.
# 4. Pytest menemukan fixture tersebut di conftest.py.
# 5. Pytest menjalankan fixture user().
# 6. Fixture mengembalikan nilai "Dani".
# 7. Nilai tersebut diisikan ke parameter user.
# 8. assert user == "Dani" dijalankan.
# 9. Assertion bernilai True sehingga test PASS.
```

---

# 🟡 Challenge 2 - Kenapa conftest.py?

Misalnya ada tiga file berikut.

```text
tests/
│
├── test_login.py
├── test_product.py
└── test_checkout.py
```

Semuanya membutuhkan fixture:

```python
browser
```

## Pertanyaan

1. Kenapa lebih baik fixture `browser` disimpan di `conftest.py`?
2. Apa keuntungan dibanding menulis fixture di setiap file?

---

### ✍️ Jawaban

```text
Jawaban :

1. Karena browser dipakai di banyak file test,
jadi lebih enak ditaruh di conftest.py supaya tinggal dipakai.

2. Keuntungannya:
- Tidak perlu menulis fixture browser berulang-ulang.
- Kodenya lebih rapi.
- Kalau ada perubahan, cukup ubah di satu tempat.
```

---

# 🔴 Challenge 3 - Pemahaman Konsep

Jawab menggunakan bahasamu sendiri.

1. Apa fungsi utama `conftest.py`?
2. Kenapa kebanyakan project QA Automation meletakkan `conftest.py` di dalam folder `tests/`, bukan di root project?

---

### ✍️ Jawaban

```text
# Jawaban :

# 1. Fungsi utama conftest.py adalah sebagai tempat menyimpan
# fixture agar dapat digunakan oleh banyak file test
# tanpa perlu di-import.

# 2. Karena fixture hanya digunakan oleh test,
# sehingga lebih rapi jika disimpan di dalam folder tests.
# Selain itu, pytest memang mencari conftest.py mulai dari
# folder tempat file test berada, lalu naik ke parent directory
# hingga root project.
```

---

# 🎯 Checklist

- [x] Paham fungsi `conftest.py`.
- [x] Paham kenapa fixture tidak perlu di-import.
- [x] Paham bagaimana pytest mencari fixture.
- [x] Paham alasan `conftest.py` biasanya diletakkan di folder `tests/`.

---

# 🚀 Goal

Kalau bisa menyelesaikan challenge ini tanpa melihat internet, berarti kamu sudah memahami konsep `conftest.py`.

Setelah ini kamu siap mempelajari:

⭐ **`@pytest.mark.parametrize`**

Karena di sanalah satu test dapat dijalankan menggunakan banyak data tanpa perlu menulis test yang sama berulang kali.
