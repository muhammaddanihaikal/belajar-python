from playwright.sync_api import Page

def test_radio_button(page: Page):
    page.goto("/radio-button")

    # akses radio button yes
    page.get_by_role("radio", name="Yes")

    # akses radio button impressive
    page.get_by_role("radio", name="Impressive")
