from linked_list import LinkedList

def find_mid(linked_list):
    fast = linked_list.head
    slow = linked_list.head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow


x = LinkedList(1)
for y in range(2,5):
    x.append(y)
print(x)
print(find_mid(x).value)
        