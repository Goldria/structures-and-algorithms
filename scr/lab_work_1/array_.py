import numpy as np


def harmonic(array):
    denominator, count, result = 0, 0, 0
    for i in range(len(array)):
        if array[i] % 2 != 0:
            denominator += (1 / array[i])
            count += 1
    if denominator != 0:
        result = count / denominator

    return result


def count_elements(array):
    count = 0
    harmonic_ = harmonic(array)
    for i in range(len(array)):
        if array[i] > harmonic_:
            count += 1

    return count


def main():
    N = 20
    x = 1
    array_ = np.array([])
    for _ in range(N):
        x += 1
        array_ = np.append(array_, x)
    result = count_elements(array_)
    print("Исходный массив:", array_,
          "\nКоличество элементов массива больше среднего",
          "гармонического нечетных элементов массива:", result)


if __name__ == "__main__":
    main()
