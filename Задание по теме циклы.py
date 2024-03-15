a = int(input())
b = int(input())
totle = 0
quantity = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        totle += i
        quantity += 1
print(totle/quantity)