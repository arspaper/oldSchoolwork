class Graph:
	def __init__(self, verticle_num):
			self.verticles = [list()] * verticle_num

	def edge_add(self, v1, v2):
		self.verticles[v1 - 1].append(v2)
		self.verticles[v2 - 1].append(v1)
	
	def edge_remove(self, v1, v2, is_directed=False):
		if not is_directed:
			self.verticles[v1 - 1].remove(v2 - 1)
			self.verticles[v2 - 1].remove(v1- 1)
		else:
			self.verticles[v1 - 1].remove(v2 - 1)
	
	def edge_get(self, v1, v2):
		flag = False
		for element in self.verticles[v1 - 1]:
			if element == v2:
				flag = True
		return flag
		
	def get_adjacent(self, verticle):
		return self.verticles[verticle]


class NewGraph:
	def __init__(self, verticle_num):
		self.verticles = [[None for i in range(verticle_num)] for j in range(verticle_num)]

	def edge_add(self, v1, v2, value):
		if v1 == v2:
			return -1
		self.verticles[v1 - 1][v2 - 1] = value
		self.verticles[v2 - 1][v1- 1] = value
	
	def edge_remove(self, v1, v2):
		if v1 == v2:
			return -1
		self.verticles[v1 - 1][v2 - 1] = None
		self.verticles[v2 - 1][v1 - 1] = None
	
	def edge_get(self, v1, v2):
		if v1 == v2:
			return -1
		return self.verticles[v1 - 1][v2 - 1]
		
	def get_adjacent(self, verticle):
		adjacents = list()
		path = self.verticles[verticle - 1]
		for i in range(len(path)):
			if path[i] is not None:
				adjacents.append(i + 1)
		return(adjacents)	
	
	def graph_get(self):
		for i in self.verticles:
			print(i)


a = NewGraph(5)
a.edge_add(2, 3, 5)
a.edge_add(2, 4, 10)
print(a.edge_get(3, 2))
print(a.get_adjacent(3))
a.graph_get()