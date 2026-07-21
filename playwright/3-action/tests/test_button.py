from playwright.sync_api import Page

def test_button(page: Page):
    page.goto("/buttons")

    # akses button double click me
    # klik button double click me
    page.get_by_role("button", name="Double Click Me").dblclick()

    # akses button right click me
    # klik button right click me
    page.get_by_role("button", name="Right Click Me").click(button="right")

    # akses button click me
    page.get_by_role("button", name="Click Me", exact=True).click()