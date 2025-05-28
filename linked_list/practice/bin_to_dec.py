from linked_list import LinkedList

def binary_to_decimal(linked_list):
    current = linked_list.head
    value = 0

    while current != None:
        value = value*2 + current.value 
        current = current.next
    return value

x = LinkedList(1)
for _ in range(3):
    x.append(0)
print(x)
print(binary_to_decimal(x))

x = LinkedList(1)
x.pop()
print(binary_to_decimal(x))
        


        