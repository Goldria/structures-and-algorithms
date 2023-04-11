import time
import random


# Сортировка расчёской, оставляя четные элементы на своих местах
def comb_sort_odd(array):
    n = len(array)
    gap = n
    shrink = 1.247
    sorted = False

    while not sorted:
        gap = int(gap / shrink)  # уменьшаем зазор
        if gap <= 1:
            gap = 1
            sorted = True  # если зазор равен 1, то массив отсортирован
        i = 0
        while i + gap < n:
            # Пропускаем четные элементы
            if array[i] % 2 == 0:
                i += 1
                continue
            if array[i + gap] % 2 == 0:
                i += 1
                continue
            if array[i] > array[i + gap]:
                # Меняем элементы местами, если они находятся в неправильном порядке
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
            i += 1

    return array


# Сортировка "прямой выбор", оставляя четные элементы на своих местах
def selection_sort_odd(array):
    n = len(array)
    for i in range(n):
        if array[i] % 2 == 0:  # Пропускаем четные элементы
            continue
        min_idx = i
        for j in range(i + 1, n):
            if array[j] % 2 == 0:  # Пропускаем четные элементы
                continue
            if array[min_idx] > array[j]:
                min_idx = j
        if min_idx != i:
            # Меняем элементы местами
            array[i], array[min_idx] = array[min_idx], array[i]

    return array


def main():
    # тестирование
    test_cases = [
        # 1. Неотсортированный массив
        [5, 2, 7, 1, 9, 3, 8, 4, 6],
        # 2. Частично отсортированный массив
        [1, 2, 3, 5, 4, 6, 7, 9, 8],
        # 3. Отсортированный массив в обратном порядке
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        # 4. Массив с одним элементом
        [1],
        # 5. Массив из одинаковых элементов
        [5, 5, 5, 5, 5],
        # 6. Большой массив случайных чисел
        [random.randint(0, 1000) for _ in range(1000)],
        # 7. Массив с повторяющимися элементами
        [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        # 8. Массив с отрицательными числами
        [-5, -2, 7, 1, -9, 3, 8, -4, 6],
        # 9. Массив, состоящий только из четных чисел
        [2, 4, 6, 8, 10],
        # 10. Массив, состоящий только из нечетных чисел
        [1, 3, 9, 5, 7]
    ]
    for i, test_case in enumerate(test_cases):
        print(f"Тест {i + 1}: {test_case}")

        # Измеряем время выполнения сортировки прямым выбором
        start_time = time.time()
        sorted_array = selection_sort_odd(test_case.copy())
        end_time = time.time()
        print(f"Прямой выбор: {sorted_array}")
        print(f"Время выполнения: {end_time - start_time:.5f} секунд")

        # Измеряем время выполнения сортировки расческой
        start_time = time.time()
        sorted_array = comb_sort_odd(test_case.copy())
        end_time = time.time()
        print(f"Расчёска: {sorted_array}")
        print(f"Время выполнения: {end_time - start_time:.5f} секунд")


if __name__ == '__main__':
    main()
