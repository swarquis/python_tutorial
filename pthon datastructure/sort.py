def bubblesort(a):
	for i in range(0,len(a)):
		for j in range(len(a)-1-i,len(a)-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
	return a

def selectionsort(a):
	for i in range(0,len(a)):
		min = i
		for j in range(i+1,len(a)):
			if a[j] < a[min]:
				min = j
		if min != i:
			a[min],a[i] = a[i],a[min]
	return a



if __name__ == "__main__":
	a = [11,1,20,-4,33]
	#print('bubblesort:'+str(bubblesort(a))) 
	print('selectionsort:'+str(selectionsort(a))) 

