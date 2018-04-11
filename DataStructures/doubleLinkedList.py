class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
	
class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def add(self,data):
		self.size = self.size + 1
		if self.head == None:
			self.head = Node(data)
		else:
			node = Node(data)
			node.next = self.head
			self.head = node
			self.head.next.prev  = self.head
			
	def printLL(self):
		if self.head == None:
			print("linkedlist is empty")
		else:
			node = self.head
			while(node != None):
				print(node.data)
				node = node.next
	
	def addToLast(self,data):
		self.size = self.size + 1
		if self.head == None:
			self.head = Node(data)
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = Node(data)
			node.next.prev = node
	
	def deleteFirst(self):
		if self.head == None:
			print("LinkedList empty cannot delete any node")
		else:
			self.head = self.head.next
			self.size = self.size - 1
			
	def deleteLast(self):
		if self.head == None:
			print("LinkedList empty cannot delete any node")
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			node.prev.next = None
			self.size = self.size - 1
	
	def insertAt(self,data,position):
		if self.head == None:
			self.head = Node(data)
		if self.size < position:
			print("cannot add to the linkedlist because given position is greater than size of the linkedlist")
		else:
			self.size = self.size + 1
			node = self.head
			for i in range(1,position-1,1):
				node = node.next
			data = Node(data)
			a = node
			b = a.next
			a.next = data
			data.prev = a
			data.next = b
			b.prev = data

	def deleteAt(self,position):
		if self.head == None:
			print("No more nodes on the linkedlist to delete")
		if self.size < position:
			print("cannot delete the node on linkedlist because given position is greater than the size of the linkedlist")
		else:	
			if position == 1:
				self.head = self.head.next
			else:
				self.size = self.size - 1
				node = self.head
				for i in range(1,position):
					node = node.next
				node.prev.next = node.next
			
	def reverse(self):
		L1 = LinkedList()
		node = self.head
		while(node):
			L1.add(node.data)
			node = node.next
		return L1
			
l = LinkedList()
l.add(1)
l.add(2)
l.addToLast(3)
l.addToLast(4)
l.printLL()
print("\n")
l.deleteFirst()
l.printLL()
print("\n")
l.deleteLast()
l.printLL()
print("\n")
print(l.size)
l.insertAt(5,2)
print("\n")
l.printLL()
l.deleteAt(3)
l.add(6)
l.add(0)
print("\n")
l.printLL()
print("\n")
l = l.reverse()
l.printLL()