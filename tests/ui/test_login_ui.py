from playwright.sync_api import Page

def test_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    success_message = page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in success_message