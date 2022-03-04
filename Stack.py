class Node:
    def _init_(self, value):
        self.value = value
        self.next = None


class Stack:
    def _init_(self, value):
        new_node = value
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_stack = Stack(4)

my_stack.print_stack()
