class DirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
            self.edges.append((from_vertex, to_vertex))

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            self.edges = [(f, t) for f, t in self.edges if f != vertex and t != vertex]
            #两个都不等于才不会删去
    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].remove(to_vertex)
            self.edges.remove((from_vertex, to_vertex))

    def vertex_exists(self, vertex):
        return vertex in self.vertices

    def get_neighbors(self, vertex):
        return self.vertices.get(vertex, [])

    def get_indegree(self, vertex):
        return sum(1 for v in self.vertices.values() if vertex in v)

    def get_outdegree(self, vertex):
        return len(self.vertices.get(vertex, []))

    def get_vertex_count(self):
        return len(self.vertices)

    def get_edge_count(self):
        return len(self.edges)

    def get_all_vertices(self):
        return list(self.vertices.keys())

    def get_all_edges(self):
        return self.edges
# 创建一个有向图对象
graph = DirectedGraph()

# 添加顶点
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

# 添加有向边
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.add_edge("E", "A")

# 测试获取顶点的邻居
neighbors = graph.get_neighbors("A")
print("Neighbors of A:", neighbors)  # 输出: Neighbors of A: ['B']

# 测试获取顶点的入度和出度
indegree = graph.get_indegree("A")
outdegree = graph.get_outdegree("A")
print("InDegree of A:", indegree)  # 输出: InDegree of A: 1
print("OutDegree of A:", outdegree)  # 输出: OutDegree of A: 1

# 测试删除顶点
graph.remove_vertex("A")
print("All Vertices:", graph.get_all_vertices())  # 输出: All Vertices: ['B', 'C', 'D', 'E']
print("All Edges:", graph.get_all_edges())  # 输出: All Edges: [('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')]

# 测试删除有向边
graph.remove_edge("B", "C")
print("All Edges:", graph.get_all_edges())  # 输出: All Edges: [('C', 'D'), ('D', 'E'), ('E', 'A')]

# 测试顶点是否存在
exists = graph.vertex_exists("B")
print("Vertex B exists:", exists)  # 输出: Vertex B exists: True

# 测试获取顶点和边的数量
vertex_count = graph.get_vertex_count()
edge_count = graph.get_edge_count()
print("Vertex Count:", vertex_count)  # 输出: Vertex Count: 4
print("Edge Count:", edge_count)  # 输出: Edge Count: 3
