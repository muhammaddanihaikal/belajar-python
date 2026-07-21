from playwright.sync_api import Page

def test_link(page: Page):
    page.goto("/links")

    # ambil locator link 'a' trus klik
    page.get_by_role("link", name="Home", exact=True).click()