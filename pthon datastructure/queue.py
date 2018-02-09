class Queue:
	def __init__(self):
		self.__queue = []

	def __isEmpty(self):
		return len(self.__queue) == 0

	def enqueue(self,data):
		self.__queue.append(data)

	def dequeue(self):
		if self.__isEmpty():
			exit('no elements to be retrieved')
		return self.__queue.pop(0)

	def size(self):
		return len(self.__queue)

	def traverse(self):
		if self.__isEmpty():
			exit('no elements to be traversed')
		for i in self.__queue:
			yield i

if __name__ == "__main__":
	queue = Queue()
	queue.enqueue(11)
	queue.enqueue(22)
	queue.enqueue('aa')
	for i in queue.traverse():
		print(i)
	print("\n")
	print(queue.dequeue())
	print(queue.size())