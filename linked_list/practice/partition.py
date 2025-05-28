from linked_list import LinkedList
from node import Node

def partition(linked_list, value):

    temp = linked_list.head
    dummy1 = Node(0)
    dummy2 = Node(0)
    prev1 = dummy1
    prev2 = dummy2

    while temp != None:
        print(temp.value, value)
        if temp.value < value:
            prev1.next = Node(temp.value)
            prev1 = prev1.next
        else:
            prev2.next = Node(temp.value)
            prev2 = prev2.next
        temp = temp.next
    prev2.next = None
    prev1.next = dummy2.next
    linked_list.head = dummy1.next
    return linked_list



x = LinkedList(10)
for y in range(9,0,-1):
    x.append(y)
print(x)

list1=partition(x,4)
print(list1)

