n1, x1 = input().split()
n = int(n1)
x = str(x1)
list1 = [l ,m ,r]
def cupGame(n ,x):
    if n > 0 & n < 1001:
        if x.lower() in list1:
            result = x
            for i in range(n):
                first, second = input().split()
                if first == result:
                    result = second
                elif second == result:
                    result = first
                else:
                    pass
        else:
            return error 
    return result
c = cupGame(n ,x)
print(c)