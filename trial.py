#from emi import emi_calculator
import emi

amount = 100000#float(input("Enter principle amount:"))
rate = 12#float(input("Enter annual rate of interest:"))
tenure = 12#int(input("Enter tenure in months:"))

emis = emi.emi_calculator(amount, rate, tenure)
index = 1
total = 0
for emi in emis:
    print("EMI For Month ", index, " is :", emi)
    total += emi
    index += 1

print("Total:", total)