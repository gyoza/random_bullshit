# -*- coding: utf-8 -*-

import json
import urllib2
from collections import defaultdict

poop = defaultdict(dict)
poop["turds"] = json.loads(urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/').read())

wanted = [ "siacoin", "litecoin", "bitcoin", "vertcoin", "dogecoin", "antshares", "ripple", "neo", "iota", "stellar", 'raiblocks']
table_data = []
for each in poop["turds"]:
  for wants in wanted:
      if each["id"] == wants:
            coin = each["id"]
            symbol = "({})".format(each["symbol"])
            price = each["price_usd"]
            if "-" in each["percent_change_1h"]:
              onehour = "↓ {}%".format(each["percent_change_1h"].replace('-', ''))
            else:
              onehour = "↑ {}%".format(each["percent_change_1h"])
            if "-" in each["percent_change_24h"]:
              twentyfour = "↓ {}%".format(each["percent_change_24h"].replace('-', ''))
            else:
              twentyfour = "↑ {}%".format(each["percent_change_24h"])
            if "-" in each["percent_change_7d"]:
              sevendays = "↓ {}%".format(each["percent_change_7d"].replace('-', ''))
            else:
              sevendays = "↑ {}%".format(each["percent_change_7d"])
            table_data.append([coin, symbol, price, onehour, twentyfour, sevendays])
table_data.sort(key=lambda x: float(x[2]), reverse=True)
table_data.insert(0, ["coin", "symbol",  "price", "1hour", "24hour", "7days"])
col_width = max(len(word) for row in table_data for word in row) + 2
print "--------------------- ---- ----- -- ---- - -- -   -\n"
first = True
for row in table_data:
  if first:
    final = "".join(word.decode('utf-8').ljust(col_width) for word in row)
    print final.encode('utf-8')
    print "--------------------- ---- ----- -- ---- - -- -   -"
    first = False
  else:
    final = "".join(word.decode('utf-8').ljust(col_width) for word in row)
    print final.encode('utf-8')
print "\n[  Item value represented in USD.  ]\n"