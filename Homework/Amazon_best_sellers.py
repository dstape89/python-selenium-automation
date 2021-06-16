# Created by dstap at 4/26/2021
from behave import given, then
from selenium.webdriver.common.by import By


@given('Open Amazon Best Sellers page')
def open_amazon_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('There are {expected_links} links at the top of the page')
def verify_best_sellers_links_visible(context, expected_links):
    actual_links = context.driver.find_elements(By.CSS_SELECTOR, '#zg_tabs a')
    assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'
