import sys
import subprocess
subprocess.call([sys.executable, 'happ.py', 'htmlfilename.htm'])
from behave import *
from selenium import webdriver

## Allows steps to receive arguments from scenario

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('C:/chromedriver.exe')
    context.browser.get('http://127.0.0.1:5000')


@then('I am on the blog page')
def step_impl(context):
    # expected_url = 'http://192.168.99.100:5000/blog'
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url