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


@register.filter(name='br_every_two')
def br_every_two(value):
    if not isinstance(value, str):
        return value

    words = value.split()
    lines = [' '.join(words[i:i+2]) for i in range(0, len(words), 2)]
    return '<br>'.join(lines)