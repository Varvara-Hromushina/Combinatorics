def PlacementWithRepetitions(elements, length):
    if length == 0:
        return [[]]
    else:
        result = []
        for element in elements:
            for tail in PlacementWithRepetitions(elements, length - 1):
                result.append([element] + tail)
        return result


elements = []
print("Введите количество элементов множества: ")
n = int(input())
print("Введите элементы множества: ")
i = 0
while (i != n):
    elem = input()
    elements.append(elem)
    i += 1
print("Введите значение k: ")
length = int(input())

print(f"Количество размещений с повторениями по {length} элементам = {len(PlacementWithRepetitions(elements, length))}")
print("Размещения с повторениями: ")
for element in PlacementWithRepetitions(elements, length):
    print(element)
