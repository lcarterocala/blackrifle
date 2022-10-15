import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import messagebox


s = Service('C:\\Users\carte\PycharmProjects\pythonProject4\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

# Locators
SEARCH_INPUT_BAR = (By.CSS_SELECTOR, 'input.gLFyf.gsfi')
SEARCH_BTN = (By.CSS_SELECTOR, 'input.gNO89b[name="btnK"]')
SEARCH_RESULTS = (By.ID, 'result-stats')

# list of names for search
names = ['shoes', 'fiber optics', 'koala']

# message box that automatically appears/disappears
w = Tk()
w.withdraw()
w.after(2750, w.destroy)
messagebox.showinfo('Google Basic Search', 'This is a BASIC SEARCH')


def basic_search(search_word):
    # open google's webpage
    driver.get('https://www.google.com')
    original_window = driver.current_window_handle

    # enters the search word into the input field
    search_bar = driver.wait.until(EC.element_to_be_clickable(SEARCH_INPUT_BAR))
    search_bar.clear()
    search_bar.send_keys(search_word)

    # locate and click the search button
    search_btn = driver.find_element(*SEARCH_BTN)
    search_btn.click()
    sleep(3)

    # verification that we're on the search results page
    search_results = driver.find_element(*SEARCH_RESULTS).text
    if bool(search_results):
        # print('\n')
        print('Verified: The search results page has been reached.')
        print('Results: ', search_results)
        print('\n')


def list_search(mylist):
    search_num = 0
    # message box that automatically appears/disappears
    w = Tk()
    w.withdraw()
    w.after(2750, w.destroy)
    messagebox.showinfo('Google List Search', 'This is a LIST SEARCH')
    for name in mylist:
        search_num = search_num + 1
        print('Search #', search_num)
        basic_search(name)


# method calls
basic_search('artemis')
list_search(names)

print('Test Successful!')
driver.quit()
