=================================
django SHOP - Multiple Currencies
=================================

This app adds support for multiple currencies to django SHOP.

Warning
=======

Do not use (yet)!
This app is still under development and might not work at all.

Installation
============

This requires django SHOP to work (https://github.com/chrisglass/django-shop)

* Add `shop_multiplecurrencies` to your INSTALLED_APPS in your settings.py
* Add `shop_multiplecurrencies.middleware.MultipleCurrenciesMiddleware` to your
  `MIDDLEWARE_CLASSES` setting
* Add a list of currencies to the `SHOP_CURRENCIES` setting like so

::

  SHOP_CURRENCIES=[ # lowercase codes, please
      ['chf', 'swiss franc'],
      ['eur', 'euro'],
  ]

Usage
=====

* Add a MultipleCurrenciesField to your product model

::

  from django.db import models
  from shop_multiplecurrencies.fields import MultipleCurrenciesField
  from shop.util.fields import CurrencyField

  class MyProduct(models.Model):
      # my fields ...
      price = MultipleCurrenciesField(CurrencyField)

The model will in our example have two fields: `price_chf` and `price_eur`.

* Extend BaseOrder with an additional field that tells us which currency the order was completed in

::

  from django.conf import settings
  from shop.models.defaults.bases import BaseOrder
  from shop.models.defaults.managers import OrderManager

  class MyOrder(BaseOrder):
      currency = models.CharField(max_length=6, choices=settings.SHOP_CURRENCIES)
      objects = OrderManager()

      def save(self, *args, **kwargs):
          self.currency = get_currency()
          super(MyOrder, self).save(*args, **kwargs)

      class Meta(object):
          abstract = False

* Use the currency template filter in your templates to prefix the price with the correct currency

::

  {% load currency %}

  <p>This product's price is {{ price|currency }}</p>