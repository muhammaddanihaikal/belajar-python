import pytest

@pytest.fixture(scope="function")
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
# 3. Jelaskan flow programnya.

# Jawaban :
# 1. 2 kali
# 2. 2 kali
# 3. fungsi test_1 dijalankan manggil fixture data, tiap dipanggil fixture jalan karena scope funciton
#    fungsi test_2 dijalankan manggil fixture data, tiap dipanggil fixture jalan karena scope function

# Flow Program :
# 1. Pytest menjalankan test_1().
# 2. Karena test_1 membutuhkan fixture data,
#    fixture dijalankan (Setup).
# 3. Test_1 selesai dijalankan.
# 4. Fixture melanjutkan proses setelah yield (Cleanup).
#
# 5. Pytest menjalankan test_2().
# 6. Fixture data dijalankan kembali (Setup).
# 7. Test_2 selesai dijalankan.
# 8. Fixture melanjutkan proses setelah yield (Cleanup).