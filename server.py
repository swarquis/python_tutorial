from socket import *	
from multiprocessing import Process

#server

s = socket(AF_INET,SOCK_STREAM)
host = ("",8085)
s.bind(host)
s.listen(5)

def main():

	clientInstance,clientAddr = s.accept()

	while True:
		p = Process(target=receive,args=(clientInstance,clientAddr))
		p.start()
		p.close()
	s.close()


def receive(clientInstance, clientAddr):

	while True:
		data = clientInstance.recv(2014)
		data = data.decode('utf-8')
		print(data)
		if len(data) == 0:
			print("%s has disconnected..."%str(clientAddr))
			clientInstance.close()
			break
		else:
			filename = str(data)
			roo_dir = "./root"
			file = roo_dir+"/"+filename

			try:
				f = open(file)
				content = "\r\nHTTP 200 OK \r\n"
				"""while f.readline():
					m += f.readline()+"\r\n"""
				m = f.read()
				content += m+"\r\n"
				#print("%s sent message: %s"%(str(clientInstance),data.decode('utf-8')))
				#print("%s"%content)
				clientInstance.send(content.encode('gbk'))
				clientInstance.close()

			except:
				content = "\r\nHTTP 404 Not Found\r\n"
				content += "Not Found"
				clientInstance.send(content.encode('gbk'))
				clientInstance.close()

	s.close()


if __name__ == "__main__":
	main()
