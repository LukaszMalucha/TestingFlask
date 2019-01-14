import sys
import subprocess

from tests.acceptance.page_model.new_post_page import NewPostPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage

subprocess.call([sys.executable, 'happ.py', 'htmlfilename.htm'])
from behave import *
from selenium import webdriver


## Allows steps to receive arguments from scenario

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)



@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url