from django import template
from shop_multiplecurrencies.fields import get_currency

register = template.Library()

@register.filter('currency')
def currency(amount):
    # Amount is a Decimal
    amount.normalize()
    return "%s %.2f" % (get_currency().upper(), amount)