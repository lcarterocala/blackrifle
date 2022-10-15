from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


# s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
s = Service('C:\\Users\carte\PycharmProjects\pythonProject4\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Locators
BELL_LINK = (By.CSS_SELECTOR, 'div#notification-container._yb_1vgbs._yb_lhjud')
HEADER_LINKS = (By.CSS_SELECTOR, 'div.ybar-mod-navigation li')
PAGE_BTNS = (By.CSS_SELECTOR, '#stream-category-form label')


# open yahoo webpage
driver.get('https://www.yahoo.com/')

bell_lnk = driver.find_element(*BELL_LINK)
header_lnk = driver.find_elements(*HEADER_LINKS)
page_btns = driver.find_elements(*PAGE_BTNS)
count_btns = len(page_btns)
count_lnks = len(header_lnk)

for options in header_lnk:
    j = options.text
    print(j)
print('Number of links: ', count_lnks)
print("Number of buttons: ", count_btns)

# bell link hover
actions = ActionChains(driver)
actions.move_to_element(bell_lnk)
actions.perform()
sleep(5)

print('Test Successful')
driver.quit()

