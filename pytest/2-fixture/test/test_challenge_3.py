import pytest

@pytest.fixture
def browser():
    return "Chrome"


# def test_login(browser):
#     print(browser)

# ubah jadi :
def test_login():
    print("Login")

# Pertanyaan :
# 1. Apakah fixture `browser()` tetap dijalankan?
# 2. Kenapa?

# Jawaban :
# 1. fixture 'browser()' tidak akan dijalankan
# 2. karena di paramter tidak dipanggil seperti test_login(browser)