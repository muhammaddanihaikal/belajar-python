from playwright.sync_api import Page

def test_upload_download_file(page: Page):
    page.goto("/upload-download")

    # ambil locator download
    page.get_by_role("button", name="Download")

    # ambil locator upload (ga bisa pake button klik, karena langsug isi pake file test nantinya)
    page.locator("#uploadFile")