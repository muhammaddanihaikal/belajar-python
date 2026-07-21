from playwright.sync_api import Page

def test_table(page: Page):
    page.goto("/webtables")

    # ambil locator table
    table = page.get_by_role("table")

    # ambil locator row (tr)
    row_1 = table.get_by_role("row").nth(1)

    # ambil locator cell (td)
    department = row_1.get_by_role("cell").nth(5).text_content()

    # print "uv run pytest -s ./test_table.py"
    print("department: ", department)

