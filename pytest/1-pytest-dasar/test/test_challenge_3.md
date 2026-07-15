🔴 Challenge 3 - Menjalankan Test

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

## Jawaban :

1. uv run pytest
2. uv run pytest -v
3. uv run pytest ./tests/test_math.py
4. uv run pytest -k penjumlahan
