from random import uniform
from timeit import timeit


def merge_sort(numbers):
    if len(numbers) > 1:
        center = len(numbers) // 2
        left = numbers[:center]
        right = numbers[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
        return numbers


numbers = int(input('Введите число элементов: '))
test = [uniform(0, 50) for _ in range(numbers)]
print(f'Исходный  - {test}')
print(f'Отсортированный - {merge_sort(test)}')

n_10 = [uniform(0, 50) for _ in range(10)]
n_100 = [uniform(0, 50) for _ in range(100)]
n_1000 = [uniform(0, 50) for _ in range(1000)]

print('10 элементов', timeit('merge_sort(n_10)', globals=globals(), number=1000))
print('100 элементов', timeit('merge_sort(n_100)', globals=globals(), number=1000))
print('1000 элементов', timeit('merge_sort(n_1000)', globals=globals(), number=1000))