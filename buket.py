# x1 + x2 + x3 = 15

buket = [0, 0, 0]
count = 0
for i in range(0, 16):
    for j in range(0, 16):
        for k in range(0, 16):
            buket = [i, j, k]
            if sum(buket) == 15 and i % 2 == 0 and j % 2 != 0 and k % 2 == 0:
                count += 1
                print(buket)

print(count)
