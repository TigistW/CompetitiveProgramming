class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx < ry:
                parent[ry] = rx
            elif rx > ry:
                parent[rx] = ry
        for i, (a, b) in enumerate(zip(s1, s2)):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        return ''.join([chr(find(ord(c)-ord('a')) + ord('a')) for c in baseStr])