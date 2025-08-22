from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """Agrega clases CSS a widgets del formulario en plantillas."""
    existing = field.field.widget.attrs.get('class', '')
    classes = f"{existing} {css}".strip()
    field.field.widget.attrs['class'] = classes
    return field