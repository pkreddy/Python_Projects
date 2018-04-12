#FILO
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class stack:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def push(self,data):
		if self.head == None:
			self.head = Node(data)
			self.size = self.size + 1
		else:
			node = self.head
			self.size = self.size + 1
			while(node.next):
				node = node.next
			node.next = Node(data)
	
	def pop(self):
		if self.head == None:
			print("stack is empty cannot pop any more")
		else:
			node = self.head
			for i in range(1,self.size-1):
				node = node.next
			node.next = None
			
	def print_stack(self):
		node = self.head
		while(node):
			print(node.data)
			node = node.next
		
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
print("\n")
s.pop()
s.print_stack()