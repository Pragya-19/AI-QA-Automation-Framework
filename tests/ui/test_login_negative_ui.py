from pages.login_page import LoginPage
from utils.config import INVALID_USERNAME, INVALID_PASSWORD

def test_login_failure(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    message = login_page.get_message()
    assert "Your username is invalid!" in message