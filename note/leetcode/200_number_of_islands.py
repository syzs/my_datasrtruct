'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''

'''
1. 染色 Flood Fill
    a. 遍历节点
        if node == '1': 
            count++;
            将node和附近所有相邻节点-> '0' 
      
        count = 0
        ["1","1","0","0","0"]
        ["1","1","0","0","0"]
        ["0","0","1","0","0"] 
        ["0","0","0","1","1"]

        count=1
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
        ["0","0","1","0","0"]
        ["0","0","0","1","1"]

        count=2
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
        ["0","0","0","1","1"]

        count=3
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
        ["0","0","0","0","0"]
    b.dfs
    c.bfs
2.并查集
    a.初始化。只需要针对'1'的节点，自身的parent为自身
    b.遍历所有节点，相邻的节点合并

    ["1"<"1","0","0","0"]
      ^   ^ 
    ["1","1","0","0","0"]
    ["0","0","1","0","0"] 
    ["0","0","0","1"<"1"]
    c. 遍历查询有多少个parent
'''

from typing import List

class UnionFind():
    def __init__(self, grid:List[List[str]]):
        m, n = len(grid), len(grid[0])
        
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue
                self.parent[i*n+j] = i*n+j # 二维转成一维的数组下标
                self.count += 1
        
    def findRoot(self, i:int):
        # while self.parent[i] != i:
        #     i = self.parent[i]
        # return self.parent[i]

        if self.parent[i] != i:
            self.parent[i] = self.findRoot(self.parent[i])
        return self.parent[i]
        
        
    def union(self, i:int, j:int):
        iRoot = self.findRoot(i)
        jRoot = self.findRoot(j)

        if iRoot == jRoot: return

        # 合并节点
        self.count -= 1 
        if self.rank[iRoot] > self.rank[jRoot]:
            self.parent[jRoot] = iRoot
        elif self.rank[iRoot] < self.rank[jRoot]:
            self.parent[iRoot] = jRoot
        else:
            self.parent[iRoot] = jRoot
            self.rank[jRoot] += 1

class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0,0]
        self.dy = [0,0,-1, 1]

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslandsUF(grid)

    def numIslandsUF(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        uf = UnionFind(grid)

        directions = [(-1, 0),(1, 0),(0,-1),(0,1)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue
                for d in directions:
                    nextI, nextJ = i+d[0], j+d[1]
                    if 0 <= nextI < m and 0<=nextJ < n and grid[nextI][nextJ] == '1':
                        uf.union(i*n+j, nextI*n+nextJ)
        return uf.count

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        self.queue = collections.deque()
        self.visited = set()
        self.grid = grid

        self.m, self.n = len(grid), len(grid[0])
        
        res = []
        for i in range(self.m):
            for j in range(self.n):
                res.append(self.floodfillBFS(i,j))
        return sum(res)


    def floodfillBFS(self, i, j):
        if not self.isValidIndex(i,j): return 0

        self.visited.add((i,j))
        self.queue.append((i,j))
        while self.queue:
            i, j = self.queue.popleft()
            for k in range(4):
                nextI, nextJ = i + self.dx[k], j + self.dy[k]
                if self.isValidIndex(nextI, nextJ):
                    self.visited.add((nextI, nextJ))
                    self.queue.append((nextI, nextJ))
        return 1


    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()

        res = []
        for i in range(self.m):
            for j in range(self.n):
                res.append(self.floodfillDFS(i,j))
        return sum(res)
       
    
    def floodfillDFS(self, i:int, j:int) -> int:
        if not self.isValidIndex(i, j): return 0

        # 把当前点标记为已访问
        self.visited.add((i,j)) 

        # 查看上下左右的节点
        for k in range(4):
            # 把相邻的点标记为已访问，防止重复计数
            self.floodfillDFS(i+self.dx[k], j+self.dy[k]) 
        # TODO Python 高级语法糖的使用 map(self.floodfillDFS, self.dx, self.dy)
        return 1

    
    def isValidIndex(self, i:int, j:int)->bool:
        # if i < 0 or i >= self.m or j < 0 or j >= self.n:
        #     return False
        # if self.grid[i][j] == '0' or (i,j) in self.visited:
        #     return False
        # return True

        return 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j] == '1' and not (i,j) in self.visited

