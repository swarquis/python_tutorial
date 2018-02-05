from socket import *
from multiprocessing import Process

def client():
	pass

def main():
	s = socket(AF_INET,SOCK_STREAM)
	addr = ("192.168.1.7",8080)
	conn = s.connect(addr)
	for i in range(10):
		s.send(str(i).encode('utf-8'))

if __name__ == "__main__":
	main()

