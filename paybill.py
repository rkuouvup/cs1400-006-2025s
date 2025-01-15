amount = 93

bill_20 = amount // 20
amount = amount % 20 #amount - bill_20 * 20

bill_10 = amount // 10
amount = amount % 10

bill_5 = amount // 5
amount = amount % 5

bill_1 = amount

print(f"Jennifer should pay {bill_20} $20 dollar bills, {bill_10} $10 dollar bills, {bill_5} $ 10 dollars bill, and {bill_1} $1 dollar bill")
