class stack:
	def __init__(self):
		self.s = []
	
	def push(self,data):
		self.s.append(data)
	
	def pop(self):
		self.s.pop()
	
	def isEmpty(self):
		if self.s:
			return False
		return True
	def print_stack(self):
		print(self.s)
		
	def peek(self):
		print(self.s[len(self.s)-1])
		
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.print_stack()
print(s.isEmpty())
s.peek()