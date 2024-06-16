def dfs(graph,visited,res,vet):
    """深度优先辅助函数"""
    res.append(vet.val)#记录访问顶点
    visited.add(vet)#标记该顶点已经被访问了
    #遍历所有的邻接顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue
        dfs(graph,visited,res,adjVet)
def graph_dfs(graph,start_vet):
    res=[]
    visited=set()
    dfs(graph,visited,res,start_vet)
    return res