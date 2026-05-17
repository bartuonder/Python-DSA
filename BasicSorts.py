# Basic Sorts for Lists

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list



# Basic Sorts for Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.length < 2:
            return
        for i in range(self.length - 1, 0, -1):
            current = self.head
            for j in range(i):
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next

    def selection_sort(self):
        if self.head is None or self.head.next is None:
            return
        current = self.head
        while current is not None:
            min_node = current
            inner = current.next
            while inner is not None:
                if inner.value < min_node.value:
                    min_node = inner
                inner = inner.next
            if min_node != current:
                current.value, min_node.value = min_node.value, current.value
            current = current.next

    def insertion_sort(self):
        if self.length < 2:
            return
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp