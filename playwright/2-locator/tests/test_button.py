from playwright.sync_api import Page

def test_button(page: Page):
    page.goto("/buttons")

    # akses button double click me
    page.get_by_role("button", name="Double Click Me")

    # akses button right click me
    page.get_by_role("button", name="Right Click Me")

    # akses button click me
    page.get_by_role("button", name="Click Me", exact=True)