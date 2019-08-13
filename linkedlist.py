class Node():
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.next_node = nextNode

    def get_data(self):
        print(self.data)

    def get_next_node(self):
        print(self.next_node)

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList():

    def __init__(self):
        self.head = Node()

    def insert_node(self, node):
        ll_data = self.head
        while ll_data is not None:
            if ll_data is None:
                ll_data = Node()
                ll_data.data = node
                ll_data.next_node = None
            ll_data = ll_data.next_node


ll = LinkedList()
ll.insert_node("Mon")
ll.insert_node("Tue")
ll.insert_node("Wed")
# n1 = Node('1')
# n2 = Node('2')
# n3 = Node('3')

# n1.next_node = n2
# n2.next_node = n3
# ll.head = n1

print("")
print("")


