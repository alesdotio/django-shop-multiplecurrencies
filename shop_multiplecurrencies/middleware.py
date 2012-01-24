from django.conf import settings
from fields import set_currency

class MultipleCurrenciesMiddleware(object):
    def get_currency_from_request (self, request):
        if hasattr(request, 'GET'):
            request_currency = request.GET.get('currency', False)
            if request_currency and request_currency in [codes[0] for codes in settings.SHOP_CURRENCIES]:
                return request_currency
        if hasattr(request, 'COOKIES') and request.COOKIES.get('shop_currency', False):
            return request.COOKIES.get('shop_currency')
        return settings.SHOP_CURRENCIES[0][0]

    def process_request(self, request):
        currency = self.get_currency_from_request(request)
        request.CURRENCY_CODE = currency
        set_currency(currency)

    def process_response(self, request, response):
        currency = getattr(request, 'CURRENCY_CODE', self.get_currency_from_request(request))
        response.set_cookie('shop_currency', currency)
        return response