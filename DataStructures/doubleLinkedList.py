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
            while node_traverse.next != None:
				print(node_traverse.data)
				node_traverse = node_traverse.next
                
	def addToFirst(self,data):
		node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

	def insertAt(self,data,position):
		node = Node(data)
		if self.head == None:
			self.head = node
		else: 
			if position == 1:
				addToFirst(data)
			else:
				node_traverse = self.head
				for i in range(1,position):
					node_traverse = node_traverse.next
				print(node_traverse.data)
	
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
l.addToLast('c')
l.traverse()