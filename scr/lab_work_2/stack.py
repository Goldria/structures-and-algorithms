import random


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def __str__(self):
        stack_values = []
        while not self.size == 0:
            stack_values.append(self.pop())
        stack_values = stack_values[::-1]

        for value in stack_values:
            self.push(value)

        return ' '.join([stack_values.__str__(), '<- Вершина стека'])

    def push(self, elem):
        self.data.append(elem)
        self.size += 1

    def pop(self):
        if not self.size == 0:
            self.size -= 1
            return self.data.pop()
        else:
            raise IndexError('Стек пустой.')


def count_average(stack):
    return sum(stack.data)/stack.size


def delete_elements(stack):
    tmp_stack = Stack()
    average = count_average(stack)
    while not stack.size == 0:
        tmp_stack.push(stack.data[stack.size - 1])
        stack.pop()
    while not tmp_stack.size == 0:
        if tmp_stack.data[tmp_stack.size - 1] > average:
            stack.push(tmp_stack.data[tmp_stack.size - 1])
        tmp_stack.pop()
    return stack


def main():
    stack = Stack()
    for _ in range(20):
        stack.push(random.randint(1, 500))
    print('Исходный стек:', stack)
    print('Среднее арифметическое элементов целочисленного стека: ',
          count_average(stack))
    print('Результат преобразования стека:',
          delete_elements(stack))


if __name__ == '__main__':
    main()
