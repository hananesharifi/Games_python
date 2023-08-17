numberOfRoad = eval(input())
maxPart = 0
for i in range(numberOfRoad):
    for j in range(numberOfRoad ,0 ,-1):
        if i + j == numberOfRoad:
            a = (i + 1) * (j + 1)
            if a > maxPart:
                maxPart = a
print(maxPart)