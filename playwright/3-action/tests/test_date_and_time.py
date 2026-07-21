from playwright.sync_api import Page, expect

def test_date_and_time(page: Page):
    page.goto("date-picker")

    # ambil locator select date dan isi
    select_date = page.locator("#datePickerMonthYearInput")
    select_date.fill("01/14/2001")
    select_date.press("Tab")
    

    # ambil locator date and time
    date_and_time = page.locator("#dateAndTimePickerInput")
    date_and_time.fill("July 22, 2000 4:11 PM")
    date_and_time.press("Tab")