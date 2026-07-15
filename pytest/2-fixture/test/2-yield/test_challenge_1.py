import pytest

@pytest.fixture
def nama():
    return "Dani"


def test_user(nama):
    assert nama == "Dani"

# Pertanyaan :
# 1. Siapa yang memanggil `nama()`?
# 2. Kapan fixture dijalankan?
# 3. Nilai pada parameter `nama` berasal dari mana?

# Jawaban :
# 1. Yang memanggil fixture nama() adalah pytest.
# Saat pytest melihat parameter 'nama' pada function test_user(),
# pytest akan mencari fixture dengan nama yang sama.
# Jika fixture ditemukan, pytest akan menjalankannya.
# Jika tidak ditemukan, pytest akan menampilkan error.

# 2. Fixture dijalankan ketika ada test yang membutuhkan fixture tersebut,
# yaitu saat parameter pada function test memiliki nama yang sama
# dengan fixture.

# 3. Pytest menjalankan fixture nama(),
# lalu mengambil nilai yang dihasilkan fixture tersebut
# dan mengisikannya ke parameter nama di test_user().