from selenium.webdriver.common.by import By
from behave import when, then


@when('Click on the first product')
def select_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.a-section > img[src*='61HPrUHCQEL._AC_UL320_.jpg']").click()


@when('Click on add to cart button')
def add_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then('verify cart has {expected_value} in it')
def verify_cart(context, expected_value):
    context.driver.find_element(By.ID, "hlb-view-cart-announce").click()
    actual_value = context.driver.find_element(By.CSS_SELECTOR, "span.sc-product-title").text
    assert expected_value == actual_value
