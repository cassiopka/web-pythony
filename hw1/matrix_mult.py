n = int(input())

matrix_a = []
for _ in range(n):
    row = []
    for num in map(int, input().split()):
        row.append(num)
    matrix_a.append(row)

matrix_b = []
for _ in range(n):
    row = []
    for num in map(int, input().split()):
        row.append(num)
    matrix_b.append(row)

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

for row in result:
    print(' '.join(map(str, row)))
