class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
    def printnodes(self):
        curr = self.head
        while curr.next != None:
            print(curr.data, end = " ")
            curr = curr.next
        print(curr.data)

    def insert(self,index,val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            prev_node = None
            curr = self.head
            while count < index and curr is not None:
                prev_node = curr
                curr = curr.next
                count += 1
            prev_node.next = new_node
            new_node.next = curr
    
    def delete(self,index):
        if index == 0:
            prev = self.head
            curr = prev.next
            self.head = curr
            prev.next = None
            prev = None
        else:
            count = 0
            prev = None
            curr = self.head
            while count < index:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next
            curr.next = None
            del curr


            

s1 = sll()

s1.append(20)
s1.append(21)
s1.append(22)
s1.append(23)
s1.append(24)
s1.append(25)
s1.append(26)

s1.printnodes()
print()
s1.insert(3,99)

s1.printnodes()

s1.delete(5)

print()

s1.printnodes()