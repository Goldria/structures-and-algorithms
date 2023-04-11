import random


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]


def find_matches(arr, key):
    arr.sort()
    indices = []
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)
    return len(indices), indices


if __name__ == '__main__':
    size = int(input("Введите размер массива: "))
    key = int(input("Введите ключ поиска: "))
    arr = generate_random_array(size)
    arr.sort()
    print("Отсортированный массив: ", arr)
    index = binary_search(arr, 0, len(arr), key)
    if not index == -1:
        count, indices = find_matches(arr, key)
        print(f"Количество совпадений: {count}")
        print(f"Индексы совпадений: {indices}")
    else:
        print("Совпадений с текущим ключом не найдено.")
