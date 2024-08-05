'''
684. Redundant Connection
Medium

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Exmaple2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
'''

from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.connected_nodes = defaultdict(list)
        # [[1,2],[1,3],[2,3]]
        for edge in edges:
            self.visited = defaultdict(bool)
            x,y = edge[0], edge[1]
            # 1.0 [1,2]
            # 2.0 [1,3]
            # 3.0 [2,3]
            if self.__is_already_connected(x,y):
                return edge
            # 1.2 {1:[2], 2:[1]}
            # 2.2 {1:[2,3], 2:[1]}
            self.connected_nodes[x].append(y)
            self.connected_nodes[y].append(x)
        return []
        
    def __is_already_connected(self, x:int, y:int)->bool:
        if x == y: # 3.1.4 3==3
            return True

        # 2.1 visited={1:true}
        # 3.1 visited={2:true}
        self.visited[x] = True
        # 1.1 connected_nodes 为空，
        # 2.1 connected_nodes[1] -> [2] 
        # 2.1.3 connected_nodes[2] -> [1] 
        # 3.1.1 connected_nodes[2] -> [1] 
        # 3.1.3 connected_nodes[1] -> [2,3] 
        for n in self.connected_nodes[x]:
            # 2.1.4 visited[1]=true
            if n in self.visited: continue
            # 2.1.1 visited={1:true, 2:true}
            # 3.1.1 visited={1:true}
            self.visited[n] = True
            # 2.1.2 (2,3)
            # 3.1.2 (1,3)
            if self.__is_already_connected(n, y):
                return True
        return False