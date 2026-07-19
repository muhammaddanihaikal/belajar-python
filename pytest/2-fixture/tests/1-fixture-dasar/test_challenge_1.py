import pytest

@pytest.fixture
def user():

    print("Login")

    yield "Dani"

    print("Logout")


def test_profile(user):

    print(user)

# Pertanyaan :
# Urutkan
# A. Logout
# B. Login
# C. Dani

# Jawaban :
# B - C - A