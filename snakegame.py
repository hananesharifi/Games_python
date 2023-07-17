n1 ,m1 = input().split()
n = int(n1)
m = int(m1)

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j] ,end=' ')
        print()
def snakeMatrix(n ,m):
    matrix = []
    for i in range(n):
        list1 = []
        if i % 2 == 0:
            list1 = [j + (i * m) for j in range(1 ,m + 1)]
        else:
            list1 = [j for j in range((i + 1) * m ,m ,-1)]

        matrix.append(list1)
    return printMatrix(matrix)

snakeMatrix(n ,m)