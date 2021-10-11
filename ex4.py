#inputx2, цикл, сравниваем, и записываем значение, enumerate создает словарь из массива, где ключ=индекс, знач=знач
def hDistance(s, t):
    d = 0
    for index, i in enumerate(s):
        if t[index] != i:
            d += 1
    return d


s = input()
t = input()
result = hDistance(s, t)
print(result)
