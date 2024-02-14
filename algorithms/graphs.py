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
        self.verticles = [[0 for i in range(verticle_num)] for j in range(verticle_num)]

    def add_edge(self, v1, v2, value, directed=False):
        if value == 0:
            return
        self.verticles[v1 - 1][v2 - 1] = value
        if not directed:
            self.verticles[v2 - 1][v1 - 1] = value

    def remove_edge(self, v1, v2, directed=False):
        self.verticles[v1 - 1][v2 - 1] = 0
        if not directed:
            self.verticles[v2 - 1][v1 - 1] = 0

    def get_edge(self, v1, v2):
        value = self.verticles[v1 - 1][v2 - 1]
        if self.verticles[v1 - 1][v2 - 1] == self.verticles[v2 - 1][v1 - 1]:
            return (False, value)
        return (True, value)
    
    def get_all_edges(self):
        edges = set()
        for i in range(len(self.verticles)):
            for j in range(i + 1, len(self.verticles[i])):
                if self.verticles[i][j] != 0:
                    edges.add((i + 1, j + 1))
        return sorted(edges)

    def get_adjacents(self, verticle):
        adjacents = []
        path = self.verticles[verticle - 1]
        for i in range(len(path)):
            if path[i] != 0:
                adjacents.append(i + 1)
        return adjacents        

    def get_graph(self):
        for i in self.verticles:
            print(*i)

    def table_overwrite_graph(self, table):
        for i in range(len(self.verticles)):
            for j in range(len(self.verticles[i])):
                self.add_edge(i + 1, j + 1, int(table[i][j]))

    def get_count_edges(self):
        edge_count = 0
        for i in range(len(self.verticles)):
            for j in range(i + 1, len(self.verticles[i])):
                if self.verticles[i][j] > 0:
                    edge_count += 1
        return edge_count
    
    def get_graph_type(self):
        for i in range(len(self.verticles)):
            if self.verticles[i][i] != 0:
                return "NO"
            for j in range(len(self.verticles)):
                if self.verticles[i][j] != self.verticles[j][i]:
                    return "NO"
        return "YES"

