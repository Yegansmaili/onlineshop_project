from django import template

register = template.Library()


@register.filter
def number_translate(value):
    value = str(value)
    x = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(x)  # applying x (translation table) to the value for translation
