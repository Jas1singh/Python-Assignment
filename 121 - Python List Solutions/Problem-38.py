#''' Problem 38: '''

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    matrix.append(list(map(int, input().split())))

top = 0
bottom = rows - 1
left = 0
right = cols - 1

result = []

while top <= bottom and left <= right:

    # Left to Right
    for j in range(left, right + 1):
        result.append(matrix[top][j])

    top += 1

    # Top to Bottom
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])

    right -= 1

    # Right to Left
    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])

        bottom -= 1

    # Bottom to Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])

        left += 1

print("Spiral order:", result)
