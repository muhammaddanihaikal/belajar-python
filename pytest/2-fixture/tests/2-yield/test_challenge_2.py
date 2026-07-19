import pytest

@pytest.fixture
def browser():

    print("Open Browser")

    return "Chrome"

    print("Close Browser")


def test_login(browser):

    print(browser)

# Pertanyaan :
# 1. Apa output dari program tersebut?
# 2. Apakah `"Close Browser"` dijalankan?
# 3. Kenapa?

# Jawaban :
# 1. Open Browser
#    Chrome
# 2. Tidak
# 3. Karena ada return, jadi proses berhenti smapai Chrome aja