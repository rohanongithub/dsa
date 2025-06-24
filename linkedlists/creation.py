class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr is not None:
                curr = curr.next
            curr.next = new_node
            

node1 = Node(10)
node2 = Node(21)
node3 = Node(31)
node4 = Node(41)

node1.next = node2
node2.next = node3
node3.next = node4