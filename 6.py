def GenerateCombinations(alphabet, n):
    if n == 0:
        return [[]]

    combinations = []
    for i in range(len(alphabet)):
        current_element = alphabet[i]
        for permutation in GenerateCombinations(alphabet[i:], n - 1):
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

j = 0
while j != n + 1:
    print(f"Сочетания с повторениями при k = {j}: ")
    for element in GenerateCombinations(elements, j):
        print(element)
    j += 1
