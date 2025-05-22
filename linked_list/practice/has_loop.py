from linked_list import LinkedList

def has_loop(linked_list):
    fast = linked_list.head
    slow = linked_list.head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


x = LinkedList(1)
for y in range(2,5):
    x.append(y)
print(x)
print("No loop: ", has_loop(x))
x.tail.next = x.head
print("Loop: ", has_loop(x))

        