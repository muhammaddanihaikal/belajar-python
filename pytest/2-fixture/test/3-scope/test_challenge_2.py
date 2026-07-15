import pytest

@pytest.fixture(scope="session")
def data():
    print("Setup")
    yield
    print("Cleanup")


def test_1(data):
    print("Test 1")


def test_2(data):
    print("Test 2")

# Pertanyaan :
# 1. Berapa kali `Setup` dijalankan?
# 2. Berapa kali `Cleanup` dijalankan?
# 3. Bagaimana flow programnya sekarang?

# Jawaban :
# 1. 1 kali
# 2. 1 kali
# 3. fungsi test_1 dan test_2 dijalankan manggil fixture data, karena scopenya sesion/fixture jalan untuk satu kali test aja

# Flow Program :

# 1. Pytest menjalankan fixture data() sekali (Setup).
# 2. Pytest menjalankan test_1().
# 3. Pytest menjalankan test_2().
# 4. Setelah semua test selesai,
#    fixture melanjutkan proses setelah yield (Cleanup).