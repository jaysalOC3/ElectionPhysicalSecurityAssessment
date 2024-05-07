from django import template

register = template.Library()

@register.inclusion_tag('assessment_app/progress_bar.html')
def progress_bar(progress):
    return {'progress': progress}