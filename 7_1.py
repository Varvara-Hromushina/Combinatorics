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


alphabet = [1, 2, 3, 4, 5, 6, 7, 8]
n = 5

permutations = GeneratePermutations(alphabet, n)

# Открываем файл для записи
with open("permutations.txt", "w") as file:
    # Записываем каждое размещение в отдельный строку
    for permutation in permutations:
        file.write(" ".join(str(x) for x in permutation) + "\n")

    # Записываем количество элементов в последнюю строку
    file.write(f"Количество элементов: {len(permutations)}")
