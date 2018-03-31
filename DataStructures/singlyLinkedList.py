class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteFirst(self):
        if self.head == None:
            pass
        else:
            self.head = self.head.next
            
    def deleteLast(self):
        if self.head == None:
            pass
        else:
            node_traverse = self.head
            while node_traverse != None:
                tmp = node_traverse
                node_traverse = node_traverse.next
            tmp.prev.next = None
    
    def addToLast(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node_traverse = self.head
            while node_traverse != None:
                tmp = node_traverse
                node_traverse = node_traverse.next
            tmp.next = node
            node.prev = tmp
            #print(node_traverse.data)
                
    def addToFirst(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :		
            while p.next != None :
                s += p.data
                p = p.next
                s += p.data
        return s

    def traverse(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
    
l = LinkedList()
l.addToLast('a')
l.addToFirst('d')
l.addToLast('c')
#l.add('c')
l.traverse()
print("deleting first element")
l.deleteFirst()
print("deleting last ")
l.deleteLast()
l.traverse()

#print(l)
