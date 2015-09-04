#github username: ahal1779
#github email:ahal1779@colorado.edu
#Ahmed M Alismail

import Queue
class myQueue():
	def __init__(this):
		this.q = Queue.Queue()#create new Q
	def putq(this,value):
		this.q.put(value)#add using the put function
	def popq(this):
		while not this.q.empty():# if the queue is not empty print the next value
			print this.q.get()
#Stack
class Stack1():

	def __init__(this):
		this.stack1=[]
	
	def push(this,i):
		return this.stack1.append(i)#add a new value to the list stack1
	
	def pop(this):
		return this.stack1.pop()#pop all values in the list

	def checkSize(this):
		return len(this.stack1)#return the length of the list stack1
		


class Node():
	
	def __init__(this,key): #initiate a new node with the given key but no others
		this.key=key     
		this.right=None
		this.left=None
		this.parent=None
		
	def getrightchild(this):
		return this.right# return the right child
		
	def getleftchild(this):
		return this.left# return the left child
		
	def getparent(this):
		return this.parent#return the parent of this specific node
	def getkey(this):
		return this.key# return the key value of this node

class BinaryTree():
	
	def __init__(this,key):
		this.root= Node(key)# intiate the new tree root
		this.current=this.root# make the current node we are in equal to the root node
		this.deleted=0# indication if the delete function was successful
		this.added=0# indication if the add function was successful
		
	def add(this,value,parentValue):
		if this.current.getkey()==parentValue:# is this the parent child
			if this.current.left==None:# if it has no lef child, add the new node in the left space
				this.current.left=Node(value)
				this.current.left.parent=this.current
				this.added=1# addition was successful
				return
			elif this.current.right==None: # if it has a left child but no right child, add the child in the right place
				this.current.right=Node(value)
				this.current.right.parent=this.current
				this.added=1#addition was succesfull
				return
			elif this.current.left!=None and this.current.right!=None:
				print "Parent has two children, node not added"# if the two spaces are taken, then it has two children
				return
		# if we didn't find it, go left always
		if this.current.left:# if it has a left child, go left
			this.current=this.current.left#change the node we are working on
			this.add(value,parentValue)# go left
		# if we are done with all left childs, then start going back and checking right childs
		if this.current.right:# if we have a right child, go right
			this.current=this.current.right# change the node we are working on to right nde
			this.add(value,parentValue)# go right 
			
		if this.current==this.root:# if we are back to the root
			if this.added==0:# and we couldn't find the parent node
				print "Node not found"
			else:
				this.added=0# return to defualt state.
					
		if this.current.parent:# go back to the parent of the node to keep searching
			this.current=this.current.parent
			if this.current==this.root:
				this.added=0# return to defualt state
			return
		
	def printT(this):
		if this.current:# if the node we are in is valid
			print(this.current.getkey())#print the value of this node
			if this.current.left:# go left all the way to the end printing these values
				this.current=this.current.left
				this.printT()
			if this.current.right:# after finishing left side, check every right side of the node
				this.current=this.current.right
				this.printT()
			if this.current.parent: #if we reached the bottom, then start going back step by step
				this.current=this.current.parent
				return
				
	def delete(this,value):
		if this.current.getkey()==value:#did we find the matching key value
			if this.current.left!=None or this.current.right!=None:#check if it has children, if so, it cannot be deleted
				print "Node not deleted, has children"
				return
			else:#otherwize, delete it and remove it from the parent list
				if this.current.parent.left.getkey()==value:
					this.current.parent.left=None
				else:
					this.current.parent.right=None
				this.current=this.current.parent
				this.deleted=1# delete process was succesfull
				return
		if this.current:# if this node is still available 
			if this.current.left:# go left all the way to find the required value
				this.current=this.current.left
				this.delete(value)
		if this.current:
			if this.current.right:# if we reached the end of the left search, then go right while steping back wards
				this.current=this.current.right
				this.delete(value)
				if this.current==this.root:#if we reached the end and the node is not found print not found
					if this.deleted==0:
						print "Not Found"
					else:
						this.deleted=0
					return
		if this.current:# go back in order to seach the right nodes
			if this.current.parent:
				this.current=this.current.parent
				return
	
		return
class Graph():
		def __init__(this):
			this.dic={}# initilaize a new dictionary for the graph
			this.list1=[]# initilize a temproray list 
		def addVertex(this,value):
			if this.dic.has_key(value):# is the key found in the dictionary
				print "Vertex already exists"
			else:# if not add it with an empty values section
				dic2={value:[]}
				this.dic.update(dic2)# add it to the dicitonary
			return
		def addEdge(this,value1,value2):# add new edge between two vertices
			if this.dic.has_key(value1) and this.dic.has_key(value2):# check if the two vertices are present
				
				this.dic.get(value1).append(value2)# add each in the others' list
				this.dic.get(value2).append(value1)
			else:# if one or two vertices not found, print the follwoing
				print "One or more vertices not found."
			return
				
		def findVertex(this,value):# search for the vertex
			if this.dic.has_key(value):# is the value present in the 
				print "Vertices adjecsent to "+value+" are:"
				
				for w in this.dic.get(value):# walk through the values adjecsent to the value and print them
					print(w)
			else:# if the value not found, print the follwoing
				print "Vertex Not Found"
				
