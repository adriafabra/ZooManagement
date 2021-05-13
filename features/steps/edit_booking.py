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


@when(u'I edit the booking with date "2022-06-28" and hour "13:00"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the booking with date "2022-06-28" and hour "13:00"')


@when(u'I try to edit a booking')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I try to edit a booking')


@then(u'Server responds with page containing "403 Forbidden"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Server responds with page containing "403 Forbidden"')