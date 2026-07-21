from playwright.sync_api import Page, expect

def test_text_box(page: Page):
    page.goto("/text-box")

    # akses input full name dan isi
    page.get_by_role("textbox", name="Full Name").fill("Muhammad Dani Haikal")
    
    # akses input email dan isi
    page.get_by_role("textbox", name="name@example.com").fill("dani@gmail.com")

    # akses textbox current address dan isi
    page.get_by_role("textbox", name="Current Address").fill("jakarta")

    # akses textbox permanent address dan isi
    page.locator("#permanentAddress").fill("tangerang")
    
    # akses button submit dan klik
    page.get_by_role("button", name="Submit").click()