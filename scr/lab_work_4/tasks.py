from hash_table import *


def build_table_from_file(file_name, size):
    table = HashTable(size)
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                table.add(word)
    return table


def search_word(table, word):
    count = 0
    value = table.get(word)
    if value != 0:
        count = 1
    return value, count


def remove_words_starting_with(table, letter):
    for i in range(table.size):
        table.table[i] = [(k, v) for k, v in table.table[i]
                          if not k.startswith(letter)]


def first_task():
    string = input('Введите строку: ')
    table = HashTable(100)

    for char in string:
        table.add(char)

    print('Хэш-таблица:')
    table.print_table()

    char = input('Введите слово для поиска: "\'')
    count, _ = search_word(table, char)
    print(f'Буква (символ) {char} встречается {count} раз.')


def second_task():
    file_name = 'text.txt'
    size = int(input('Введите размер таблицы: '))
    table = build_table_from_file(file_name, size)

    table.print_table()

    word = input('Введите слово для поиска: "\'')
    count, comparisons = search_word(table, word)
    print(
        f'Слово {word} встречается {count} раз (количество сравнений: {comparisons})')

    letter = input('Введите букву для удаления слов: ')
    remove_words_starting_with(table, letter)
    print('Таблица после удаления слов:')
    table.print_table()


def third_task():
    file_name = 'int.txt'
    table = build_table_from_file(file_name, 1000)

    table.print_table()

    integer = input('Введите число для поиска: "\'')
    count, _ = search_word(table, integer)
    print(f'Число {integer} встречается {count} раз.')


def main(number_task=None):
    if number_task == 1:
        first_task()
    if number_task == 2:
        second_task()
    if number_task == 3:
        third_task()
    if number_task == None:
        print('Задайте номер задания.')


if __name__ == '__main__':
    main(3)
