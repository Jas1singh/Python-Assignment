#''' Problem 40: '''

nums = list(map(int, input("Enter elements: ").split()))

farthest = 0

for i in range(len(nums)):

    if i > farthest:
        print(False)
        break

    farthest = max(farthest, i + nums[i])

else:
    print(True)
