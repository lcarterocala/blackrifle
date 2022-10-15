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

# testing in incognito mode on google chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

s = Service('C:\\Users\carte\PycharmProjects\pythonProject4\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 40)
driver.implicitly_wait(20)


# Locators
DROP_DOWN_ALERT = (By.CSS_SELECTOR, 'div#hs-eu-cookie-confirmation')
DECLINE_BTN = (By.ID, 'hs-eu-decline-button')
HEADER_MENU = (By.CSS_SELECTOR, 'li.navigation__main-list-item a')
HOME_LOGO = (By.CSS_SELECTOR, 'a.navigation__logo-wrapper')
HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle div.hamburger__menu-line.line--1')
CLOSE_HAMBURGER_MENU = (By.CSS_SELECTOR, 'div.hamburger__menu.navigation__toggle')
SEARCH_LINK = (By.CSS_SELECTOR, 'span.navigation__main-item.search-box__label')
COFFEE_BAG1 = (By.XPATH, "//span[text()='Just Black']")
COFFEE_BAG2 = (By.XPATH, "//span[text()='Thin Blue Line']")
COFFEE_BAGS = (By.CSS_SELECTOR, 'div.roast__product-image-wrapper')
RIGHT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--right path')
LEFT_ARROW = (By.CSS_SELECTOR, 'button.roast__slider-arrow--left path')
SLIDER = (By.ID, 'roast__scale')


# open black rifle webpage
driver.get('https://www.blackriflecoffee.com/')

# elements and more
drop_down_alert = driver.wait.until(EC.visibility_of_element_located(DROP_DOWN_ALERT))
header_menu = driver.find_elements(*HEADER_MENU)
decline_popup_btn = driver.wait.until(EC.element_to_be_clickable(DECLINE_BTN))
# hamburger_menu = driver.wait.until(EC.element_to_be_clickable(HAMBURGER_MENU))
# close_hamburger_menu = driver.find_element(*CLOSE_HAMBURGER_MENU)
# home_logo = driver.find_element(*HOME_LOGO)
# coffee_bags = driver.find_elements(*COFFEE_BAGS)
search_link = driver.find_element(*SEARCH_LINK)
coffee_bag1 = driver.find_element(*COFFEE_BAG1)
coffee_bag2 = driver.find_element(*COFFEE_BAG2)
right_arrow = driver.wait.until(EC.element_to_be_clickable(RIGHT_ARROW))
left_arrow = driver.wait.until(EC.element_to_be_clickable(LEFT_ARROW))
slider = driver.find_element(*SLIDER)

try:
    # working the page - if dropdown appears first
    if bool(decline_popup_btn):
        decline_popup_btn.click()
except TimeoutException:
    print('Popup failure due to Timeout Exception')
    print(TimeoutException)

# printing the menu link titles
# for items in header_menu:
    # link = items.text
    # print('Menu category: ', link)

# hovering effect over the menu links
print('\n')
actions = ActionChains(driver)

for items in header_menu:
    actions.move_to_element(items)
    actions.perform()


def hover_search():
    actions.move_to_element(search_link)
    actions.perform()
    sleep(3)


def move_slider_right():
    actions.click_and_hold(slider)
    actions.move_by_offset(100, 0)
    actions.perform()
    sleep(2)


def move_slider_left():
    actions.click_and_hold(slider)
    actions.move_by_offset(-100, 0)
    actions.perform()
    sleep(2)


def move_slider():
    move_slider_right()
    move_slider_left()


def hover_bags():
    # driver.execute_script("window.scrollBy(0,500)", "")
    hover1 = actions.move_to_element(coffee_bag1)
    hover2 = actions.move_to_element(coffee_bag2)
    hover1.perform()
    hover2.perform()
    # print('Hover effect successful-proof by url')
    sleep(4)


# I had problems with this because of element overlay...had to use this alternative!
def arrows_click():
    # driver.execute_script("arguments[0].click();", right_arrow)
    driver.execute_script("window.scrollBy(0,500)", "")
    actions.move_to_element(right_arrow).click(right_arrow).perform()
    actions.move_to_element(right_arrow).click(right_arrow).perform()
    actions.move_to_element(left_arrow).click(left_arrow).perform()
    actions.move_to_element(left_arrow).click(left_arrow).perform()
    # right_arrow.click()
    # right_arrow.click()
    # left_arrow.click()
    # left_arrow.click()
    sleep(3)


# method call for hovering over search link
hover_search()
sleep(2)

# scroll down to the coffee bag images - using estimation
# driver.execute_script("window.scrollTo(0,1055)")
# sleep(4)

# method call for clicking on arrows for coffee bags
# arrows_click()


# method call for moving the slider
move_slider()
sleep(2)

# method call for hovering over coffee bag images
hover_bags()

# method call for clicking on arrows for coffee bags
arrows_click()


print('Test Successful.')
driver.quit()
