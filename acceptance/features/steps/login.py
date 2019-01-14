import time
import django
from behave import *


@given(
    u'the user with username "{username}" and password "{password}" has been created'
)
def step_impl(context, username, password):
    if not hasattr(context, "created_users"):
        context.created_users = []
    try:
        from django.contrib.auth import get_user_model

        User = get_user_model()
        created_user = User.objects.create_user(username=username, password=password)
        context.created_users.append(created_user)
    except django.db.utils.IntegrityError:
        pass


@when(u"the user navigates to the login page")
def step_impl(context):
    context.browser.visit(context.server_url + "/accounts/login")


@when(u'the user tries to log in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_input_name = "username"
    password_input_name = "password"
    submit_button_css = ".btn--primary"
    context.browser.find_by_name(username_input_name).fill(username)
    context.browser.find_by_name(password_input_name).fill(password)
    context.browser.find_by_css(submit_button_css).click()


@then(u"the user should be redirected to the home page")
def step_impl(context):
    assert context.browser.title == "Home | Rental Service"


@given(u"the user has logged out")
def step_impl(context):
    context.browser.visit(context.server_url + "/accounts/logout")


@then(u"the error message should be displayed in the login page")
def step_impl(context):
    error_css = "ul.errorlist>li"
    error = context.browser.find_by_css(error_css)
    assert error.first.visible == True
