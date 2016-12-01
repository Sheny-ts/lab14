A = list(input().split())
i = A.index('0')
A = A[0:i]

s = A[0]
n = 0
for i in range(len(A)):
    if A[i] > s:
        s = A[i]
        n = 0
    if A[i] == s:
        n += 1
print(n)