from playwright.sync_api import Page

def test_radio_button(page: Page):
    page.goto("/radio-button")

    # pilih radio button 'Yes'
    page.get_by_role("radio", name="Yes").check()

    # pilih radio button 'Impressive'
    page.get_by_role("radio", name="Impressive").check()

    page.get_by_role("radio", name="Yes").check()
    page.get_by_role("radio", name="Impressive").check()
