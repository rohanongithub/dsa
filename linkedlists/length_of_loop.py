class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(21)
n2 = Node(22)
n3 = Node(23)
n4 = Node(24)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

# n1 -> n2 -> n3 -> n4 -> n2

head = n1

slow = head
fast = head
count = 1
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        fast = fast.next
        while fast != slow:
            fast = fast.next
            count += 1
        print("Len of loop", count)
        break
if count == 1:
    print("No loop found")