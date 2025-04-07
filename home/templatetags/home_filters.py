import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='highlight_digits')
def highlight_digits(value, css_class='font-for-numbers'):
    if not isinstance(value, str):
        value = str(value)

    result = re.sub(
        r'(\d)', 
        rf'<span class="{css_class}">\1</span>', 
        value
    )
    return mark_safe(result)