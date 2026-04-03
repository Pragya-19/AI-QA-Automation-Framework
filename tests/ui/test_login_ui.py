from pages.login_page import LoginPage
from utils.config import VALID_USERNAME, VALID_PASSWORD

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    message = login_page.get_message()
    assert "You logged into a secure area!" in message