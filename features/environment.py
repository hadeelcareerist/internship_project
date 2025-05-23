from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service




def browser_init(context):
    """
    :param context: Behave context
    """


    options = Options()
    options.headless = True


    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service, options=options)

    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
