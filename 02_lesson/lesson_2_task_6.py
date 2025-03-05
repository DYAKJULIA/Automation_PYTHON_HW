lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = []

for element in lst:

    if (element % 3 == 0) and (element < 30):
        result.append(element)

print(result)