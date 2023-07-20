n1 ,s1 ,d1 = input().split()
n = int(n1)
s = int(s1)
d = int(d1)

matrix = [[0 for _ in range(n)] for _ in range(n)]

def fill_spiral_matrix(matrix, n):
    counter = 1
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1

    while counter <= n * n:
        # Fill top row
        for j in range(start_col, end_col + 1):
            matrix[start_row][j] = counter
            counter += 1
        start_row += 1

        # Fill rightmost column
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = counter
            counter += 1
        end_col -= 1

        # Fill bottom row
        for j in range(end_col, start_col - 1, -1):
            matrix[end_row][j] = counter
            counter += 1
        end_row -= 1

        # Fill leftmost column
        for i in range(end_row, start_row - 1, -1):
            matrix[i][start_col] = counter
            counter += 1
        start_col += 1

    return matrix
matrix = fill_spiral_matrix(matrix, n)
si = 0
sj = 0
di = 0
dj = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == s:
            si = i
            sj = j
        if matrix[i][j] == d:
            di = i
            dj = j
result1 = si -di
if result1 != 0:
    if result1 < 0:
        print(str(abs(result1)) + ' R')
    else:
        print(str(result1) + ' L')
result2 = sj - dj
if result2 != 0:
    if result2 < 0:
        print(str(abs(result2)) + ' U')
    else:
        print(str(result2) + ' D')