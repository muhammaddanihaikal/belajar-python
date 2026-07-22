from playwright.sync_api import Page
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
print("base dir : ",BASE_DIR)
# catatan :
# __file__ = lokasi file Python saat ini
# .parent = cd .. -> (tests/)
# .parent.parent = cd ../.. -> (3-action/)
# .parent.parent.parent = cd ../../.. -> (playwright/)

test_file_pdf = BASE_DIR / "test-file" / "file pdf test.pdf"
print("test file pdf : ", test_file_pdf)


def test_upload_download_file(page: Page):
    page.goto("/upload-download")

    # ambil locator download
    page.get_by_role("button", name="Download")

    # ambil locator upload (ga bisa pake button klik, karena langsug isi pake file test nantinya)
    # single file
    page.locator("#uploadFile").set_input_files(test_file_pdf)

    ## multiple file
    # page.locator("#uploadFile").set_input_files([
    #     "D:/Belajar/Python/belajar-python/playwright/test-file/file pdf test.pdf",
    #     "D:/Belajar/Python/belajar-python/playwright/test-file/file excel test.pdf",
    #     "D:/Belajar/Python/belajar-python/playwright/test-file/file word test.pdf",
    # ])