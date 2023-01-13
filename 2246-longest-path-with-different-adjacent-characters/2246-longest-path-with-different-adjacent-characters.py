class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        from collections import defaultdict
        d=defaultdict(list)
        d[0]=[]
        for i in range(len(parent)):
            d[parent[i]].append(i)
        maxi=[0]
        def r(root):
            max1=''
            max2=''
            for i in d[root]:
                st=r(i)
                if st[-1]!=s[root]:
                    if len(st)>len(max1):
                        max2=max1
                        max1=st
                    elif len(st)>len(max2):
                        max2=st
            maxi[0]=max(maxi[0],len(max1)+len(max2)+1)
            return max1+s[root]
        r(0)
        return maxi[0]