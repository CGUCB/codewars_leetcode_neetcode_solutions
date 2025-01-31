from collections import defaultdict, deque
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n + 1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        if not self.is_bipartite(adj,n):
            return -1

        degree_bfs = [0]*(n + 1)

        for i in range(1,n+1):
            degree_bfs[i] = self.bfs_depth(adj,i)

        visited = [0]*(n + 1)
        groups = 0
        for i in range(1,n+ 1):
            if not visited[i]:
                groups += self.dfs(adj,visited,degree_bfs,i)
                
        return groups 

    def dfs(self,adj,visited,degree_bfs,node):

        visited[node] = 1
        max_depth = degree_bfs[node]

        for neigh in adj[node]:
            if not visited[neigh]:
                max_depth = max(max_depth , self.dfs(adj,visited,degree_bfs,neigh))

        return max_depth

    def bfs_depth(self,adj,node):
        
        queue = deque([(node,1)])
        visited = [0]*len(adj)
        visited[node] = 1
        last_depth = 1

        while queue:
            cur,depth = queue.popleft()
            last_depth = depth

            for neigh in adj[cur]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    queue.append((neigh,depth + 1))

        return last_depth

    def is_bipartite(self,adj,n):

        color = [0]*(n + 1)

        for i in range(1,n+1):
            if color[i] == 0 and not self.bfs_check_bipartite(adj,color,i):
                return False
        return True

    def bfs_check_bipartite(self,adj,color,node):

        queue = deque([node])
        color[node] = 1

        while queue:
            cur = queue.popleft()
            if color[cur] == 1:
                cur_color = 2
            else:
                cur_color = 1

            for neigh in adj[cur]:
                if color[neigh] == 0:
                    color[neigh] = cur_color
                    queue.append(neigh)
                elif color[neigh] != cur_color:
                    return False

        return True