# Восстановить перестановку по введенному вектору инверсий

# функция восстановления
def recover(inversions):
    n = len(inversions)
    numbers = list(range(1, n + 1))

    result = [None] * n

    for i in reversed(range(0, n)):
        d = inversions[i] + 1
        a = numbers[-d]
        result[i] = a
        numbers.remove(a)

    return result


print("Введите длину n:")
length = int(input())  # длина вектора инверсий/перестановки
inversions = []  # вектор инверсий

print("Введите компоненты:")
for i in range(0, length):
    component = int(input())
    inversions.append(component)

print(f"Исходная перестановка: {recover(inversions)}")
