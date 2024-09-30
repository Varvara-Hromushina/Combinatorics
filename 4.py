def GenerateSubset(alphabet, n):
    if n == 0:
        return [[]]

    subset = []
    for i in range(len(alphabet)):
        current_element = alphabet[i]
        remaining_alphabet = alphabet[i + 1:]
        for permutation in GenerateSubset(remaining_alphabet, n - 1):
            subset.append([current_element] + permutation)

    return subset


elements = []
print("Введите количество элементов множества: ")
n = int(input())
print("Введите элементы множества: ")
i = 0
while i != n:
    elem = input()
    elements.append(elem)
    i += 1

j = 0
print("Подмножества: ")
while j != n + 1:
    for element in GenerateSubset(elements, j):
        print(element)
    j += 1
