import pytest

@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.regression
def test_checkout():
    pass

@pytest.mark.ui
@pytest.mark.smoke
def test_profile():
    pass

# Pertanyaan
# 1. Test mana yang memiliki marker `smoke`?
# 2. Test mana yang memiliki marker `ui`?
# 3. Berapa marker yang dimiliki `test_profile`?

# Jawaban :
# 1. test_login dan test_profile
# 2. test_profile
# 3. 2, ui dan smoke