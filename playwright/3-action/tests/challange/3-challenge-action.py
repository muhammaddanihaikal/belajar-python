### Kasus A

# <select id="country">
#     <option value="id">Indonesia</option>
#     <option value="jp">Japan</option>
# </select>

# Tulis kode Playwright untuk memilih **Indonesia**.

### Kasus B

# <input role="combobox">

# <div role="option">NCR</div>
# <div role="option">Delhi</div>

# Tulis kode Playwright untuk memilih **NCR**.

from playwright.sync_api import Page

def test_kasus_a(page: Page):
    page.goto("/login")

    # ambil locator
    combobox = page.locator("#country")

    # pilih indonesia
    combobox.select_option("id")
    

def test_kasus_b(page: Page):
    page.goto("/login")

    # ambil locator
    page.locator("#country").select_option("id").click()
    # pilih NCR
    page.get_by_role("option", name="NCR").click()