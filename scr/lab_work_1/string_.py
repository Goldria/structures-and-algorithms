def find_spaces(text):
    numbers = []
    length = len(text) - 1
    for i in range(length, -1, -1):
        if text[i] == ".":
            j = i - 1
            while text[j] == " ":
                if j not in numbers:
                    numbers.append(j)
                j -= 1
    return numbers


def delete_spaces(text):
    count = len(text) - 1
    numbers = find_spaces(text)
    while numbers:
        if count in numbers:
            text = text[:count] + text[count + 1:]
            numbers.remove(count)
        count -= 1

    return text


def main():
    print("Исходный текст: ", end="")
    text = "Меня зовут Даша    . Мне 19 лет   . Приятно познакомиться           . Сколько Вам лет?"
    print(text)
    result = delete_spaces(text)
    print("Исправленный текст:", result)


if __name__ == "__main__":
    main()
