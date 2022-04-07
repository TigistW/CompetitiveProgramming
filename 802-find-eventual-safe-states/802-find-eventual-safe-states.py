class Solution:
    def eventualSafeNodes(self,graph: List[List[int]]) -> List[int]:
        def dfs(graph, state, idx):  
            if state[idx]:
                return state[idx]
            state[idx] = 1
            
            for next_node_idx in graph[idx]:
                
                next_state = dfs(graph, state, next_node_idx)
                
                if next_state ==1:
                    return state[idx]
                
            state[idx] = 2
            return state[idx]
        
        safe_nodes = []
        state = [0] * len(graph)
        
        for idx in range(len(graph)):
            if dfs(graph, state, idx) == 2:
                safe_nodes.append(idx)
        return safe_nodes          
   