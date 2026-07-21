from playwright.sync_api import Page


def test_check_box(page: Page):
    page.goto("/checkbox")
    # akses checkbox home
    # ceklis checkbox
    page.get_by_role("checkbox", name="Select Home").check()
    # uncheck checkbox
    page.get_by_role("checkbox", name="Select Home").uncheck()

