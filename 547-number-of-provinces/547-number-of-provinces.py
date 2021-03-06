class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.count
    
class UF:
    def __init__(self,size):
        # for i in range(size):
        #     self.root = i
        self.root = [i for i in range(size)]
        self.count = size
    
    def find(self,node):
        if self.root[node] != node:
            return self.find(self.root[node])
        return self.root[node]
    
    def union(self,node1,node2):
        node1_pare,node2_pare = self.find(node1),self.find(node2)
        if node1_pare != node2_pare:
            self.root[node2_pare] = node1_pare
            self.count -= 1
    
    def count(self):
        return self.count 