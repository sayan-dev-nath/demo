from django import template

register = template.Library()


@register.filter(name="iamToweare")
def myreplace(value, arg):
    return value.replace(arg, "We are")
