from playwright.sync_api import Page

def test_link(page: Page):
    page.goto("/links")

    page.get_by_role("link", name="Home", exact=True)