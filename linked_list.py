class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node('Head')

    def add(self, value=None):
        newNode = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def showLinkedList(self):
        cur = self.head
        while True:
            print(f'{cur.value} ')
            if(cur.next == None):
                break
            cur = cur.next
        

myLinkedList = LinkedList()
listValues = [1, 2, 3, 4, 5]

for index in range(len(listValues)):
    value = listValues.pop(0)
    myLinkedList.add(value)

myLinkedList.showLinkedList()



# Create a linked list for values -> 1, 2, 3, 4, 5