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
* Add `shop_multiplecurrencies.middleware.CurrencyMiddleware` to your
  `MIDDLEWARE_CLASSES` setting.
* Add a list of currencies to the `SHOP_CURRENCIES` setting like so

::

  SHOP_CURRENCIES=[ # lowercase codes, please
      ['chf', 'swiss franc'],
      ['eur', 'euro'],
  ]

Usage
=====

* Add a CurrencyField to your product model

::

  from shop_multiplecurrencies.fields import CurrencyField
  from shop.util.fields import CurrencyField as ShopCurrencyField

  class MyProduct(models.Model):
      # my fields ...
      price = CurrencyField(ShopCurrencyField)

* Extend BaseOrderItem

::

  TODO!!!


* Use the currency template filter in your templates

::

  {% load currency %}

  <p>This product's price is {{ price|currency }}</p>