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


def GenerateWords(alphabet):
    words = []
    for triple_symbol in alphabet:  # 3 повторяющихся символа
        for double_symbol in alphabet:  # 2 повторяющихся символа
            if triple_symbol != double_symbol:
                for remaining_symbols in GenerateCombinations(alphabet, 2):  # остальные
                    # выбранные символы не совпадают с triple_symbol и double_symbol
                    if all(symbol not in (triple_symbol, double_symbol) for symbol in remaining_symbols):
                        # все перестановки символов добавляем в words
                        for permutation in GeneratePermutations([triple_symbol] * 3 + [double_symbol] * 2 + list(remaining_symbols), 7):
                            words.append(''.join(str(symbol) for symbol in permutation))
    return words


alphabet = [1, 2, 3, 4, 5, 6, 7, 8]
words = GenerateWords(alphabet)
print(f"Количество слов: {len(words)}")
