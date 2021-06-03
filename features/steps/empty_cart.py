from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Clicks on cart icon')
def click_cart(context):
    search_field = context.driver.find_element(By.XPATH, 'cart-size')
    search_field.send_keys(Keys.RETURN)
