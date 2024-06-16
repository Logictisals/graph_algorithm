from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph) :
        ans = list()
        stk = list()
        def dfs(x):
            if x ==len(graph)-1:
                ans.append(stk[:])
                return
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        stk.append(0)
        dfs(0)
        return ans
class Solution:
    def allPathsSourceTarget(self, graph):
        ans = list()
        queue = deque([(0,[0])])
        while queue:
            node , path = queue.popleft()#出队操作
            if node == len(graph)-1:
                ans.append(path)
                continue
            for neighbor in graph[node]:
                queue.append((neighbor,path+[neighbor]))
        return ans
solution = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
ans=solution.allPathsSourceTarget(graph)
print(ans)
a = [12,31,1]
print(a)
print(a[:])