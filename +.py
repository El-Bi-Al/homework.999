class LinkedList(object):
    head = None  # Nachalo spiska

    class Node:  # Node - uzel

        element = None
        next_node = None

        def __init__(self, head=None):
            self.head = head

        def search(self, data):
            current = self.head
            found = False
            while current and found is False:
                if current.get_data() == data:
                    found = True
                else:
                    current = current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            return current

LinkedList.append(135)
LinkedList.append(234)
LinkedList.append(232)
LinkedList.append(1)
LinkedList.search(3)