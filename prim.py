import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, mst_set):
        """从优先队列中选择最小权值的边"""
        min_value = float('inf')
        for v in range(self.V):
            if mst_set[v] == False and self.graph[self.parent][v] != 0:
                min_value = min(min_value, self.graph[self.parent][v])
        return min_value

    def prim_mst(self, parent):
        self.parent = parent
        mst_set = [False] * self.V
        parent_list = [None] * self.V
        weight_sum = 0

        mst_set[parent] = True
        for _ in range(self.V - 1):
            min_value = self.min_key(mst_set)
            u = self.graph.index(min_value, 1)
            mst_set[u] = True
            weight_sum += min_value
            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and self.graph[u][v] < min_value:
                    parent_list[v] = u
        return weight_sum, parent_list

# 创建图对象
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

# 执行Prim算法
parent = 0
mst_weight, parent_list = g.prim_mst(parent)

print("边的总权重为:", mst_weight)
print("最小生成树的边:", parent_list)