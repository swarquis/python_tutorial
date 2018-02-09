
#define a node with data and addr pointer
class Node(object):
	#init
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(object):
	#init a head pointer and number of elements to be 0
	def __init__(self):
		self.__head = None
		self.__count = 0

	def isEmpty(self):
		'''check whether there are any nodes'''
		return self.__count == 0

	def add(self,data):
		'''add node before head'''
		node = Node(data)
		if self.isEmpty():
			self.__head = node
			node.next = None
		else:
			tmp = self.__head
			self.__head = node
			node.next = tmp
		self.__count += 1

	def append(self, data):
		'''append node after last'''
		node = Node(data)
		if self.isEmpty():
			self.__head = node
		else:
			tmp = self.__head
			while tmp.next != None:
				tmp = tmp.next
			#get the last node
			tmp.next = node
			node.next = None
		self.__count += 1

	def insert(self, pos, data):
		'''insert node at pos, move nodes to the rear,offset is -1'''
		node = Node(data)
		if pos-1 <= 0:
			tmp = self.__head
			self.__head = node
			node.next = tmp
		elif pos-1 > self.__count:
			tmp = self.__head
			while tmp.next != None:
				tmp = tmp.next
			tmp.next = node
			node.next = None
		else:
			tmp = self.__head
			count = 0
			while tmp != None:
				if count == pos -2:
					node.next = tmp.next
					tmp.next = node
					break
				tmp = tmp.next
				count += 1
		self.__count += 1

	def addafter(self,pos,data):
		node = Node(data)
		if pos-1 < 0:
			tmp = self.__head
			self.__head = node
			node.next = tmp
		elif pos > self.__count:
			tmp = self.__head
			while tmp.next != None:
				tmp = tmp.next
			tmp.next = node
			node.next = None
		else:
			tmp = self.__head
			count = 1
			while tmp != None:
				if count == pos:
					cur = tmp.next
					tmp.next = node
					node.next = cur
				count += 1
		self.__count += 1

	def traverse(self):
		'''traverse the list'''
		if self.isEmpty():
			print("no element to be traversed.")
			exit()
		else:
			tmp = self.__head
			while(tmp != None):
				print(tmp.data,end = " ")
				tmp = tmp.next
			print("\n")





if __name__ == "__main__":
	list = LinkedList()
	print(list.isEmpty())
	list.add(11)
	list.add('aa')
	list.add('bb')
	list.append('a')
	list.append('b')
	list.append('c')
	list.insert(1,'ccc')
	list.insert(2,'ccc')
	list.traverse()