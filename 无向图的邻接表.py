from collections import deque
class Vertex:
    """顶点类"""
    def __init__(self, val):
        self.val = val

class GraphAdjList:
    """基于邻接表实现的无向图"""
    def __init__(self, edges):
        """构造方法"""
        # 邻接表,key:顶点,value:该顶点的所有临界顶点
        self.adj_list = {}

        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        """获取顶点的数量"""
        return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet2 == vet1:
            raise ValueError
        # 添加边,vet1,vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet2 == vet1:
            raise ValueError
        # 删除边 ,vet1,vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return
        # 在邻接表中添加一个新的邻接表
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError
        # 在邻接表中删除顶点vet对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表,删除所有包含vet的边
        for vertex, edges in self.adj_list.items():
            if vet in edges:
                self.remove_edge(vertex, vet)

    def display(self):
        """打印邻接表"""
        for vertex, edges in self.adj_list.items():
            tmp = [v.val for v in edges]
            print(f"{vertex.val}: {tmp}")



# 创建一些顶点
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)
v8 = Vertex(8)
v9 = Vertex(9)
# 创建一些边
edges = [
    (v1, v2), (v1, v4),
    (v2, v3), (v2, v5),
    (v3, v6),
    (v4, v5), (v4, v7),
    (v5, v6), (v5, v8),
    (v6, v9),
    (v7, v8),
    (v8, v9)
]

# 创建图
graph = GraphAdjList(edges)

# 打印图的邻接表
print("初始邻接表:")
graph.display()

# 测试添加顶点
v5 = Vertex(5)
graph.add_vertex(v5)
print("\n添加顶点后的邻接表:")
graph.display()
def graph_bfs(graph,start_vet:Vertex)->list[Vertex]:
    """广度优先遍历"""
    #使用邻接表取表示图,一边获取指定顶点的所有邻接顶点
    #顶点遍历序列
    res=[]
    #哈希表,用力记录已经访问过的顶点
    visited=set[Vertex]([start_vet])
    #队列用来实现bfs
    que=deque[Vertex]([start_vet])

    #以顶点vet为起点,遍历所有的顶点
    while len(que)>0 :
        vet=que.popleft()#队首元素出列
        res.append(vet.val)#记录访问顶点
        #遍历所有的邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                    continue#跳过访问过的顶点
            que.append(adj_vet)
            visited.add(adj_vet)
    #返回遍历的序列
    return res
from graph_dfs import *
ans=graph_dfs(graph,v1)
print(ans)