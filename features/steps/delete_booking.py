from functools import reduce
from behave import *
import operator
from django.db.models import Q
from ZooWeb.models import GroupOfVisitor, Sector
from django.contrib.auth.models import User


use_step_matcher("parse")


@when(u'I try to delete a booking with date "{date}" and hour "{hour}"')
def step_impl(context, date, hour):
    visit = GroupOfVisitor.objects.get(date=date, hour=hour)
    context.browser.visit(context.get_url('visitors_delete', visit.pk))
    


@when(u'I delete the booking with date "{date}" and hour "{hour}"')
def step_impl(context, date, hour):
    visit = GroupOfVisitor.objects.get(date=date, hour=hour)
    context.browser.visit(context.get_url('visitors_detail', visit.pk))

    context.browser.find_by_value('Delete').first.click()

    form = context.browser.find_by_tag('form').first
    form.find_by_value('Confirm').first.click()


@then(u'I\'m viewing the home page for "{username}"')
def step_impl(context, username):
    assert context.browser.url.startswith(context.get_url('home'))
    assert context.browser.is_text_present('Hi ' + username + '!')