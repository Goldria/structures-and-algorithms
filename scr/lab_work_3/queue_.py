import random


class Queue:
    def __init__(self, max_size=100):
        self.data = []
        self.size = 0
        self.max_size = max_size

    def push(self, elem):
        if not self.size >= self.max_size:
            self.size += 1
            self.data.append(elem)
        else:
            raise IndexError('Очередь переполнена.')

    def pop(self):
        if not self.size == 0:
            self.size -= 1
            return self.data.pop(0)
        else:
            raise IndexError('Очередь пуста.')

    def __str__(self):
        queue_values = []
        while not self.size == 0:
            queue_values.append(self.pop())

        for value in queue_values:
            self.push(value)

        return queue_values.__str__()


def put_first_in_last(queue1, queue2):
    queue1.push(queue2.data[0])
    queue2.pop()


def swap(queue):
    tmp_queue = Queue()
    size = queue.size
    min_ = 2 ** 32
    while not size == 0:
        min_ = min(min_, queue.data[0])
        put_first_in_last(queue, queue)
        size -= 1
    if not queue.data[0] == min_:
        while not queue.data[0] == min_:
            put_first_in_last(tmp_queue, queue)
        tmp_queue.push(queue.data[0] - 10)
        queue.pop()
        min_ -= 10
        put_first_in_last(queue, tmp_queue)
        size = queue.size - 1
        while not size == 0:
            put_first_in_last(queue, queue)
            size -= 1
        while not tmp_queue.data[0] == min_:
            put_first_in_last(tmp_queue, tmp_queue)
        while not tmp_queue.size == 0:
            queue.push(tmp_queue.data[0])
            tmp_queue.pop()
        while not queue.data[0] == min_:
            put_first_in_last(queue, queue)
        queue.push(queue.data[0] + 10)
        queue.pop()
        for _ in range(queue.size - 1):
            put_first_in_last(queue, queue)


def main():
    queue = Queue()
    for _ in range(50):
        queue.push(random.randint(1, 100))
    print('Исходная очередь: ', queue)
    swap(queue)
    print('Очередь после изменений: ', queue)


if __name__ == '__main__':
    main()
