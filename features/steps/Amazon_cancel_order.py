from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

driver = webdriver.Chrome()

@given('Open Amazon order page')
def open_amazon_order(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    driver.implicitly_wait(4)

@when('Enter search text')
def enter_search_text(context):
    search_field = context.driver.find_element(By.XPATH, "//input[@type='search']")
    search_field.send_keys('Cancel order')
    search_field.send_keys(Keys.RETURN)

@then('Confirm text')
def confirm_text(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@CLASS='help-content']/h1").text
    expected_text = 'Cancel Items or Orders'
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
    driver.quit()
