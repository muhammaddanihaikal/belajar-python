from playwright.sync_api import Page

def test_modal(page: Page):
    page.goto("modal-dialogs")

    # klik button small modal
    page.get_by_role("button", name="Small modal").click()
    # ambil locator dialog small modal
    small_modal = page.get_by_role("dialog", name="Small Modal")
    # tutup small modal pakai button Close dibawah (bukan 'X')
    small_modal.locator(".modal-footer").get_by_role("button", name="Close").click

    # klik button large modal
    page.get_by_role("button", name="Large modal").click()
    # ambil locator dialog large modal
    page.get_by_role("dialog", name="Large Modal")