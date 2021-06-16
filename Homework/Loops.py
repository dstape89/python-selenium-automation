from selenium.webdriver.common.by import By
from behave import given, then


@given('Open Amazon {product_id} page')
def product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/Under-Armour-Freedom-T-Shirt-Graphite/dp/{product_id}/')


@then('Verify user can click through colors')
def verify_can_loop_thru_colors(context):
    expected_colors = ['White', 'Black']
    color_webelements = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(color_webelements)):
        # i = 0
        color_webelements[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'
