loan = float(input("Enter amound of loan: "))
interest = float(input("Enter interest rate: ")) / 100 / 12
m_payment = float(input("Enter monthly payment: "))

i1 = round(interest * loan, 2)
b1 = loan + i1 - m_payment
i2 = round(interest * b1, 2)
b2 = b1 + i2 - m_payment
i3 = round(interest * b2, 2)
b3 = b2 + i3 - m_payment

print()
print(f"The interests for the first month is ${i1:.2f}.")
print(f"The balance remaining after first payment is ${b1:.2f}\n")
print(f"The interests for the second month is ${i2:.2f}.")
print(f"The balance remaining after second payment is ${b2:.2f}\n")
print(f"The interests for the third month is ${i3:.2f}.")
print(f"The balance remaining after third payment is ${b3:.2f}")

