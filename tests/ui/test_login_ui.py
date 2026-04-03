from pages.login_page import LoginPage

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")

    message = login_page.get_message()
    assert "You logged into a secure area!" in message