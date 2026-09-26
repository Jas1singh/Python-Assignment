#''' Problem 37: '''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    matrix.append(list(map(int, input().split())))

zero_rows = []
zero_cols = []

# Find positions containing zero
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.append(i)
            zero_cols.append(j)

# Set rows and columns to zero
for i in range(rows):
    for j in range(cols):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0

print("Result:")

for row in matrix:
    print(row)
