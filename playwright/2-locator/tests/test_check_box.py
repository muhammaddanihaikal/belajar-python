from playwright.sync_api import Page


def test_check_box(page: Page):
    page.goto("/checkbox")
    # klik untuk ceklis
    page.get_by_role("checkbox", name="Select Home").click()
    # klik untuk unchecklis
    page.get_by_role("checkbox", name="Select Home").click()

    # klik untuk ceklis
    page.get_by_role("checkbox", name="Select Home").click()
    # klik untuk uncheck
    page.get_by_role("checkbox", name="Select Home").click()
