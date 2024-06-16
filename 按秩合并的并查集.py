class UnionFind:
    def __init__(self,n):
        self.n=n
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
    # def find(self,x):
    #     while x!=self.root[x]:
    #         x = self.root[x]
    #     return x
    def find_lujinyasuo(self,x):
        if  x== self.root[x]:
            return x
        return self.find_lujinyasuo(self.root[x])
    def union(self,x,y):
        root_x,root_y=self.find_lujinyasuo(x),self.find_lujinyasuo(y)
        if root_x !=root_y:
            """谁的秩比较大就将小秩连接到大的上面去"""
            if self.rank[root_x]>self.rank[root_y]:
                self.root[root_y]=root_x
            elif self.rank[root_x]<self.rank[root_x]:
                self.root[root_y] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] +=1
    def connected(self,x,y):
        return self.find_lujinyasuo(x) == self.find_lujinyasuo(y)
if __name__ == "__main__":
    demo=UnionFind(5)
    demo.union(0,1)
    demo.union(0,2)
    demo.union(0,3)
    demo.union(2,3)
    print(demo.root)
    print(demo.connected(2,3))