temp = input("enter temperature")
temp = int(temp)
if temp>=100:
    print("Boiling")
if temp <=32 and temp <=99:
    print("liquid")
if temp<=32:
    print("freezing")