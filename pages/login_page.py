from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.login_button = "button[type='submit']"
        self.message = "#flash"

    def load(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_button)

    def get_message(self):
        return self.page.locator(self.message).inner_text()