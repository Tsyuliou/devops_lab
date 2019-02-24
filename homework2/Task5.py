n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())
happenies = 0
for i in array:
    if i in A:
        happenies += 1
    elif i in B:
        happenies -= 1
    else:
        happenies = happenies
print(happenies)
