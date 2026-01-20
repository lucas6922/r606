class Site():

  units = 0
  rate = 0.0
  tax_rate = 0.5

  def __init__(self, p_units : int, p_rate : float):
    self.units = p_units
    self.rate = p_rate

  def getBaseAmount(self):
    raise NotImplementedError
  
  def getTaxeAmount(self):
    raise NotImplementedError
  
  def getBillableAmount(self):
    return self.getBaseAmount() + self.getTaxeAmount()



class ResidentialSale(Site):

  def getBaseAmount(self):
    return self.units * self.rate
  
  def getTaxeAmount(self):
    return self.getBaseAmount() * self.tax_rate


class LifelineSite(Site):

  def getBaseAmount(self):
    return self.units * self.rate * 0.5
  
  def getTaxeAmount(self):
    return self.getBaseAmount() * self.tax_rate * 0.2


resident = ResidentialSale(5000, 1.5)
print(resident.getBillableAmount())

lifeline = LifelineSite(5000, 1.5)
print(lifeline.getBillableAmount())
