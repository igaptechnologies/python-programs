amount = float(input("Enter amount:"))
rate = float(input("Enter rate of interest:"))
duration = float(input("Enter duration of loan:"))
si = (amount * rate * duration) / 100
print("Simple Interest is:", si)
print("Total Amount To repay:", (amount + si))