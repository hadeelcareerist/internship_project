from behave import given, when, then
#from selenium import webdriver
from pages.login_page import LoginPage
from pages.secondary_page import SecondaryPage
from pages.Application import Application


@given('Open the Reelly main page')
def step_open_main_page(context):
    #context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://soft.reelly.io')
    context.app = Application(context.driver)

@given('Log in to the page')
def step_login(context):
    context.app.login_page.log_in_to_the_page('hadeel.altameemi@gmail.com', 'Hadoola@2hm' )

@when('Click on the "Secondary" option at the left side menu')
def step_click_secondary(context):
  context.app.secondary_page.click_secondary_option()

@then('Verify the right page opens')
def step_verify_page(context):
    context.app.secondary_page.verify_secondary_page_opens()

@when('Click on Filters')
def step_click_filters(context):
    context.app.secondary_page.click_filter()

@when('Filter the products by “want to buy”')
def step_filter_products(context):
   context.app.secondary_page.filter_products_by_want_to_buy()

@when ('Click on Apply Filter')
def step_apply_filter(context):
    context.app.secondary_page.click_on_apply_filter()

@then ('Verify all cards have a “Want to buy” tag')
def step_verify_all_cards(context):
    context.app.secondary_page.verify_all_cards_have_want_to_buy_tag()











