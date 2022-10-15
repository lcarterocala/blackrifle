from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Home Page')
def open_homepage(context):
    context.app.black_ri_homepage.open_homepage()


@given('Hover over main menu')
def main_menu_hover(context):
    context.app.black_ri_header.main_menu_hover()


@when('Scroll down to working area')
def scroll_screen(context):
    context.app.black_ri_homepage.scroll_screen()


@when('Cart button is clicked')
def cart_button(context):
    context.app.black_ri_header.cart_button()


@when('Mouse hover on Main Menu items')
def menu_items_hover(context):
    context.app.black_ri_homepage.menu_items_hover()


@then('Print Main Menu links')
def print_menu_links(context):
    context.app.black_ri_homepage.print_menu_links()


@then('Close hamburger menu')
def close_menu(context):
    context.app.black_ri_homepage.close_menu()


@then('Interact with the coffee bag image arrows')
def arrows_click(context):
    context.app.black_ri_homepage.arrows_click()


@then('Hover over coffee bag images')
def hover_bags(context):
    context.app.black_ri_homepage.hover_bags()


@then('Move the slider knob to the left and right')
def move_slider(context):
    context.app.black_ri_homepage.move_slider()

