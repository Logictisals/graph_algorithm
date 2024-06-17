class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(graph):
    result = []  # 存储最小生成树的边
    edges = sorted(graph['edges'], key=lambda item: item[2])  # 按权重排序边
    uf = UnionFind(graph['vertices'])  # 初始化并查集

    # 遍历边并选择
    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):  # 如果u和v不在同一个连通分量
            result.append(edge)  # 添加到结果
            uf.union(u, v)  # 合并u和v的连通分量

    return result

# 示例图的表示
# graph = {
#     'vertices': 4,  # 顶点数量
#     'edges': [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
# }

# 使用示例
# mst = kruskal(graph)
# print("Edges in the minimum spanning tree are:", mst)

"""Kruskal算法是一种用于寻找图的最小生成树（Minimum Spanning Tree, MST）的贪心算法。
最小生成树是连接图中所有顶点的边的集合，且这些边的权重之和最小，同时保证图是连通的。Kruskal算法的基本思想是按照边的权重从小到大的顺序选择边，每次选择时确保加上这条边后不会产生环。
Kruskal算法的步骤如下：

排序：将图中的所有边按照权重从小到大排序。
初始化：创建一个空的边集合，用来存放最小生成树的边。
遍历：遍历排序后的边列表，对于每条边：
使用并查集（Union-Find）数据结构检查这条边连接的两个顶点是否已经在同一个连通分量中。
如果不在同一个连通分量中，将这条边加入到最小生成树的边集合中，并通过并查集将这两个顶点合并到同一个连通分量。
结束条件：当边集合中边的数量等于图中顶点数减去1，或者遍历完所有边时，算法结束。
Kruskal算法的效率主要取决于排序和并查集的操作。使用优先队列（例如最小堆）可以有效地实现边的排序，而并查集则可以快速地判断两个顶点是否在同一连通分量中，并进行合并。

Kruskal算法适用于边稠密的图，因为它在边的数量上具有较好的时间复杂度。算法的时间复杂度是O(E log E)
，其中E是边的数量。如果使用朴素的排序算法，这个复杂度可能会退化到O(E log V)，其中V是顶点的数量。但是，如果使用并查集，这个复杂度可以保持在O(E log E)。"""