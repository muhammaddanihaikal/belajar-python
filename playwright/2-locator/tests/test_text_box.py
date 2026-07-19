from playwright.sync_api import Page, expect

def test_text_box(page: Page):
    page.goto("/text-box")

    page.get_by_role("textbox", name="Full Name").fill("Muhammad Dani Haikal")
    page.get_by_role("textbox", name="name@example.com").fill("mdanihaikal@gmail.com")
    page.get_by_role("textbox", name="Current Address").fill("jakarta")
    page.locator("#permanentAddress").fill("jakarta barat")

    page.get_by_role("button", name="Submit").click()