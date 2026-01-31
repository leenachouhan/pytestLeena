import time
from playwright.sync_api import Page

def test_FirstCase(page:Page):
    page.goto("https://google.com")
    #.sleep(5)
    page.locator("#APjFqb").fill("IPL points table 2021")
    #time.sleep(5)
    resultCount = page.get
    print (resultCount)
    time.sleep(2)
