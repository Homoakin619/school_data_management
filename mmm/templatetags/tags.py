from django.template.defaultfilters import length
from mmm.models import Result,Student
from django import template

register = template.Library()

@register.filter
def c_string(myuser):
    mid = myuser.id
    result = myuser.result_set.get(id=mid)
    m_result = str(result)
    string = ''
    for letter in m_result:
        string += letter
        if letter.isdigit():
            string += '\n'
    return string

@register.filter
def con_result(result):
    m_result = str(result)
    string = ''
    for letter in m_result:
        string += letter
        if letter.isdigit():
            string += '\n'
    return string
