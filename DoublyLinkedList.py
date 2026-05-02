class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp   # return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp   # return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp   # return temp.value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp   # return temp.value

    def is_palindrome(self):
        if self.length <= 1:
            return True
        front_node = self.head
        back_node = self.tail
        for _ in range(self.length // 2):
            if front_node.value != back_node.value:
                return False
            front_node = front_node.next
            back_node = back_node.prev
        return True

    def reverse(self):
        if self.length < 2:
            return
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def partition_list(self, x):
        if self.head is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next
        prev2.next = None
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        self.head = dummy1.next
        if self.head:
            self.head.prev = None

    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        before = dummy
        for _ in range(start_index):
            before = before.next
        current = before.next
        for _ in range(end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            node_to_move.next = before.next
            node_to_move.prev = before
            before.next.prev = node_to_move
            before.next = node_to_move
        self.head = dummy.next
        self.head.prev = None

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        if self.head:
            self.head.prev = dummy
        prev_node = dummy
        curr = self.head
        while curr and curr.next:
            first = curr
            second = curr.next
            next_pair = second.next
            second.next = first
            first.prev = second
            first.next = next_pair
            if next_pair:
                next_pair.prev = first
            prev_node.next = second
            second.prev = prev_node
            prev_node = first
            curr = next_pair
        self.head = dummy.next
        if self.head:
            self.head.prev = None


