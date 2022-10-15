from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import Page


class BlackHeader(Page):
    # Locators
    MAIN_MENU = (By.CSS_SELECTOR, 'li.navigation__main-list-item')
    SEARCH_BAR = (By.CSS_SELECTOR, 'a.navigation__search-toggle.search-box.search-box--line')
    CART_BTN = (By.CSS_SELECTOR, 'a.navigation__cart-toggle')
    CART_COUNT_ICON = (By.CSS_SELECTOR, 'span.inline-cart__title-count.js-inline-cart-count')
    CART_EMPTY_MSG = (By.CSS_SELECTOR, 'div.inline-cart__empty')
    HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle div.hamburger__menu-line.line--1')
    HEADER_MENU1 = (By.CSS_SELECTOR, 'li.navigation__main-list-item a')
    HEADER_MENU3 = (By.CSS_SELECTOR, 'div.mobile-navigation__menu-item.menu-item')

    def main_menu_hover(self):
        header_menu = self.driver.find_elements(*self.HEADER_MENU1)
        # hamburger_menu = self.driver.wait.until(EC.element_to_be_clickable(self.HAMBURGER_MENU))
        try:
            # main_menu = self.driver.find_elements(*self.MAIN_MENU)
            main_menu = header_menu
            # main_menu = self.driver.wait.until(EC.presence_of_element_located(self.MAIN_MENU))
            if bool(main_menu):
                actions = ActionChains(self.driver)
                for item in main_menu:
                    actions.move_to_element(item)
                    actions.perform()
        except TimeoutException:
            print('Failure due to Timeout Exception')
            print(TimeoutException)

    def search_bar_click(self):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.click()

    def search_bar_input(self, search_word):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(search_word).submit()

    def cart_button(self):
        try:
            cart_btn = self.driver.find_element(*self.CART_BTN)
            cart_btn.click()
        except ElementClickInterceptedException:
            print('Failure due to Element Click Intercepted Exception')
            print(ElementClickInterceptedException)

    def verify_cart_empty(self):
        cart_count = self.driver.find_element(*self.CART_COUNT_ICON)
        cart_empty_msg = self.driver.find_element(*self.CART_EMPTY_MSG)
        message = 'Your cart is currently empty.'
        if cart_count == 0:
            assert cart_empty_msg == message, f'Error: The cart is not empty.'
            print('Verified: Cart is empty')

