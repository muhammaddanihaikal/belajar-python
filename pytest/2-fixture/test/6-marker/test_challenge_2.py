import pytest

@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.api
def test_create_user():
    pass

@pytest.mark.smoke
@pytest.mark.ui
def test_dashboard():
    pass

@pytest.mark.slow
def test_export():
    pass

# Pertanyaan :
# Apa saja test yang dijalankan jika menggunakan:
# 1. uv run pytest -m smoke
# 2. uv run pytest -m "smoke and ui"
# 3. uv run pytest -m "smoke or api"
# 4. uv run pytest -m "not slow"
# Jelaskan alasannya.

# Jawaban :
# 1. test_login dan test_dashboard
# Karena keduanya memiliki marker smoke.

# 2. test_dashboard
# Karena hanya test_dashboard yang memiliki marker smoke dan ui.

# 3. test_login, test_dashboard, dan test_create_user
# Karena ketiganya memiliki marker smoke atau api.

# 4. test_login, test_create_user, dan test_dashboard
# Karena ketiganya tidak memiliki marker slow.