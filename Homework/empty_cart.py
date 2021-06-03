from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Clicks on cart icon')
def click_cart(context):
    search_field = context.driver.find_element_by_xpath("//a[@id='nav-cart']")
    search_field.send_keys(Keys.RETURN)


@then('Shopping cart is empty')
def empty_cart(context):
    actual_text = context.driver.find_element_by_xpath("//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
