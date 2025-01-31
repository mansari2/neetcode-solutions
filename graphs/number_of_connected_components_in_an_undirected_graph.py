#DFS solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0 
        seen = set()
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        for i in range(n):
            if self.dfs(graph,i,seen):
                count += 1
        return count
    
    def dfs(self, graph,node,seen):
        if node in seen:
            return False
        seen.add(node)
        
        for nextnode in graph[node]:
            self.dfs(graph,nextnode,seen)
            
        return True


#union find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for A,B in edges:
            uf.union(A,B)
        
        count = 0
        for i in range(n):
            if i == uf.root[i]:
                count += 1
        return count
   

class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self,x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1