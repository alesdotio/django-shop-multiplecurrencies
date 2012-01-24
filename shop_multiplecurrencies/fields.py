from django.conf import settings
from django.utils.translation import string_concat
import threading

class MultipleCurrenciesField(object):
    def __init__(self, field_class, *args, **kwargs):
        self.field_class = field_class
        self.args = args
        self.kwargs = kwargs

    def contribute_to_class(self, cls, name):
        self.name = name
        setattr(cls, self.name, self)
        for currency_code, currency_name in settings.SHOP_CURRENCIES:
            field_name = '%s_%s' % (name, currency_code)
            field = self.field_class(*self.args, **self.kwargs)
            field.contribute_to_class(cls, field_name)
            field.verbose_name = string_concat(field.verbose_name, ' (', currency_code, ')')

    def __get__(self, instance, instance_type=None):
        if not instance:
            return ''
        return getattr(instance, '%s_%s' % (self.name, get_currency()))

    def __set__(self, instance, value):
        setattr(instance, '%s_%s' % (self.name, get_currency()), value)

    def __delete__(self, instance):
        delattr(instance, '%s_%s' % (self.name, get_currency()))

def set_currency(currency):
    setattr(threading.currentThread(), 'shop_currency', currency)

def get_currency():
    return getattr(threading.currentThread(), 'shop_currency', settings.SHOP_CURRENCIES[0][0])