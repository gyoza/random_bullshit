import json
import urllib2
from collections import defaultdict

poop = defaultdict(dict)
poop["turds"] = json.loads(urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/').read())

wanted = [ "siacoin", "litecoin", "bitcoin", "vertcoin", "dogecoin", "antshares", "ripple", "neo"]
print "Items represented in USD.\n"
table_data = [["coin", "price", "1hour", "24hour", "7days"]]
for each in poop["turds"]:
  for wants in wanted:
      if each["id"] == wants:
            coin = each["id"]
            price = each["price_usd"]
            if "-" in each["percent_change_1h"]:
              onehour = "{}%".format(each["percent_change_1h"])
            else:
              onehour = "+{}%".format(each["percent_change_1h"])
            if "-" in each["percent_change_24h"]:
              twentyfour = "{}%".format(each["percent_change_24h"])
            else:
              twentyfour = "+{}%".format(each["percent_change_24h"])
            if "-" in each["percent_change_7d"]:
              sevendays = "{}%".format(each["percent_change_7d"])
            else:
              sevendays = "+{}%".format(each["percent_change_7d"])
            table_data.append([coin, price, onehour, twentyfour, sevendays])
            col_width = max(len(word) for row in table_data for word in row) + 5  # padding
for row in table_data:
  print "".join(word.ljust(col_width) for word in row)

