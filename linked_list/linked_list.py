from node import Node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        temp = self.head
        string = ""
        while temp != None:
            string += (str(temp.value) + ' ')
            temp = temp.next
        return string.strip()

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
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp
        
    def get(self, index):
        if index >= self.length or index < 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0 :
            return False
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index - 1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            self.print_list

        return True
    
    def remove(self, index):
        if index >= self.length or index < 0 :
            return False
        elif index == self.length-1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            self.length -= 1
            temp.next = None
            return temp
    
    # def reverse(self):
    # O(n) time & space
    #     if self.length > 1:
    #         stack = []
    #         temp = self.head
    #         while temp != None:
    #             stack.append(temp)
    #             temp = temp.next
    #         self.head = stack.pop()
    #         temp = self.head
    #         while stack != []:
    #             temp.next = stack.pop()
    #             temp = temp.next
    #         temp.next = None
    #         self.tail = temp
    #     return self

    def reverse(self):
    # O(n) time, O(1) space
        if self.length > 1:
            temp = self.head
            prev = None
            next = temp.next

            self.head = self.tail
            self.tail = temp

            while temp!=None:
                temp.next = prev
                prev = temp
                temp = next
                if next:
                    next = next.next
            # self.tail.next = None
        return self
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
print(my_linked_list)
print(my_linked_list.reverse())
