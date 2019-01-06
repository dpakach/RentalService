import django
import sys
import os

from behave import use_fixture, fixture
from splinter import Browser

sys.path.append(os.path.abspath("/home/deepak/Documents/code/colez_projects/RentalService/"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rental.settings'

@fixture
def browser(context):
    context.browser = Browser('chrome')
    yield context.browser
    context.browser.quit()

def before_all(context):
    django.setup()
    use_fixture(browser, context)

def after_scenario(context, scenario):
    if hasattr(context, 'created_users'):
        for user in context.created_users:
            user.delete()
