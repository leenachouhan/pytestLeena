from playwright.sync_api import Page, expect
import time
# def test_Playwrightbasic(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
    #page.goto("https://rahulshettyacademy.com/loginpagePractise")

def test_FirstCase(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    time.sleep(5)

def test_SecondNegativeCase(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2nvhfkdn")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

    
def test_thirdCase(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    iphoneLocator = page.locator("app-card").filter(has_text="iphone X")
    iphoneLocator.get_by_role("button").click()
    blackberryLocator = page.locator("app-card").filter(has_text="Blackberry")
    blackberryLocator.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    time.sleep(3)

def test_fourthCase(page:Page):
    page.goto("https://example.com")
    print(page.title())

def test_fifthCase(page:Page):
    page.goto("https://example.com")
    expect(page.get_by_text("Example Domain")).to_be_visible()

def test_sixthCase(page:Page):
    page.goto("https://google.com")
    page.locator("#APjFqb").fill("Playwright pytest")
    page.keyboard.press("Enter")

def test_seventhCase(page:Page):
    page.goto("https://example.com")
    page.get_by_text("Learn more").click()
    assert "iana.org" in page.url

def test_eighthCase(page:Page):
    page.goto("https://example.com")
    links = page.locator("a").all_text_contents()
    print(links)

def test_ninthCase(page:Page):
    page.goto("https://www.microsoft.com")
    page.locator("#APjFqb").fill("Playwright automation")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    time.sleep(5)
    title = page.locator(".LC20lb").all_text_contents()
    print(title)

def test_tenthCase(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    #time.sleep(5)
    expect(page.locator("h1",has_text="Shop Name")).to_be_visible() 
    assert "/shop" in page.url

def test_eleventhCase(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("#firstName").fill("leena")
    page.locator("#lastName").fill("chouhan")
    page.locator("#userEmail").fill("abcd@gmail.com")
    page.get_by_label("Female").click()
    page.locator("#userNumber").fill("1234567891")
    page.get_by_role("button", name="Submit").click()
    time.sleep(5)
    assert page.locator(".modal-content",has_text="Thanks for submitting the form")
    print("execution completed")
    
    
        
    


