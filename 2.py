k = 0
s1 = 1
s2 = 1
while s1 != 0 and s2 !=0:
    s = input().split()
    s1 = int(s[0])
    s2 = int(s[1])
    if s1//100 != 0 or s2//100 != 0:
        if s1%2 == 0 and s2%7 == 0:
            k+=1
print(k)