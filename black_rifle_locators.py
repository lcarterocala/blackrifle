from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import Page

s = Service('C:\\Users\carte\PycharmProjects\pythonProject4\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.wait = WebDriverWait(driver, 20)
driver.implicitly_wait(10)

# Locators
DROP_DOWN_ALERT = (By.CSS_SELECTOR, 'div#hs-eu-cookie-confirmation')
DECLINE_BTN = (By.ID, 'hs-eu-decline-button')
# HEADER_MENU = (By.CLASS_NAME, 'navigation__main-list')
HEADER_MENU3 = (By.CSS_SELECTOR, 'div.mobile-navigation__menu-item.menu-item')
HEADER_MENU2 = (By.CSS_SELECTOR, 'div.mobile-navigation__menu')
HEADER_MENU = (By.CSS_SELECTOR, 'div.mobile-navigation__menu-item')
HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle div.hamburger__menu-line.line--1')
MAIN_MENU = (By.CSS_SELECTOR, 'ul.navigation__main-list li')
CLOSE_HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle')
HOME_LOGO = (By.CSS_SELECTOR, 'a.navigation__logo-wrapper')
COFFEE_BAG1 = (By.XPATH, "//span[text()='Just Black']")
COFFEE_BAG2 = (By.XPATH, "//span[text()='Thin Blue Line']")
COFFEE_BAGS = (By.CSS_SELECTOR, 'div.roast__product-image-wrapper')
RIGHT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--right rect')
LEFT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--left rect')
SLIDER = (By.ID, 'roast__scale')

# open black rifle webpage
driver.get('https://www.blackriflecoffee.com/')

# elements and more
drop_down_alert = driver.wait.until(EC.visibility_of_element_located(DROP_DOWN_ALERT))
header_menu = driver.find_elements(*HEADER_MENU3)
decline_popup_btn = driver.wait.until(EC.element_to_be_clickable(DECLINE_BTN))
hamburger_menu = driver.wait.until(EC.element_to_be_clickable(HAMBURGER_MENU))
close_hamburger_menu = driver.find_element(*CLOSE_HAMBURGER_MENU)
home_logo = driver.find_element(*HOME_LOGO)
# coffee_bags = driver.find_elements(*COFFEE_BAGS)
coffee_bag1 = driver.find_element(*COFFEE_BAG1)
coffee_bag2 = driver.find_element(*COFFEE_BAG2)
right_arrow = driver.find_element(*RIGHT_ARROW)
left_arrow = driver.find_element(*LEFT_ARROW)


# switch to popup frame
# if bool(drop_down_alert):
    # driver.switch_to.frame(drop_down_alert)
    # decline_popup_btn.click()

# working the page
# popup handler
if bool(decline_popup_btn):
    decline_popup_btn.click()

# popup handler for mobile
if bool(hamburger_menu):
    hamburger_menu.click()
    sleep(3)

# printing the menu link titles
for items in header_menu:
    link = items.text
    print('Menu category: ', link)

# hovering effect over the menu links
print('\n')
actions = ActionChains(driver)
for items in header_menu:
    actions.move_to_element(items)
    actions.perform()


# close the menu after hover effect
close_hamburger_menu.click()
print('Hamburger menu closed.')


# header interactions
# def main_menu_hover():
    # try:
        # main_menu = driver.wait.until(EC.element_to_be_clickable(MAIN_MENU))
        # if bool(main_menu):
            # for item in main_menu:
                # actions.move_to_element(item)
                # actions.perform()
    # except TimeoutException:
        # print('Failure due to Timeout Exception')
        # print(TimeoutException)
        # hamburger_menu.click()
        # sleep(5)


# scroll down to the coffee bag images - using estimation
# driver.execute_script("window.scrollTo(0,1179)")
# sleep(5)


# method to click on page arrow icon
def arrows_click():
    right_arrow.click()
    right_arrow.click()
    left_arrow.click()
    left_arrow.click()
    sleep(5)


# method call for arrows click
arrows_click()

# hover over two of the coffee bags - only visible by url
# actions = ActionChains(driver)
# hover1 = actions.move_to_element(coffee_bag1)
# hover2 = actions.move_to_element(coffee_bag2)
# hover1.perform()
# hover2.perform()
# print('Hover effect successful-proof by url')
# sleep(7)

# slider = driver.find_element(*SLIDER)


# move the slider
# def move_slider_right():
    # actions.click_and_hold(slider)
    # actions.move_by_offset(100, 0)
    # actions.perform()
    # sleep(4)


# def move_slider_left():
    # actions.click_and_hold(slider)
    # actions.move_by_offset(-100, 0)
    # actions.perform()
    # sleep(4)


# method call for move slider
# main_menu_hover()
# move_slider_right()
# move_slider_left()

print('Test Successful.')
driver.quit()


