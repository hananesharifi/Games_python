n = int(input())
position = []
a_str = input().split()
for elemnt in a_str:
    position.append(int(elemnt))

def first(positions):
    results = [positions[0]]
    destination = [0]
    for i in range(1 ,n):
        a = results[i - 1] - 3
        results.append(a)
        b = a - positions[i]
        destination.append(b)
    return destination
f = first(position)
def second(positions):
    results = [positions[0]]
    destination = [0]
    for i in range(1 ,n):
        a = results[i - 1] + 3
        results.append(a)
        b = a - positions[i]
        destination.append(b)
    return destination
s = second(position)
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += abs(f[i])
    sum2 += abs(s[i])
if sum1 <= sum2:
    for e in f:
        if e > 0:
            print('+'+str(e))
        else:
            print(e)

else:
    for e in s:
        if e > 0:
            print('+'+str(e))
        else:
            print(e)