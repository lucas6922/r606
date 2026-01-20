quantity = 5
itemPrice = 100


def discountedPrice(basePrice, seasonalDiscount, fees):
  return basePrice * seasonalDiscount - fees


def getFees():
  return 10


def getSeasonalDiscount():
  return 0.5

basePrice = quantity * itemPrice
seasonalDiscount = getSeasonalDiscount()
fees = getFees()
finalPrice = discountedPrice(basePrice, seasonalDiscount, fees)
print(finalPrice)
