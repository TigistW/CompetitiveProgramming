class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0 for i in range(n)]
        for i,j in edges:
            incoming[j] += 1
        ans = []
        for i in range(len(incoming)):
            if incoming[i] == 0:
                ans.append(i)
        return ans