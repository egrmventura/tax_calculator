import sys

fedtaxDict = [
    [0.1, [11000, 11000, 15700, 22000]],
    [0.12, [44725, 44725, 59850, 89450]],
    [0.22, [95375, 95375, 95350, 190750]],
    [0.24, [182100, 182100, 182100, 364200]],
    [0.32, [231250, 231250, 231250, 462500]],
    [0.35, [578125, 346875, 578100, 693750]]
] #
tr = 0
grp = 3

def fed_tax_due(income=0, tr=0, grp=0, amt_due=0):    
    if tr > 6 or grp > 3:
        print("Error: tax rate index or group id is too large.")
        return
    if tr > 5: 
        amt_due += (0.37 * income)
        return amt_due
    prevCutoff = 0 if tr == 0 else fedtaxDict[tr-1][1][grp]
    cutoff = fedtaxDict[tr][1][grp] - prevCutoff
    tax_rate = fedtaxDict[tr][0]
    taxable_income = income if income < cutoff else cutoff
    amt_due += (tax_rate * taxable_income)
    income -= taxable_income
    if income > 0:
        tr += 1
        return fed_tax_due(income, tr, grp, amt_due)
    return amt_due

def tax_info_intake():
    income = float(input("Enter your income (USD): $"))
    amt_due = round(fed_tax_due(income),2)
    fed_percentage = round(amt_due / income, 4)
    return [amt_due, fed_percentage]



fed_due = tax_info_intake()
print(f'You will owe ${fed_due[0]} in federal income tax, {100*fed_due[1]}% of your annual income.')
print("mobile test")
