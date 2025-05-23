from linked_list import LinkedList

def dedupe(linked_list):
    seen = set()
    temp = linked_list.head
    while temp != None:
        seen.add(temp.value)
        #not O(n^2) as it continues its parent loop and deletes elements it traverses for the parent loop
        while temp.next != None and temp.next.value in seen:
            temp.next = temp.next.next
            linked_list.length -=1
        temp = temp.next
    return linked_list

def setless_dedupe(linked_list):
    outer = linked_list.head
    while outer != None:
        inner = outer
        while inner != None:
            #not O(n^3) as it continues its parent loop and deletes elements it traverses for the parent loop
            while inner.next != None and inner.next.value==outer.value:
                inner.next = inner.next.next
                linked_list.length -=1
            inner = inner.next
        outer = outer.next
    return linked_list


x = LinkedList(1)
y = LinkedList(1)
for i in range(2,5):
    x.append(3)
    y.append(3)
x.append(4)
y.append(4)


print(dedupe(x))
print(x)
print(setless_dedupe(y))
print(y)
