import random


class MySet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            used_elements = []
            unique = []
            for _, elem in enumerate(iterable):
                if elem not in used_elements:
                    unique.append(elem)
                    used_elements.append(elem)
            self.data = unique

    def add(self, element):
        if element not in self.data:
            self.data.append(element)

    def intersection(self, other_set):
        result = MySet()
        for elem in self.data:
            if elem in other_set.data:
                result.add(elem)
        return result

    def difference(self, other_set):
        result = MySet()
        for elem in self.data:
            if elem not in other_set.data:
                result.add(elem)
        return result

    def union(self, other_set):
        result = self.copy()
        for elem in other_set.data:
            result.add(elem)
        return result

    def copy(self):
        return MySet(self.data.copy())

    def __str__(self):
        return self.data.__str__()


def find_available_toys(kindergartens):
    kg_sets = [MySet(kg) for kg in kindergartens[1:]]
    for kg in kg_sets[1:]:
        kg_sets[0] = kg_sets[0].intersection(kg)
    return kg_sets[0]


def find_missing_toys(kindergartens, toys):
    kg_sets = [MySet(kg) for kg in kindergartens[1:]]
    miss_toys = MySet(toys.copy())
    for toy in kg_sets:
        miss_toys = miss_toys.difference(toy)
    return miss_toys


def hand_out_toys_random(toys, n):
    kindergartens = []
    kindergartens.append([])
    for _ in range(n):
        kg = []
        for _ in range(random.randint(1, len(toys) - 1)):
            kg.append(toys[random.randint(0, len(toys) - 1)])
        kindergartens.append(kg)
    return kindergartens


def main():
    n = 5
    toys = ['Погремушка', 'Пирамидка', 'Сортер',
            'Пазл', 'Кубик', 'Конструктор', 'Мозаика',
            'Лото', 'Кольцеброс', 'Боулинг', 'Крокет']
    kindergartens = hand_out_toys_random(toys, n)
    print('Детские сады и имеющиесы в нём игрушки:')
    for i in range(1, len(kindergartens)):
        print('Десткий сад ', i, ': ', kindergartens[i])
    nothing = find_missing_toys(kindergartens, toys)
    print('Игрушки, которых нет ни в однои дет.садике:', nothing)
    intersection = find_available_toys(kindergartens)
    print('Игрушки, которые есть в каждом дет.садике:', intersection)


if __name__ == '__main__':
    main()
