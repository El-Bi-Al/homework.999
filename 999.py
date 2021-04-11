class Node:
    element = None
    next_node = None
    prev_node = None


class LinkedList:
    head = None

    def __init__(self, prev_node, element, next_node=None ):
        self.element = element
        self.next_node = next_node
        self.prev_node = prev_node

    def append(self, element):
        if not self.head:
            self.head = self.node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.prev_node = self.next_node
        node.next_node = self.node(element)

    def insert(self, element , index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i+=1
        prev_node.next_node = self.node(element, next_node=node)
        return element
    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i+=1

        return node.element
    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node
        #node.prev_node = node.next_node

        while i <index:
            prev_node = node
            node = node.next_node
            i+=1
        prev_node.node = node.next_node
        element = node.element
        del node
        return element

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

linked_list = LinkedList(element=None,prev_node=None, next_node=None)
linked_list.append(10)
linked_list.append(143)
linked_list.append(132)
linked_list.append(257)
linked_list.append(1)
linked_list.insert(14,1)
linked_list.delete(2)
linked_list.out()
print(" ")
print(linked_list.get(0))
