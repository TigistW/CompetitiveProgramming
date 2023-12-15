class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        incoming = {}
        
        for i, j in paths:
            graph[i] = j
            incoming[j] = 1

        start  = ""
        for i, j in paths:
            if i not in incoming:
                start = i
            
        for i in range(len(paths)):
            start = graph[start]

        return start
            