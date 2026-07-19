import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("admin", "123"),
        ("user", "456"),
        ("guest", "000")
    ]
)
def test_login(username, password):

    if username == "guest":
        assert password == "789"
    else:
        assert len(password) == 3
    
# Pertanyaan :
# 1. Test mana yang PASS?
# 2. Test mana yang FAIL?
# 3. Kenapa?

# Jawaban :
# 1. Test yang PASS:
# - Run 1 (admin)
# - Run 2 (user)

# 2. Test yang FAIL:
# - Run 3 (guest)

# 3. Kenapa?
# Karena saat username = "guest",
# pytest mengambil data ("guest", "000"),
# sehingga password berisi "000".
#
# Test kemudian memeriksa:
# assert password == "789"
#
# Karena "000" tidak sama dengan "789",
# assertion bernilai False sehingga test FAIL.