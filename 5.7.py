def find_missing_number(arr):
    n = len(arr)
    buckets = [0] * (n+1)

    for num in arr:
        if num > 0 and num <= n:
            buckets[num] = 1
    for i in range(1, n+1):
        if buckets[i] == 0:
            return i
    return n+1

arr = [3, 4, -1, 1, 5, 2, 7]
print('Наименьшее пропущенное число: \n ',find_missing_number(arr))

