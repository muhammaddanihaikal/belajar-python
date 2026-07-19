# 09 - Pytest Marker Challenge

## Challenge 1 - Memahami Marker

```python
import pytest

@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.regression
def test_checkout():
    pass

@pytest.mark.ui
@pytest.mark.smoke
def test_profile():
    pass
```

### Pertanyaan

1. Test mana yang memiliki marker `smoke`?
2. Test mana yang memiliki marker `ui`?
3. Berapa marker yang dimiliki `test_profile`?

---

## ✍️ Jawaban

```text

```

---

# Challenge 2 - Menjalankan Marker

```python
import pytest

@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.api
def test_create_user():
    pass

@pytest.mark.smoke
@pytest.mark.ui
def test_dashboard():
    pass

@pytest.mark.slow
def test_export():
    pass
```

### Pertanyaan

Apa saja test yang dijalankan jika menggunakan:

```bash
uv run pytest -m smoke
```

```bash
uv run pytest -m "smoke and ui"
```

```bash
uv run pytest -m "smoke or api"
```

```bash
uv run pytest -m "not slow"
```

Jelaskan alasannya.

---

## ✍️ Jawaban

```text

```

---

# Challenge 3 - Pemahaman Konsep

Jawab menggunakan bahasamu sendiri.

1. Apa fungsi utama marker?
2. Apa perbedaan marker buatan sendiri dan marker bawaan pytest?
3. Kenapa satu test boleh memiliki lebih dari satu marker?
4. Kenapa `@pytest.mark.smoke.ui` tidak bisa digunakan?
5. Apa fungsi operator `and`, `or`, dan `not` pada `-m`?

---

## ✍️ Jawaban

```text

```

---

# Challenge 4 - Register Custom Marker

Perhatikan kode berikut.

```python
import pytest

@pytest.mark.smoke
def test_login():
    pass
```

Saat menjalankan test muncul warning:

```text
PytestUnknownMarkWarning
```

### Pertanyaan

1. Kenapa warning tersebut muncul?
2. Apakah test tetap dijalankan?
3. Bagaimana cara menghilangkan warning tersebut?

---

## ✍️ Jawaban

```text

```

---

# Challenge 5 - Pemahaman Register Marker

Jawab menggunakan bahasamu sendiri.

1. Kenapa marker buatan sendiri sebaiknya diregister?
2. Marker apa saja yang tidak perlu diregister?
3. Apa manfaat register marker bagi sebuah project?

---

## ✍️ Jawaban

```text

```
