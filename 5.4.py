n = int(input("Введите количество ступенек: "))
variants = [0] * (n+1)
variants[0] = 1
variants[1] = 1
variants[2] = 2

for i in range(3, n+1):
    variants[i] = variants[i-1] + variants[i-2] + variants[i-3]

print("Количество вариантов перемещения ребенка по лестнице:", variants[n])


