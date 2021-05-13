from functools import reduce
from behave import *
import operator
from django.db.models import Q
from ZooWeb.models import GroupOfVisitor, Sector
from django.contrib.auth.models import User


use_step_matcher("parse")

@given(u'Exists booking registered by "{username}"')
def step_impl(context, username):
    user = User.objects.get(username=username)
    
    for row in context.table:
        visit = GroupOfVisitor(user=user)
        for heading in row.headings:
            if(heading != 'sector'):
                setattr(visit, heading, row[heading])
        visit.save()
        sector = Sector.objects.get(name=row[row.headings[1]])
        
        visit.sector.add(sector)


@when(u'I edit the booking with date "{date}" and hour "{hour}"')
def step_impl(context, date, hour):
    visit = GroupOfVisitor.objects.get(date=date, hour=hour)
    context.browser.visit(context.get_url('visitors_edit', visit.pk))

    if context.browser.url == context.get_url('visitors_edit', visit.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


@when(u'I try to edit a booking with date "{date}" and hour "{hour}"')
def step_impl(context, date, hour):
    visit = GroupOfVisitor.objects.get(date=date, hour=hour)
    context.browser.visit(context.get_url('visitors_edit', visit.pk))


@then(u'Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)