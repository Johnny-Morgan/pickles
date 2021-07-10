from django import template

register = template.Library()


@register.filter(name='calc_discounted_price')
def calc_discounted_price(price, discount):
    '''
    Returns discounted product price
    '''
    return float(price) * (1 - discount / 100)
