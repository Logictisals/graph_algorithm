from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  # 邻接表

    def add_edge(self, u, v):
        # 添加有向边
        self.graph[u].append(v)

    def topological_sort_kahn(self):
        # 计算所有顶点的入度
        in_degree = {i: 0 for i in range(1, self.V + 1)}
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # 队列，存储所有入度为0的顶点
        queue = deque([i for i in range(1, self.V + 1) if in_degree[i] == 0])
        top_order = []

        while queue:
            # 从队列中移除一个顶点并添加到拓扑排序结果中
            v = queue.popleft()
            top_order.append(v)

            # 减少相邻顶点的入度，并把入度为0的顶点添加到队列
            for neighbour in self.graph[v]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        # 检查是否存在环
        if len(top_order) == self.V:
            return top_order
        else:
            return "A cycle exists in the graph"

# 示例
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Kahn's Algorithm Topological Sort:")
print(g.topological_sort_kahn())


# 继续使用上面的Graph类定义

def topological_sort_dfs(self):
    visited = [False] * (self.V + 1)
    stack = []  # 用于存储拓扑排序结果
    for i in range(1, self.V + 1):
        if not visited[i]:
            if not self.dfs_visit(i, visited, stack):
                return None  # 如果存在环，则返回None
    stack.reverse()
    return stack

def dfs_visit(self, v, visited, stack):
    visited[v] = True
    for neighbour in self.graph[v]:
        if not visited[neighbour]:
            if not self.dfs_visit(neighbour, visited, stack):
                return False
    stack.append(v)
    return True

# 示例
g = Graph(6)
# 与上面Kahn算法的例子使用相同的图结构

print("DFS Topological Sort:")
print(g.topological_sort_dfs())