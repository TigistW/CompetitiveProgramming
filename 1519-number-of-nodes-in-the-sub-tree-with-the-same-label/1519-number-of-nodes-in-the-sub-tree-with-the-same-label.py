class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for s , e in edges:
            tree[s].append(e)
            tree[e].append(s)
        res=[0]*n

        def dfs(node , par):
            nonlocal res
            count = Counter()
            for  neighbor in tree[node]:
                if neighbor != par:
                    count += dfs(neighbor,node)
            count[labels[node]] += 1
            res[node] =  count[labels[node]]

            return count
        dfs(0,-1)
        return res