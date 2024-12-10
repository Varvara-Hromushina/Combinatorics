# x1 + x2 + x3 = 15
"""
Найти количество всевозможных букетов из 15 цветов,
каждый состоящий из четного числа белых и красных цветов и нечетного количества розовых.
"""

buket = [0, 0, 0]
count = 0
print("Возможные букеты из 15 цветов: ")
print("Белый Розовый Красный")
for i in range(0, 16):
    for j in range(0, 16):
        for k in range(0, 16):
            buket = [i, j, k]  # белый, розовый, красный
            if sum(buket) == 15 and i % 2 == 0 and j % 2 != 0 and k % 2 == 0:
                count += 1
                print(buket)

print(f"Количество букетов с учетом условий четности и нечетности: {count}")