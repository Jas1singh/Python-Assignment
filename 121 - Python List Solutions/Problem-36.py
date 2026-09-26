#''' Problem 36: '''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter target: "))

left = 0
right = rows * cols - 1

found = False

while left <= right:
    mid = (left + right) // 2

    r = mid // cols
    c = mid % cols

    if matrix[r][c] == target:
        found = True
        break

    elif matrix[r][c] < target:
        left = mid + 1

    else:
        right = mid - 1

print(found)
