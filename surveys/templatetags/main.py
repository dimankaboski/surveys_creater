
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template.defaultfilters import filesizeformat

from datetime import datetime, timedelta, timezone

from accounts.models import User
from surveys.models import Survey

register = template.Library()


@register.simple_tag()
def get_resp_statistic(resp, el, survey):
    data = {
        'resp_count': 0,
        'resp_percent': 0,
    }
    resp = resp.replace('\r', '').replace('\n', '')
    filled = survey.filledsurvey_set.all()
    for sur in filled:
        for user_resp in sur.elementvalue_set.filter(element=el):
            for many_resp in user_resp.value.split('\n'):
                if many_resp.replace('\r', '') == resp:
                    data['resp_count'] += 1
    if filled.count() != 0:
        data['resp_percent'] = str(round(data['resp_count'] * 100 / filled.count(), 1)).replace(',', '.')
    return data


@register.simple_tag()
def get_el_response_count(el, survey):
    filled = survey.filledsurvey_set.all()
    filled_count = 0
    for sur in filled:
        for user_resp in sur.elementvalue_set.filter(element=el):
            if user_resp.value != '':
                filled_count += 1
    return filled_count