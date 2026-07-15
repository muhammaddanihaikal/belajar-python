import pytest

@pytest.fixture
def angka():
    return 10


def test_tambah(angka):

    hasil = angka + 5

    assert hasil == 15

# Pertanyaan :
# Jelaskan flow program dari awal sampai akhir menggunakan bahasamu sendiri.

# Jawaban :
# 1. Pytest menjalankan function test_tambah().
# 2. Pytest melihat ada parameter bernama 'angka'.
# 3. Pytest mencari fixture dengan nama 'angka'.
# 4. Fixture 'angka()' ditemukan lalu dijalankan.
# 5. Fixture mengembalikan nilai 10.
# 6. Pytest mengisi parameter 'angka' dengan nilai 10.
# 7. Program menjalankan hasil = 10 + 5.
# 8. Program menjalankan assert 15 == 15.
# 9. Karena hasil assert bernilai True, test dinyatakan PASS.