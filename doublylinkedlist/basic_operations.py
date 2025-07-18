class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class doublyll:
    def __init__(self):
        self.head = None
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def print_nodes(self):
        if self.head is None:
            print("No Nodes Present")
        else:
            temp = self.head
            while temp:
                print(temp.val)
                temp = temp.next
    def insert_at_last(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
    def delete_head(self):
        temp = self.head.next
        self.head.next = None
        temp.prev = self.head.prev 
        self.head = temp
    def delete_node(self,index):
        if self.head is None:
            print("List is empty")
        if index == 0:
            self.delete_head()
        else:
            temp = self.head
            count = 0
            while count != index:
                temp = temp.next
                count += 1
            prev = temp.prev
            prev.next = temp.next
            del temp
    def insert_at_position(self,index,val):
        new_node = Node(val)
        if self.head is None and index != 0:
            print("List is empty, position invalid")
        elif index == 0:
            self.insert_at_head(val)
        else:
            temp = self.head
            count = 0
            while count != index:
                temp = temp.next
                count += 1
            back_node = temp.prev
            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev = new_node
            back_node.next = new_node
            


dll = doublyll()
dll.insert_at_head(20)
dll.insert_at_last(21)
dll.insert_at_last(22)
dll.insert_at_last(23)
dll.insert_at_last(24)
dll.insert_at_last(25)
dll.delete_node(0)
dll.insert_at_position(0,99)
dll.print_nodes()

