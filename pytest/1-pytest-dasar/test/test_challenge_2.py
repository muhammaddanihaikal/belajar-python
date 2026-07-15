def test_username():
    username = "admin"

    assert username == "admin"


def test_password():
    password = "123456"

    assert password == "password"

# Pertanyaan :
# 1. Test mana yang PASS?
# 2. Test mana yang FAIL?
# 3. Kenapa bisa FAIL?
# 4. Kira-kira pesan error apa yang ditampilkan pytest?

# Jawaban :
# 1. test yang PASS = test_username
# 2. test yang FAIL = test_password
# 3. knp bisa FAIL? karena jelas valuenya ga sama antara "123456" dan "password"
# 4. pesan errornya kira kira AssertionError assert "123456" == "password"