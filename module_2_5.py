def get_matrix (n, m, value): # Объявляем функцию с тремя параметрами.
    matrix = []                # Внутри функции создаем пустой список.
    for i in range(n):          # Перебираем все значения параметра n.
        matrix.append([]) # добавляем пустой список в список matrix.
        for j in range(m): # Перебираем все значения параметра m.
            matrix[i].append(value) # Пишем в список matrix с индексом i значение
    return(matrix)          # Возвращаем результат выполнения.

# Примеры работы функции def get_matrix.
 
result_1 = get_matrix(2, 2, 10)
print(result_1)
result_2 = get_matrix(3,5,42)
print(result_2)
result_3 = get_matrix(4,2,13)
print(result_3)

