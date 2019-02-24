[w, h] = list(map(int, input("Введите w и h через пробел: ").split()))
if 1 <= w <= 100 and 1 <= h <= 100:
    print("input correct")
else:
    print("input incorrect")
while True:
    n = int(input("Input n: "))
    if 0 <= n <= 5000:
        print("input n - correct")
        break
    else:
        print("input n - incorrect")
area = []
for i in range(n):
    while True:
        xy = list(map(int, input("Введите коорд {}-го: ".format(i + 1)).split()))
        if 0 <= xy[0] <= xy[2] <= w and 0 <= xy[1] <= xy[3] <= h:
            break
        else:
            print("something wrong")
    for x in range(xy[0], xy[2] + 1):
        for y in range(xy[1], xy[3] + 1):
            area.append((x, y))
S = w * h - len(set(area))
print(S)
