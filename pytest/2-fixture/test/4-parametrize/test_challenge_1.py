import pytest

@pytest.mark.parametrize(
        "username,password",
        [
            ("dani", "452"),
            ("ekal", "999"),
            ("basir", "159")
        ]
)
def test_login(username, password):
    print(username, password)
    if(username == "dani") :
     assert password == "452"

# Pertanyaan :
# 1. Berapa kali `test_login()` dijalankan?
# 2. Nilai `username` pada setiap test apa saja?
# 3. Jelaskan flow programnya.

# Jawaban :
# 1. 3 kali, karena data dari parametrize ada 3
# 2. admin, user, guest
# 3. Flow Program :
# - Pytest menemukan test_login().
# - Pytest melihat ada decorator @pytest.mark.parametrize.
# - Pytest menentukan bahwa test harus dijalankan 3 kali
#    karena ada 3 data.

# Run 1
# - username = "admin"
# - password = "123"
# - test_login() dijalankan.

# Run 2
# - username = "user"
# - password = "456"
# - test_login() dijalankan.

# Run 3
# - username = "guest"
# - password = "789"
# - test_login() dijalankan.