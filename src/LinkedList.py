from src.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insert_array(self, arr):
        for item in arr:
            self.insert_at_end(item)

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return "The list is empty"
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return "The list is empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

