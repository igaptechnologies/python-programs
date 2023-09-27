def emi_calculator(amount, rate_year, tenure_months):
    emis = []
    monthly_installment = amount / tenure_months
    for i in range (0, tenure_months):
        pending_amount = amount - (monthly_installment * i)
        interest = ((pending_amount * (tenure_months / 12) * rate_year) / 100) / tenure_months
        emi_amount = monthly_installment  + interest
        emis.append(emi_amount)
    return emis


# amount = 100000#float(input("Enter principle amount:"))
# rate = 12#float(input("Enter annual rate of interest:"))
# tenure = 12#int(input("Enter tenure in months:"))

# emis = emi_calculator(amount, rate, tenure)
# index = 1
# total = 0
# for emi in emis:
#     print("EMI For Month ", index, " is :", emi)
#     total += emi
#     index += 1

# print("Total:", total)