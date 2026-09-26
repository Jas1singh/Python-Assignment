#''' Problem 34: '''

nums = list(map(int, input("Enter elements: ").split()))

n = len(nums)
result = [1] * n

for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product = product * nums[j]

    result[i] = product

print("Result:", result)
