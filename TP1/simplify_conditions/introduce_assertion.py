def getExpenseLimit(self):
  # Should have either expense limit or
  # a primary project.
  if self.expenseLimit != NULL_EXPENSE:
    return self.expenseLimit
  else:
    return self.primaryProject.getMemberExpenseLimit()
