from playwright.sync_api import Page, expect

def test_text_box(page: Page):
    page.goto("/text-box")

    # akses input full name
    page.get_by_role("textbox", name="Full Name")
    
    # akses input email
    page.get_by_role("textbox", name="name@example.com")

    # akses textbox current address
    page.get_by_role("textbox", name="Current Address")

    # akses textbox permanent address
    page.locator("#permanentAddress")
    
    # akses button submit
    page.get_by_role("button", name="Submit")