Z = input().split()
A = int(Z[1], base = int(Z[0]))
k = int(Z[2])
l = []
while A>=k:
    l.append(A % k)
    A = A//k
l.append(A)

print(l[::-1])