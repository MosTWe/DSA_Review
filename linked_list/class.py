class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            while temp.next != None:
                pre = temp
                temp=temp.next
            self.tail = pre.next
            pre.next = None
            self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        self.head = new_node
        self.length += 1
        return True
        
    #     return

    # def prepend(self, value):
    #     return
    
    # def insert(self, index, value):
    #     return
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
