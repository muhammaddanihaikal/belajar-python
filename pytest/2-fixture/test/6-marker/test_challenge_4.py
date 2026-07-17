import pytest

@pytest.mark.smoke
def test_login():
    pass

# muncul warning 'PytestUnknownMarkWarning'

# Pertanyaan :
# 1. Kenapa warning tersebut muncul?
# 2. Apakah test tetap dijalankan?
# 3. Bagaimana cara menghilangkan warning tersebut?

# Jawaban :
# 1. Karena marker buatan sendiri belum diregister di pyproject.toml atau pytest.ini.
# 2. Ya, test tetap dijalankan tetapi muncul warning.
# 3. Register marker di pyproject.toml atau pytest.ini.