def search_element(matrix, element):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1
    while i < m and j >= 0:
        if matrix[i][j] == element:
            return (i, j)
        elif matrix[i][j] < element:
            i += 1
        else:
            j -= 1
    return None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input('Введите значение, которое нужно найти:'))
result = search_element(matrix, element)
if result:
    print(f"Элемент {element} найден в позиции {result}")
else:
    print(f"Элемент {element} не найден")
