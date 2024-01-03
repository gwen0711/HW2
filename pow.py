print("a^b = ?")
a = int(input("enter a: "))
b = int(input("enter b: "))
c = 1
for i in range(b):
    c *= a
print(f"{a}^{b} = {c}")
