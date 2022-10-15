from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException

from pages.base_page import Page


class BlackHomepage(Page):
    # Locators
    DROP_DOWN_ALERT = (By.CSS_SELECTOR, 'div#hs-eu-cookie-confirmation')
    DECLINE_BTN = (By.ID, 'hs-eu-decline-button')
    HEADER_MENU = (By.CSS_SELECTOR, 'div.mobile-navigation__menu-item')
    HEADER_MENU1 = (By.CSS_SELECTOR, 'li.navigation__main-list-item a')
    HEADER_MENU2 = (By.CSS_SELECTOR, 'div.mobile-navigation__menu')
    HEADER_MENU3 = (By.CSS_SELECTOR, 'div.mobile-navigation__menu-item.menu-item')
    HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle div.hamburger__menu-line.line--1')
    # CLOSE_HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.navigation__toggle-wrapper')
    CLOSE_HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle')
    HOME_LOGO = (By.CSS_SELECTOR, 'a.navigation__logo-wrapper')
    COFFEE_BAG1 = (By.XPATH, "//span[text()='Just Black']")
    COFFEE_BAG2 = (By.XPATH, "//span[text()='Thin Blue Line']")
    COFFEE_BAGS = (By.CSS_SELECTOR, 'div.roast__product-image-wrapper')
    RIGHT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--right rect')
    LEFT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--left rect')
    SLIDER = (By.ID, 'roast__scale')

    def open_homepage(self):
        self.open_page('https://www.blackriflecoffee.com/')
        sleep(5)
        try:
            # elements
            drop_down_alert = self.driver.wait.until(EC.presence_of_element_located(self.DROP_DOWN_ALERT))
            decline_popup_btn = self.driver.wait.until(EC.element_to_be_clickable(self.DECLINE_BTN))
            # hamburger_menu = self.driver.wait.until(EC.element_to_be_clickable(self.HAMBURGER_MENU))
            if bool(drop_down_alert):
                # self.driver.switch_to.frame(drop_down_alert)
                decline_popup_btn.click()

            # if bool(hamburger_menu):
                # hamburger_menu.click()
                # sleep(3)
        except TimeoutException:
            print('Failure due to Timeout Exception')
            print(TimeoutException)

    def menu_items_hover(self):
        try:
            # elements
            header_menu = self.driver.find_elements(*self.HEADER_MENU1)
            # hovering effect over the temp menu links
            actions = ActionChains(self.driver)
            for items in header_menu:
                # link = items.text
                # print(link)
                actions.move_to_element(items)
                actions.perform()
        except ElementNotInteractableException:
            print('Failure due to Element Not Interactable Exception')
            print(ElementNotInteractableException)

    def print_menu_links(self):
        header_menu = self.driver.find_elements(*self.HEADER_MENU1)
        for items in header_menu:
            link = items.text
            print('Menu category: ', link)

    def close_menu(self):
        try:
            # elements
            close_hamburger_menu = self.driver.find_element(*self.CLOSE_HAMBURGER_MENU)
            # close the menu after hover effect
            close_hamburger_menu.click()
            print('Hamburger menu closed.')
        except ElementNotInteractableException:
            print('Failure due to Element Not Interactable Exception')
            print(ElementNotInteractableException)

    def scroll_screen(self):
        # scroll the screen down to the coffee bag images - using estimation
        self.driver.execute_script("window.scrollBy(0,500)", "")
        sleep(2)

    def arrows_click(self):
        actions = ActionChains(self.driver)
        right_arrow = self.driver.find_element(*self.RIGHT_ARROW)
        left_arrow = self.driver.find_element(*self.LEFT_ARROW)
        # self.driver.execute_script("window.scrollBy(0,500)", "")
        actions.move_to_element(right_arrow).click(right_arrow).perform()
        actions.move_to_element(right_arrow).click(right_arrow).perform()
        actions.move_to_element(left_arrow).click(left_arrow).perform()
        actions.move_to_element(left_arrow).click(left_arrow).perform()
        # right_arrow.click()
        # left_arrow.click()
        sleep(4)

    def hover_bags(self):
        # driver.execute_script("window.scrollBy(0,500)", "")
        actions = ActionChains(self.driver)
        coffee_bag1 = self.driver.find_element(*self.COFFEE_BAG1)
        coffee_bag2 = self.driver.find_element(*self.COFFEE_BAG2)
        hover1 = actions.move_to_element(coffee_bag1)
        hover2 = actions.move_to_element(coffee_bag2)
        hover1.perform()
        hover2.perform()
        # print('Hover effect successful-proof by url')
        sleep(4)

    def move_slider_right(self):
        actions = ActionChains(self.driver)
        slider = self.driver.find_element(*self.SLIDER)
        actions.click_and_hold(slider)
        actions.move_by_offset(100, 0)
        actions.perform()
        sleep(2)

    def move_slider_left(self):
        actions = ActionChains(self.driver)
        slider = self.driver.find_element(*self.SLIDER)
        actions.click_and_hold(slider)
        actions.move_by_offset(-100, 0)
        actions.perform()
        sleep(2)

    def move_slider(self):
        self.move_slider_right()
        self.move_slider_left()
        print('Slider Log: Slider was successfully moved left & right')
