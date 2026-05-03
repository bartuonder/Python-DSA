class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty() is True:
            return None
        return self.stack_list.pop()


def reverse_string(string_example):
    my_stack = Stack()
    for char in string_example:
        my_stack.push(char)
    reversed_str = ""
    while not my_stack.is_empty():
        reversed_str += my_stack.pop()
    return reversed_str


def is_balanced_parentheses(parentheses):
    my_stack = Stack()
    for p in parentheses:
        if p == "(":
            my_stack.push(p)
        elif p == ")":
            if my_stack.is_empty():
                return False
            my_stack.pop()
    return my_stack.is_empty()


def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())