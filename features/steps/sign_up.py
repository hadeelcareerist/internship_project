from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@given ('I am on the registration page')
def open_registration_page(context):
    context.driver.get('https://soft.reelly.io/sign-up')

@when('I fill in valid registration details')
def fill_registration_form(context):
    driver = context.driver
    driver.find_element(By.NAME, 'first_name').send_keys('test+hadeel+careerist')
    driver.find_element(By.NAME, 'last_name').send_keys('altameemi')
    driver.find_element(By.NAME, 'email').send_keys('hadeel.altameemi@gmail.com')
    driver.find_element(By.NAME, 'password').send_keys('Hadoola@2hm')
    Select(driver.find_element(By.NAME, 'country')).select_by_visible_text('US')
