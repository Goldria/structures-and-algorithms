import random

import graphviz


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def search(self, key):
        if not self.root:
            return False
        else:
            return self._search(key, self.root)

    def _search(self, key, node):
        if key == node.key:
            return True
        elif key < node.key and node.left is not None:
            return self._search(key, node.left)
        elif key > node.key and node.right is not None:
            return self._search(key, node.right)
        return False

    def delete(self, key):
        if self.root is None:
            return self.root
        else:
            self.root = self._delete(key, self.root)
        return self.root

    def _delete(self, key, node):
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None and node.right is None:
                del node
                node = None
            elif node.left is None:
                temp = node.right
                del node
                node = temp
            elif node.right is None:
                temp = node.left
                del node
                node = temp
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = self._delete(temp.key, node.right)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        dot = graphviz.Digraph()
        self._display(self.root, dot)
        return dot

    def _display(self, node, dot):
        if node is None:
            return
        else:
            dot.node(str(node.key))
            if node.left is not None:
                dot.edge(str(node.key), str(node.left.key))
            if node.right is not None:
                dot.edge(str(node.key), str(node.right.key))
            self._display(node.left, dot)
            self._display(node.right, dot)


def contain_number(tree, number):
    if tree.search(number):
        print('Число', number, 'содержится в дереве.')
    else:
        print('Число', number, 'не содержится в дереве.')


def main():
    tree = BST()
    arr = [random.randint(1, 100) for _ in range(100)]
    for i in range(len(arr)):
        tree.insert(arr[i])
    print('Элементы, по которым будет построено дерево:', arr)

    tree.display().render('tree.gv', view=True)

    number = int(input('Введите число, которое хотите найти в дереве: '))
    contain_number(tree, number)

    number = int(input('Введите число, которое хотите удалить в дереве: '))
    tree.delete(number)
    tree.display().render('new_tree.gv', view=True)


if __name__ == '__main__':
    main()
