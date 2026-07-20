from playwright.sync_api import Page

def test_button(page: Page):
    page.goto("/buttons")

    # double klik
    page.get_by_role("button", name="Double Click Me").dblclick()

    # klik kanan
    page.get_by_role("button", name="Right Click Me").click(button="right")

    # klik button yang namanya persis "Click Me"
    page.get_by_role("button", name="Click Me", exact=True).click()