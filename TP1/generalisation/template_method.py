class Site():

  units = 0
  rate = 0.0
  tax_rate = 0.5

  def __init__(self, p_units : int, p_rate : float):
    self.units = p_units
    self.rate = p_rate



class ResidentialSale(Site):

  def getBillableAmount(self):
    base = self.units * self.rate
    tax = base * self.tax_rate
    return base + tax


class LifelineSite(Site):
  def getBillableAmount(self):
    base = self.units * self.rate * 0.5
    tax = base * self.tax_rate * 0.2
    return base + tax


resident = ResidentialSale(5000, 1.5)
print(resident.getBillableAmount())

lifeline = LifelineSite(5000, 1.5)
print(lifeline.getBillableAmount())
