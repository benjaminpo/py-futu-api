# -*- coding: utf-8 -*-
from futu import *


quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

"""-------------------------------------------------"""

from futu.quote.quote_get_warrant import Request
from futu.quote.quote_stockfilter_info import SimpleFilter

field = SimpleFilter()
field.filter_min = 100
field.filter_max = 1000
field.stock_field = StockField.CUR_PRICE

field2 = SimpleFilter()
field2.filter_min = 100
field2.filter_max = 1000
field2.stock_field = StockField.VOLUME_RATIO

field3 = SimpleFilter()
field3.stock_field = StockField.CUR_PRICE_TO_HIGHEST52_WEEKS_RATIO
field3.is_no_filter = True
print(quote_ctx.get_stock_filter(StockMarket.HK, [field, field2, field3]))

"""-------------------------------------------------"""
# req = Request()
# req.sort_field = SortField.CODE
# req.ascend = True
# req.type_list = [WrtType.BEAR, WrtType.CALL]
# req .issuer_list = [Issuer.CS, Issuer.CT, Issuer.EA]
# print(quote_ctx.get_warrant("HK.00700", req))

quote_ctx.close()


