def GenerateCombinations(alphabet, n):
    if n == 1:
        return [[x] for x in alphabet]

    combinations = []
    for i in range(len(alphabet)):
        current_element = alphabet[i]
        remaining_alphabet = alphabet[i + 1:]
        for permutation in GenerateCombinations(remaining_alphabet, n - 1):
            combinations.append([current_element] + permutation)

    return combinations


elements = []
print("Введите количество элементов множества: ")
n = int(input())
print("Введите элементы множества: ")
i = 0
while i != n:
    elem = input()
    elements.append(elem)
    i += 1
print("Введите значение k: ")
length = int(input())

print(f"Количество сочетаний по {length} элементам = {len(GenerateCombinations(elements, length))}")
print("Сочетания: ")
for element in GenerateCombinations(elements, length):
    print(element)
