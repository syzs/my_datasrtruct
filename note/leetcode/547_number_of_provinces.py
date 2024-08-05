'''
547. Number of Provinces
Medium

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''

class Solution:
    def __init__(self):
        self.directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return self.__findCircleNumDFS(isConnected)
    
    def __findCircleNumUF(self, isConnected: List[List[int]]) -> int:
        # parent[2]=1, parent[3]=2, 合并 parent[3]=1
        return 0
    
    # A->B->C 类比到 树/图 结构
    def __findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        if not isConnected or not isConnected[0]: return 0

        n = len(isConnected)
        # 记录哪些城市已经被访问过
        visited = set()

        def dfs(i):
            # 对于每个未被访问过的城市，进行一次DFS搜索，将所有与之连通的城市标记为已访问。
            for j, v in enumerate(isConnected[i]):
                # v=isConnected[i][j]
                if not v or j in visited: continue
                visited.add(j)
                dfs(j) # i 可以联通 j，再继续探查 j 可以联通哪些城市

        count = 0
        for i in range(n):
            if i in visited: continue
            dfs(i)
            count +=1
        return count
            

    def __findCircleNumDFS_onlyDirectConnection(self, isConnected: List[List[int]]) -> int:
        if not isConnected or not isConnected[0]: return 0

        self.n = len(isConnected)
        self.visited = set()
        count = 0

        self.isConnected = isConnected
        
        for i in range(self.n):
            for j in range(i+1):
                count += self.__dfs_onlyDirectConnection(i, j)
        
        return count
    
    def __dfs_onlyDirectConnection(self, i:int, j:int)->int:
        if not (0 <= i < self.n and 0 <= j <= i and self.isConnected[i][j] and not (i,j) in self.visited):
            return 0
        
        self.visited.add((i,j)) # 染色
        for k in self.directions:
            self.__dfs_onlyDirectConnection(i + k[0], j + k[1]) # 将相邻的点染色 
        return 1