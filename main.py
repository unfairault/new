class Node:
    def __init__(self, value, left=None, right=None):
        self.left_link = left
        self.right_link = right
        self.value = value


class Deque:
    def __init__(self, size):
        self.left_pointer = None
        self.right_pointer = None
        self.size = size

    def add_right(self, value):
        if not self.size:
            return 'error'

        new_node = Node(value)
        if self.right_pointer:
            self.right_pointer.right_link = new_node
            new_node.left_link = self.right_pointer
            self.right_pointer = new_node
        else:
            self.right_pointer = self.left_pointer = new_node

        self.size -= 1

    '''def print_right_to_left(self):
        print('<-- start')
        node = self.right_pointer
        while node != None:
            print(node.value)
            node = node.left_link
        print('<-- end')

    def print_left_to_right(self):
        print('start -->')
        node = self.left_pointer
        while node != None:
            print(node.value)
            node = node.right_link
        print('end -->')'''

    def add_left(self, value):
        if not self.size:
            return 'error'

        new_node = Node(value)
        if self.left_pointer:
            self.left_pointer.left_link = new_node
            new_node.right_link = self.left_pointer
            self.left_pointer = new_node
        else:
            self.right_pointer = self.left_pointer = new_node

        self.size -= 1

    def remove_left(self):
        # Удалить последний элемент
        if self.left_pointer and not self.left_pointer.right_link:
            value = self.left_pointer.value
            self.right_pointer = self.left_pointer = None
            self.size += 1
            return value

        # Удалить НЕ последний элемент
        if self.left_pointer:
            value = self.left_pointer.value
            new_end_node = self.left_pointer.right_link
            new_end_node.left_link = None
            self.left_pointer = new_end_node
            self.size += 1
            return value
        # Удалять нечего
        else:
            return 'error'

    def remove_right(self):
        if self.right_pointer and not self.right_pointer.left_link:
            value = self.right_pointer.value
            self.left_pointer = self.right_pointer = None
            self.size += 1
            return value

        if self.right_pointer:
            value = self.right_pointer.value
            new_end_node = self.right_pointer.left_link
            new_end_node.right_link = None
            self.right_pointer = new_end_node
            self.size += 1
            return value
        # Удалять нечего
        else:
            return 'error'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    command_count = int(input())
    size = int(input())
    d = Deque(size)

    for i in range(command_count):
        x = input()
        x = x.split(' ')
        if x[0] == 'push_front':
            result = d.add_right(x[1])
            if result:
                print(result)
        if x[0] == 'push_back':
            result = d.add_left(x[1])
            if result:
                print(result)
        if x[0] == 'pop_back':
            result = d.remove_left()
            if result:
                print(result)
        if x[0] == 'pop_front':
            result = d.remove_right()
            if result:
                print(result)







