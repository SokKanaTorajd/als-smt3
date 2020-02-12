class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items==[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)

def revString(mystr):
	s = Stack()
	for i in range(0,len(mystr)):
		s.push(mystr[i])
	result = ""
	while not s.isEmpty():
		result += s.pop()
	return result

def testEqual(string1,string2):
	if string1 == string2:
		print("string bernilai sama")
	else:
		print("string tidak sama")

testEqual(revString('apple'),'elppa')
testEqual(revString('x'),'x')
testEqual(revString('1234567890'),'0987654321')