from linked_list import LinkedList

def kth_from_end(linked_list, index):
    fast = linked_list.head
    solution = linked_list.head

    for _ in range(index):
        if fast:
            fast = fast.next
        else:
            return None
        
    while fast != None:
        fast = fast.next
        solution = solution.next
    return solution

x = LinkedList(1)
for y in range(2,5):
    x.append(y)

print(kth_from_end(x,1).value) #4
print(kth_from_end(x,3).value) #2

