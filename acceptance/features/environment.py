import django
import sys
import os

from behave import use_fixture, fixture
from splinter import Browser

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../..")
os.environ['DJANGO_SETTINGS_MODULE'] = 'rental.settings'

@fixture
def browser(context):
    selenium_url=os.environ.get('SELENIUM_URL', 'http://172.17.0.1:4444/wd/hub')
    kwargs = {'driver_name': 'chrome'}
    if 'DRIVER_NAME' in os.environ:
        kwargs.update({
            'driver_name': os.environ['DRIVER_NAME'],
            'url': selenium_url
        });
        if os.environ.get('DRIVER_NAME').lower() == "remote":
            kwargs.update({
                'browser': 'chrome'
            });
    if os.environ.get('TRAVIS'):
        kwargs.update({
            "tunnel-identifier": os.environ["TRAVIS_JOB_NUMBER"]
        })
    context.browser = Browser(**kwargs)
    context.server_url = os.environ.get('SERVER_URL', 'http://localhost:8000')
    yield context.browser
    context.browser.quit()

def before_all(context):
    django.setup()
    use_fixture(browser, context)

def after_scenario(context, scenario):
    if hasattr(context, 'created_users'):
        for user in context.created_users:
            user.delete()
