class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.FirstArc = None
class Arc(object):
    def __init__(self, adjacent):
        self.adjacent = adjacent
        self.info = None
        self.NextArc = None
class Graph(object):
    def __init__(self, kind):
        self.kind = kind
        self.VertexNum = 0
        self.ArcNum = 0
        self.Vertices = []
    def CreateGraph(self):
        print('请依次输入图中各顶点的值，每个顶点值以回车间隔，并以#作为输入结束符：')
        date = input('->')
        while date != '#':
            vertex = Vertex(date)
            self.Vertices.append(vertex)
            self.VertexNum = self.VertexNum + 1
            date = input('->')
        print('请依次输入图中每条边的两个顶点值，两个顶点值以空格作为间隔，每输入一组后进行换行，最终以#结束输入：')
        arc = input('->')
        while arc != '#':
            TailVertex = Vertex(arc.split()[0])  # 这里应该直接使用arc.split()[0]作为顶点数据
            HeadVertex = Vertex(arc.split()[1])  # 同上
            TailIndex = self.LocateVertex(TailVertex.data)  # 使用TailVertex.data获取顶点数据
            HeadInedx = self.LocateVertex(HeadVertex.data)  # 使用HeadVertex.data获取顶点数据
            self.InsertArc(TailIndex, HeadInedx)
            self.ArcNum = self.ArcNum + 1
            arc = input('->')
        print('创建成功')

    def LocateVertex(self, Vertex):
        index = 0
        while index < len(self.Vertices):  # 这里不需要比较self.Vertices[index].date，因为Vertex已经是输入的顶点值
            if self.Vertices[index].data == Vertex:  # 使用data而不是date
                return index
            index = index + 1
        return None  # 如果没有找到顶点，返回None或适当的错误处理
    def InsertArc(self, TailIndex, HeadIndex):
        if self.kind == 0:  # 无向图
            TailArc = Arc(TailIndex)
            HeadArc = Arc(HeadIndex)
            HeadArc.NextArc = self.Vertices[TailIndex].FirstArc
            self.Vertices[TailIndex].FirstArc = HeadArc
            TailArc.NextArc = self.Vertices[HeadIndex].FirstArc
            self.Vertices[HeadIndex].FirstArc = TailArc
        elif self.kind == 2:  # 有向图
            HeadArc = Arc(HeadIndex)
            HeadArc.NextArc = self.Vertices[TailIndex].FirstArc
            self.Vertices[TailIndex].FirstArc = HeadArc

    def GetFirstAdjacentVertex(self, Vertex):
        FirstArc = self.Vertices[Vertex].FirstArc
        if FirstArc is not None:
            return FirstArc.adjacent

    def GetNextAdjacentVertex(self, Vertex, Adjacent):
        ArcLink = self.Vertices[Vertex].FirstArc
        while ArcLink is not None:
            if ArcLink.adjacent is Adjacent:
                if ArcLink.NextArc is not None:
                    return ArcLink.NextArc.adjacent
                else:
                    return None
            else:
                ArcLink = ArcLink.NextArc

    def DFSTraverse(self):
        visited = []
        index = 0
        while index < self.VertexNum:
            visited.append('False')
            index = index + 1
        index = 0
        while index < self.VertexNum:
            if visited[index] == 'False':
                self.DFS(visited, index)
            index = index + 1
            if index == self.VertexNum:
                print("\n 该图连通！")
    def DFS(self, visited, Vertex):
        visited[Vertex] = 'True'
        self.VisitVertex(Vertex)
        NextAdjacent = self.GetFirstAdjacentVertex(Vertex)
        while NextAdjacent is not None:
            if visited[NextAdjacent] == 'False':
                self.DFS(visited, NextAdjacent)
            NextAdjacent = self.GetNextAdjacentVertex(Vertex, NextAdjacent)
    def VisitVertex(self,Vertex):
        print(self.Vertices[Vertex].data,end='')
if __name__ == '__main__':
    graph = Graph(0)
    graph.CreateGraph()
    print('深度优先递归遍历图的结果如下:')
    graph.DFSTraverse()