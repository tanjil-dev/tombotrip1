from django import template

register = template.Library()

def count(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')