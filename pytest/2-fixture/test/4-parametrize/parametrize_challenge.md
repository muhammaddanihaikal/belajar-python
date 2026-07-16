# 🧠 Pytest Parametrize Challenge

---

# 🟢 Challenge 1 - Flow Parametrize

Perhatikan kode berikut.

```python
import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("admin", "123"),
        ("user", "456"),
        ("guest", "789")
    ]
)
def test_login(username, password):
    print(username)
```

## Pertanyaan

1. Berapa kali `test_login()` dijalankan?
2. Nilai `username` pada setiap test apa saja?
3. Jelaskan flow programnya.

---

### ✍️ Jawaban

```text
1. 3 kali, karena data dari parametrize ada 3
2. admin, user, guest
3. Flow Program :

# 1. Pytest menemukan test_login().
# 2. Pytest melihat ada decorator @pytest.mark.parametrize.
# 3. Pytest menentukan bahwa test harus dijalankan 3 kali
#    karena ada 3 data.
#
# Run 1
# 4. username = "admin"
# 5. password = "123"
# 6. test_login() dijalankan.
#
# Run 2
# 7. username = "user"
# 8. password = "456"
# 9. test_login() dijalankan.
#
# Run 3
# 10. username = "guest"
# 11. password = "789"
# 12. test_login() dijalankan.
```

---

# 🟡 Challenge 2 - PASS atau FAIL

Perhatikan kode berikut.

```python
import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("admin", "123"),
        ("user", "456"),
        ("guest", "000")
    ]
)
def test_login(username, password):

    if username == "guest":
        assert password == "789"
    else:
        assert len(password) == 3
```

## Pertanyaan

1. Test mana yang PASS?
2. Test mana yang FAIL?
3. Kenapa?

---

### ✍️ Jawaban

```text
# Jawaban :

# 1. Test yang PASS:
# - Run 1 (admin)
# - Run 2 (user)

# 2. Test yang FAIL:
# - Run 3 (guest)

# 3. Kenapa?
# Karena saat username = "guest",
# pytest mengambil data ("guest", "000"),
# sehingga password berisi "000".
#
# Test kemudian memeriksa:
# assert password == "789"
#
# Karena "000" tidak sama dengan "789",
# assertion bernilai False sehingga test FAIL.
```

---

# 🔴 Challenge 3 - Pemahaman Konsep

Jawab menggunakan bahasamu sendiri.

1. Apa fungsi utama `@pytest.mark.parametrize`?
2. Kenapa `parametrize` ditulis di atas function test, bukan di `conftest.py`?
3. Kalau ada banyak test yang menggunakan data login yang sama, apa yang sebaiknya dibuat reusable?

---

### ✍️ Jawaban

```text
# Jawaban :

# 1. Fungsi utama parametrize adalah menjalankan satu test yang sama menggunakan banyak data.

# 2. Karena parametrize hanya berlaku untuk function test yang berada di bawahnya.
# Berbeda dengan fixture yang dapat digunakan oleh banyak test,
# parametrize hanya digunakan untuk mengatur cara satu test dijalankan.

# 3. Yang dibuat reusable adalah datanya, misalnya disimpan di (variable, JSON, CSV, dll)
# Kemudian data tersebut dipanggil kembali pada @pytest.mark.parametrize.
```

---

# 🎯 Checklist

- [ ] Paham fungsi `@pytest.mark.parametrize`.
- [ ] Paham flow eksekusi `parametrize`.
- [ ] Paham kenapa `parametrize` ditulis di atas function test.
- [ ] Paham bahwa setiap tuple mewakili satu skenario test.
- [ ] Paham bahwa yang biasanya dibuat reusable adalah data, bukan `parametrize`-nya.

---

# 🚀 Goal

Kalau bisa menyelesaikan challenge ini tanpa melihat internet, berarti kamu sudah memahami konsep `@pytest.mark.parametrize`.

Setelah ini kamu siap mempelajari:

⭐ **Pytest Marker (`@pytest.mark`)**

Karena marker digunakan untuk mengelompokkan, memilih, atau mengatur test yang ingin dijalankan.
