# Problem 92:

s1 = "pqqp"
s2 = "qpqp"

def pq_balanced(s):
    count = 0

    for ch in s:
        if ch == 'p':
            count += 1
        elif ch == 'q':
            count -= 1

        if count < 0:
            return False

    return count == 0

print(pq_balanced(s1))
print(pq_balanced(s2))
