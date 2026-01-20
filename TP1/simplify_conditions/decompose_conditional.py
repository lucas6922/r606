if not dateBetween(SUMMER_START,SUMMER_END):
    charge = quantity * winterRate + winterServiceCharge
else:
    charge = quantity * summerRate

def dateBetween(start_date, end_date):
    return date.after(start_date) or date.before(end_date)