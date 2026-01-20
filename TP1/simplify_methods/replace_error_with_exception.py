class Account():
  balance = 50

  def withdraw(self, amount):
    if amount > self.balance:
      return -1
    else:
      self.balance -= amount
      return 0


account = Account()
print(account.withdraw(55))
