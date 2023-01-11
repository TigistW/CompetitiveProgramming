def dfs(v,gp,parent,hasApple):
    vt=0
    for i in range(len(gp[v])):
        if gp[v][i]!=parent:
            t=dfs(gp[v][i],gp,v,hasApple)
            if hasApple[gp[v][i]] or t>0:
                vt+=2+t
    return vt
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        gp=[]
        for i in range(n):
            gp.append([])
        for i in range(len(edges)):
            gp[edges[i][0]].append(edges[i][1])
            gp[edges[i][1]].append(edges[i][0])
        return dfs(0,gp,None,hasApple)