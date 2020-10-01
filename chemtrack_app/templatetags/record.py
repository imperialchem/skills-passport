from django import template
from .. import controllers


register = template.Library()

@register.simple_tag(name='is_descriptor_selected')
def is_descriptor_selected(descriptor, number, button_level):
    if number == 0 and descriptor.draft_level == button_level:
        return "selected"
    elif number == 1 and descriptor.feedback_level == button_level:
        return "selected"
    elif number == 2 and descriptor.final_level == button_level:
        return "selected"
    else:
        return ""


@register.simple_tag(name='can_modify')
def can_modify(record, user, state):
    return controllers.can_modify(record, user, state)

@register.simple_tag(name='list_levels_generate')
def list_levels_generate(state):
    if state == 0 or state == 2:
        return "123456"
    else:
        return "-=+"

@register.simple_tag(name='pre_select')
def pre_select(record, state):
    """
        Function that says if the descriptor state should be displayed by default when the page is loaded
        state is either 0,1,2:
            0: draft_level & draft_statement

    """
    display = ""
    if record.state == 0:
        if state == 0:
            display = "selected"
    elif record.state == 1:
        if state == 0 or state == 1:
            display = "selected"
    elif record.state == 2:
        if state == 1 or state == 2:
            display = "selected"
    else:
        if state == 2:
            display = "selected"
    return display


@register.simple_tag(name='can_submit')
def can_submit(record, user):
    return controllers.can_submit(record, user)