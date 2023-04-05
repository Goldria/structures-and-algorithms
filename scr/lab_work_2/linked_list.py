import datetime


class Notebook:
    def __init__(self, course, last_name, date, number,
                 code=None,  discipline=None, grade=None):
        self.course = course
        self.code = code
        self.last_name = last_name
        self.date = date
        self.number = number
        self.discipline = discipline
        self.grade = grade

    def __str__(self):
        return f'Фамилия студента: {self.last_name}, \n' \
               f'Курс: {self.course}, \n' \
               f'Номер зачётной книжки: {self.number}, \n' \
               f'Дата поступления: {self.date}.\n -----\n'


class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_node = self.head
        result = f''
        while True:
            result += f'{cur_node.data}'
            cur_node = cur_node.next
            if not cur_node:
                break
        return result

    def add(self, element):
        new_node = Node(element)
        node = self.head
        if self.head is None:
            self.head = new_node
            return
        while node.next:
            node = node.next
        node.next = new_node

    def extend(self, iterable):
        for element in iterable:
            self.add(element)

    def search(self, **elem):
        cur_node = self.head
        while cur_node:
            if self.is_equal(cur_node.data, **elem):
                return cur_node.data
            cur_node = cur_node.next

    def is_equal(self, node_data, **properties):
        for property_name, property_value in properties.items():
            if getattr(node_data, property_name) != property_value:
                return False
        return True

    def sort(self, elem=None):
        isNotSorted = True
        while isNotSorted:
            isNotSorted = False
            tmp = self.head
            while tmp is not None:
                if tmp.next is not None:
                    if elem is not None:
                        if getattr(tmp.data, elem) > getattr(tmp.next.data, elem):
                            tmp.data, tmp.next.data = tmp.next.data, tmp.data
                            isNotSorted = True
                    else:
                        if tmp.data > tmp.next.data:
                            tmp.data, tmp.next.data = tmp.next.data, tmp.data
                            isNotSorted = True
                tmp = tmp.next


def main():
    notebook1 = Notebook(last_name='Newton', course=2, number=123, code=65, discipline='Информатика',
                         date=datetime.datetime.strptime('24052020', "%d%m%Y").date(), grade=5)
    notebook2 = Notebook(last_name='Galilei', course=5, number=411, code=65, discipline='Экология',
                         date=datetime.datetime.strptime('24062015', "%d%m%Y").date(), grade=4)
    notebook3 = Notebook(last_name='Euler', course=3, number=246, code=12, discipline='История',
                         date=datetime.datetime.strptime('25082011', "%d%m%Y").date(), grade=5)
    notebook4 = Notebook(last_name='Lipton', course=1, number=132, code=49, discipline='Физика',
                         date=datetime.datetime.strptime('25052010', "%d%m%Y").date(), grade=3)
    notebook5 = Notebook(last_name='Mask', course=2, number=523, code=65, discipline='Математика',
                         date=datetime.datetime.strptime('24012020', "%d%m%Y").date(), grade=5)
    notebooks = [notebook1, notebook2, notebook3, notebook4, notebook5]

    linked_list = LinkedList()
    linked_list.extend(notebooks)
    print('Исходный журнал с пятью студентами:\n---------')
    print(linked_list)
    sorted = 'course'
    linked_list.sort(sorted)
    print('Журнал после сортировки по полю', sorted, ': \n---------')
    print(linked_list)
    print('Студент с номером зачётной книжки 523: \n---------')
    print(linked_list.search(number=523))


if __name__ == '__main__':
    main()
