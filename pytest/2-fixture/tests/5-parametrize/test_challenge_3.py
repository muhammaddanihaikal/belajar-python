# Pertanyaan :
#1. Apa fungsi utama `@pytest.mark.parametrize`?
#2. Kenapa `parametrize` ditulis di atas function test, bukan di `conftest.py`?
#3. Kalau ada banyak test yang menggunakan data login yang sama, apa yang sebaiknya dibuat reusable?

# Jawaban :
# 1. Fungsi utama parametrize adalah menjalankan satu test yang sama menggunakan banyak data.

# 2. Karena parametrize hanya berlaku untuk function test yang berada di bawahnya.
# Berbeda dengan fixture yang dapat digunakan oleh banyak test,
# parametrize hanya digunakan untuk mengatur cara satu test dijalankan.

# 3. Yang dibuat reusable adalah datanya, misalnya disimpan di (variable, JSON, CSV, dll)
# Kemudian data tersebut dipanggil kembali pada @pytest.mark.parametrize.