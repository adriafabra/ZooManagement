from functools import reduce
from behave import *
import operator
from django.db.models import Q
from ZooWeb.models import GroupOfVisitor

use_step_matcher("parse")

@when(u'I book a tour')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('visitors_create'))
        if context.browser.url == context.get_url('visitors_create'):
            form = context.browser.find_by_tag('form').first

            values = {}
            for heading in row.headings:
                values[heading] = row[heading]
                
            context.browser.fill_form(values)
            
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for booking by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    
    visit = GroupOfVisitor.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(visit)

@then(u'There are {count:n} bookings')
def step_impl(context, count):
    assert count == GroupOfVisitor.objects.count()


@when(u'I try to access booking page')
def step_impl(context):
    context.browser.visit(context.get_url('/zooweb/groupofvisitors/create'))

