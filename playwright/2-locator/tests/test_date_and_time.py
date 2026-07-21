from playwright.sync_api import Page, expect

def test_date_and_time(page: Page):
    page.goto("date-picker")

    # ambil locator select date
    expect(page.locator("#datePickerMonthYearInput")).to_be_visible()
    

    # ambil locator date and time
    expect(page.locator("#dateAndTimePickerInput")).to_be_visible()