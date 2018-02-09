class Stack(object):
	def __init__(self):
		self.__stack = []

	def __isEmpty(self):
		return len(self.__stack) == 0

	def push(self,data):
		self.__stack.append(data)

	def pop(self):
		if self.__isEmpty():
			exit('no element to be popped')
		return self.__stack.pop()

	def size(self):
		return len(self.__stack)

	def traverse(self):
		for i in self.__stack:
			yield i



if __name__ == "__main__":
	stack = Stack()
	stack.push(11)
	stack.push(22)
	stack.push('aa')
	for i in stack.traverse():
		print(i)

	print(stack.pop())
	
	for i in stack.traverse():
		print(i)
