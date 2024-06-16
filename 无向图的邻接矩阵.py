class GraphAdjMat:
    """邻接矩阵无向图`图类"""
    def __init__(self,vertices:list[int],edges:list[list[int]]):
        """构造方法"""
        #顶点列表,元素代表,"顶点值",索引代表"顶点索引"
        self.vertices:list[int]=[]
        #邻接矩阵,行列索引对应的"顶点索引"
        self.adj_mat:list[list[int]]=[]
        #添加顶点
        for val in vertices:
            self.add_vertex(val)
            #添加边
            #请注意,edge元素代表的是顶点的索引,即对应vertices元素索引
        for e in edges:
            self.add_edge(e[0],e[1])

    def size(self)->int:
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self,val:int):
        """添加顶点"""
        n=self.size()
        #向顶点列表中添加新顶点的值
        self.vertices.append(val)
        #在邻接矩阵中添加一行
        new_row=[0]*n
        self.adj_mat.append(new_row)
        #在邻接矩阵中添加一列
        for row in self.adj_mat:
            row.append(0)

    def add_edge(self,i:int,j:int):
        """添加边"""
        """参数i,j分别对应vertices元素索引"""
        #索引越界与相等处理
        if i<0 or j<0 or i>=self.size() or j>=self.size() or i== j:
            raise IndexError()
        #在无向图中,邻接矩阵关于主对角线对称,即满足i,j=j,i
        self.adj_mat[i][j]=1
        self.adj_mat[j][i]=1
    def remove_edge(self,i:int,j:int):
        """删除边"""
        """参数i,j,分别对应vertices的元素索引"""
        #索引越界与相等处理
        if i <0 or j <0 or i>=self.size()or j >= self.size() or i==j:
            raise  IndexError
        self.adj_mat[i][j]=0
        self.adj_mat[j][i]=0

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 = ",self.vertices)
        print("邻接矩阵 = ")
        print(self.adj_mat)

def graph_adj_mat():
    # 测试顶点和边
    vertices = ["A", "B", "C", "D"]
    edges = [[0, 1], [0, 2], [1, 3]]

    # 创建图实例
    graph = GraphAdjMat(vertices, edges)

    # 打印初始图状态
    print("初始图状态:")
    graph.print()

    # 测试添加顶点
    new_vertex = "E"
    graph.add_vertex(new_vertex)
    print(f"\n添加顶点 {new_vertex} 后的图状态:")
    graph.print()

    # 测试添加边
    new_edge = [2, 3]
    graph.add_edge(*new_edge)
    print(f"\n添加边 {new_edge} 后的图状态:")
    graph.print()

    # 测试删除边
    edge_to_remove = [0, 1]
    graph.remove_edge(*edge_to_remove)
    print(f"\n删除边 {edge_to_remove} 后的图状态:")
    graph.print()

    # 测试索引越界和删除不存在的边
    try:
        graph.remove_edge(5, 0)  # 索引越界
    except IndexError as e:
        print(f"\n尝试删除不存在的边时抛出了 IndexError: {e}")

    try:
        graph.add_edge(5, 0)  # 索引越界
    except IndexError as e:
        print(f"尝试添加不存在的边时抛出了 IndexError: {e}")

    # 测试边的对称性
    for i in range(graph.size()):
        for j in range(graph.size()):
            if i != j:
                assert graph.adj_mat[i][j] == graph.adj_mat[j][i], "邻接矩阵不满足对称性"

    print("\n所有测试通过！")

# 运行测试函数
graph_adj_mat()