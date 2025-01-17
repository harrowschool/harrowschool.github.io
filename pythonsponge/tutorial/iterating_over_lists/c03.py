personal_allowances = [11850, 12500, 12500, 12570]

for i in range(len(personal_allowances)):
  print("in tax year starting April {}...".format(2018 + i))
  print("the income tax personal allowance was £{}".format(personal_allowances[i]))