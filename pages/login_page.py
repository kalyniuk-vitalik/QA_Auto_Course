from .base_page import BasePage
from .locators import LoginPagelLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page_again(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        login = "login"
        current_url = self.browser.current_url
        assert login in current_url, "Login link is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPagelLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPagelLocators.REGISTER_FORM), "Register form is absent"

