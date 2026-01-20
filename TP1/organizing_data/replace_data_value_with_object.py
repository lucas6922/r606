class Order():
  _price = 0
  _customer = ""
  _address = ""

  def __init__(self, p_price : int, p_customer : str, p_address):
    self._price = p_price
    self._customer = p_customer
    self._address = p_address



order = Order(5, "Arthur", "85 rue du port.")
print("prix:", order._price)
print("client:", order._customer)
print("address:", order._address)
