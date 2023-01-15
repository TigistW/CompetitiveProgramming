class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find_parent(node, parent_list):
            if parent_list[node] != node:
                parent_list[node] = find_parent(parent_list[node], parent_list)
            return parent_list[node]
        num_nodes = len(vals)
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        parents = list(range(num_nodes))
        size = defaultdict(Counter)
        for i, val in enumerate(vals):
            size[i][val] = 1
        good_paths = num_nodes
        for val, node in sorted(zip(vals, range(num_nodes))):
            for neighbor in graph[node]:
                if vals[neighbor] > val:
                    continue
                parent1, parent2 = find_parent(node, parents), find_parent(neighbor, parents)
                if parent1 != parent2:
                    good_paths += size[parent1][val] * size[parent2][val]
                    parents[parent1] = parent2
                    size[parent2][val] += size[parent1][val]
        return good_paths