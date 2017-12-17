def rhs(N):
    return N * (N + 1) / 2

def lhs(N):
    total = 0
    i = 0
    while i < N:
        i = i + 1
        total = total + i
    return total

print(lhs(5), rhs(5), lhs(5) == rhs(5))
print(lhs(50), rhs(50), lhs(50) == rhs(50))
