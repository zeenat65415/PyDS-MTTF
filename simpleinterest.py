#simpleinterest and amount
principle=float(input("Enter principle=>"))
rate=float(input("Enter rate=>"))
time=float(input("Enter time=>"))
SI=principle*rate*time/100
amount=principle+SI
print(F"Simple Interest is:{SI}")
print(f"Amount is:{amount}")