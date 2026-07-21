from playwright.sync_api import Page


# CUSTOM DROPDOWN — tidak menggunakan <select>
def test_combobox_tanpa_select(page: Page):
    page.goto("/automation-practice-form")

    # Ambil locator combobox State dan klik
    page.locator("#state").get_by_role("combobox").click()
    # Pilih NCR
    page.get_by_role("option", name="NCR").click()

    # ambil locator combobox city dan klik
    page.locator("#city").get_by_role("combobox").click()
    page.get_by_role("option", name="Noida").click()


## NATIVE DROPDOWN — menggunakan <select>
# def test_combobox_dengan_select(page: Page):
#     page.goto("/halaman-yang-ada-select")

#     # Ambil locator <select>
#     country = page.locator("#country")

#     # Pilih option berdasarkan label
#     country.select_option(label="Indonesia")