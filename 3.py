def GeneratePermutations(alphabet, n):
    if n == 1:
        return [[x] for x in alphabet]

    permutations = []
    for i in range(len(alphabet)):
        current_element = alphabet[i]
        remaining_alphabet = alphabet[:i] + alphabet[i + 1:]
        for permutation in GeneratePermutations(remaining_alphabet, n - 1):
            permutations.append([current_element] + permutation)

    return permutations


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

print(f"Количество размещений по {length} элементам = {len(GeneratePermutations(elements, length))}")
print("Размещения: ")
for element in GeneratePermutations(elements, length):
    print(element)
