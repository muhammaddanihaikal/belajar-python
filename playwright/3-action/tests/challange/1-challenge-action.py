## Challenge 1 — Action Dasar

# Buat script Playwright untuk melakukan aksi berikut:

# - Isi **Username** dengan `"admin"`
# - Isi **Password** dengan `"secret123"`
# - Klik tombol **Login**

# Gunakan Locator dan Action yang sesuai.

from playwright.sync_api import Page

def test_login(page: Page):
    page.goto("/login")

    # ambil locator dan isi
    page.get_by_role("textbox", name="username").fill("admin")
    page.get_by_role("textbox", name="password").fill("secret123")