print "input 1 to test Queue"
print "input 2 to test Stack"
print "input 3 to test Binary Tree"
print "input 4 to test Graph"
x=input("input -999 to Quit ")
while x!=-999:
		
#Queue Test
	if x==1:
		print "Testing the Queue"
		print "adding 1, 3, 6, 8, 4, 5, 12, 9, 15, 7, 23, 45"
		que=myQueue()
		que.putq(1)
		que.putq(3)
		que.putq(6)
		que.putq(8)
		que.putq(4)
		que.putq(5)
		que.putq(12)
		que.putq(9)
		que.putq(15)
		que.putq(7)
		que.putq(23)
		que.putq(45)
		print "poping all values out of the queue"
		que.popq()
#Stack Test
	if x==2:
		print "Testing the Stack"
		print "Adding 1, 3, 6, 8, 4, 5, 12, 9, 15, 7, 23, 45"
		stack = Stack1()
		stack.push(1)
		stack.push(3)
		stack.push(6)
		stack.push(8)
		stack.push(4)
		stack.push(5)
		stack.push(12)
		stack.push(9)
		stack.push(15)
		stack.push(7)
		stack.push(23)
		stack.push(45)
		print "\n Checking the size of the values in graph: "
		print stack.checkSize()
		print "poping all values out of the stack:"
		while stack.checkSize()!=0:
			print stack.pop()
	elif x==3:
#Binary Tree Test
		print "Testing the Binary Tree"
		print "Root has value 1"
		binary=BinaryTree(1)
		print "Addiing 2 to 1"
		binary.add(2,1)
		print "Addiing 3 to 1"
		binary.add(3,1)
		print "Addiing 4 to 2"
		binary.add(4,2)
		print "Addiing 5 to 2"
		binary.add(5,2)
		print "Addiing 6 to 3"
		binary.add(6,3)
		print "Addiing 7 to 4"
		binary.add(7,4)
		print "Addiing 8 to 6"
		binary.add(8,6)
		print "Addiing 9 to 6"
		binary.add(9,6)
		print "Addiing 10 to 8"
		binary.add(10,8)
		print "Addiing 11 to 7"
		binary.add(11,7)
		print "Addiing 12 to 2"
		binary.add(12,2)
		print "Addiing 13 to 23"
		binary.add(13,20)

		print "Printing Tree"
		binary.printT()

		print "Deleting 9 (can be deleted)"
		binary.delete(9)
		print "Deleting 11 (can be deleted)"
		binary.delete(11)
		print "Deleting 12 (12 was never added to the tree)"
		binary.delete(12)
		print "Deleting 3 (3 has two children )"
		binary.delete(3)
		print "Deleting 19 (19 was never added to the tree)"
		binary.delete(19)
		print "Printing Tree after deleted values"
		binary.printT()


	elif x==4:
#Graph test
		print "Testing the Graph"
		print "adding the vertex: a, b, c, d , e ,f ,g, h, i, j, k, l, m"
		g=Graph()
		g.addVertex('a')	
		g.addVertex('b')
		g.addVertex('c')	
		g.addVertex('d')
		g.addVertex('e')	
		g.addVertex('f')
		g.addVertex('g')	
		g.addVertex('h')
		g.addVertex('i')	
		g.addVertex('j')
		g.addVertex('k')	
		g.addVertex('l')
		g.addVertex('m')	
		print "adding edges between: (a,b),(b,c),(c,d),(d,e),(e,f),(f,g),(g,h),(h,i),(i,j),(j,k),(k,l),(l,m),(m,a)"
		g.addEdge('a','b')
		g.addEdge('b','c')
		g.addEdge('c','d')
		g.addEdge('d','e')
		g.addEdge('e','f')
		g.addEdge('f','g')
		g.addEdge('g','h')
		g.addEdge('h','i')
		g.addEdge('i','j')
		g.addEdge('j','k')
		g.addEdge('k','l')
		g.addEdge('l','m')
		g.addEdge('m','a')
		print "adding edges between: (a,e),(a,h),(b,j),(c,m),(c,i),(d,g),(e,m),(f,m),(h,k),(i,m)"
		g.addEdge('a','e')
		g.addEdge('a','h')
		g.addEdge('c','m')
		g.addEdge('c','i')
		g.addEdge('d','g')
		g.addEdge('e','m')
		g.addEdge('f','m')
		g.addEdge('h','k')
		g.addEdge('i','m')

		print "adding edge between: a and z (z is not in the graph)"
		g.addEdge('z','a')

		print "adding vertex: n"
		g.addVertex('n')
		print "adding edges: (a,n), (n,h)"
		g.addEdge('a','n')
		g.addEdge('h','n')

		print "finding vertex: a"
		g.findVertex('a')
		print "finding vertex m"
		g.findVertex('m')
		print "finding vertex: c"
		g.findVertex('c')

		print "finding vertex: l"
		g.findVertex('l')
		print "finding vertex d"
		g.findVertex('d')
		print "finding vertex: n"
		g.findVertex('n')
	print "\ninput 1 to test Queue"
	print "input 2 to test Stack"
	print "input 3 to test Binary Tree"
	print "input 4 to test Graph"
	x=input("input -999 to Quit ")
print "Thank you have a good day"
