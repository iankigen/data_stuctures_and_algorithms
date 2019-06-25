"""
Breadth-first search is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes
at the next depth

Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at
the root node and explores as far as possible along each branch before backtracking.
"""


class Vertex(object):
	def __init__(self, name):
		self.name = name
		self.neighbours = list()

		self.distance = 9999
		self.status = 'unvisited'

		self.discovery = 0
		self.finish = 0

	def add_neighbour(self, vertex):
		if vertex not in set(self.neighbours):
			self.neighbours.append(vertex)
			self.neighbours.sort()


class Graph(object):
	vertices = {}
	time = 0

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbour(v)
				if key == v:
					value.add_neighbour(u)
			return True
		return False

	def print_graph(self):
		for key in sorted(self.vertices.keys()):
			print('Vertex :', key)
			print('Neighbours :', self.vertices[key].neighbours)
			print('Distance :', self.vertices[key].distance)
			print('-' * 40)

	def bfs(self, vertex):
		q = list()
		vertex.distance = 0
		vertex.status = 'visited'
		for v in vertex.neighbours:
			self.vertices[v].distance = vertex.distance + 1
			q.append(v)

		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.status = 'visited'

			for v in node_u.neighbours:
				node_v = self.vertices[v]
				if node_v.status == 'unvisited':
					q.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1

	def _dfs(self, vertex):
		global time
		vertex.status = 'visited'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbours:
			if self.vertices[v].status == 'unvisited':
				self._dfs(self.vertices[v])
		vertex.status = 'dfs_visited'
		vertex.finish = time
		time += 1

	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)


g = Graph()
a = Vertex('A')
g.add_vertex(a)
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

print('BFS')
g.bfs(a)
g.print_graph()
print('DFS')
g.dfs(a)
g.print_graph()
