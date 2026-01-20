price = 5

def raise_price_by_ten():
  global price
  price += 10

def raise_price_by_five():
  global price
  price += 5


raise_price_by_ten()
raise_price_by_five()
print(price)
