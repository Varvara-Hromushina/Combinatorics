def GeneratePermutations(alphabet):
    if len(alphabet) == 0:
        return [[]]
    permutations = []
    for i in range(len(alphabet)):
        current_element = alphabet[i]
        remaining_alphabet = alphabet[:i] + alphabet[i + 1:]
        for permutation in GeneratePermutations(remaining_alphabet):
            permutations.append([current_element] + permutation)

    return permutations


elements = []
print("Введите количество элементов алфавита: ")
n = int(input())
print("Введите элементы алфавита: ")
i = 0
while (i != n):
    elem = input()
    elements.append(elem)
    i += 1

print(f"Количество перестановок = {len(GeneratePermutations(elements))}")
print("Перестановки: ")
for element in GeneratePermutations(elements):
    print(element)
