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


def PlacementWithRepetitions(elements, length):
    if length == 0:
        return [[]]
    else:
        result = []
        for element in elements:
            for tail in PlacementWithRepetitions(elements, length - 1):
                result.append([element] + tail)
        return result



def GenerateWords(alphabet):
    words = []
    triple_symbol = 2
    for remaining_symbols in PlacementWithRepetitions(alphabet, 3):  # остальные
        # все перестановки символов
        for permutation in GeneratePermutations([triple_symbol] * 3 + list(remaining_symbols), 3):
            words.append(''.join(str(symbol) for symbol in permutation))
    return words


alphabet = [1, 2, 3, 4, 5, 6, 7, 8]
words = GenerateWords(alphabet)

print(f"Количество слов: {len(words)//6}") # делим на 6, тк 222111 итп считается 6 раз (222111, 222111 итд считаются как разные слова)
print(words) # печатаем все возможные оставшиеся тройки элементов слова, тк три 2 зафиксированы
