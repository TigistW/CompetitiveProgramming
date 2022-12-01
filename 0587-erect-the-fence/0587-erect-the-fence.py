class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        l=len(trees)
        if l<=3:
            return trees
        
        minx=min(t[0] for t in trees)
        miny=None
        for i in range(l):
            if trees[i][0]==minx and (miny==None or trees[i][1]<miny):
                miny=trees[i][1]
                mini=i
        trees[0], trees[mini]= trees[mini], trees[0]

        def ang(x1, y1):
            if x1>0:
                return y1/x1/(1+abs(y1/x1))
            elif x1<0:
                return 2+y1/x1/(1+abs(y1/x1))
            elif y1>0:
                return 1
            else:
                return 3

        angle=[]
        x0=trees[0][0]
        y0=trees[0][1]
        for i in range(1, l):
            x1, y1=trees[i]
            angle.append((ang(x1-x0, y1-y0), abs(x1-x0)+abs(y1-y0), trees[i]))        
        angle.sort(key=lambda x:(x[0], x[1]))

        amin=angle[0][0]
        amax=angle[-1][0]
        if amin!=amax:
            i=l-2
            while i>=0 and angle[i][0]==amax:
                i-=1
            angle[i+1:]=reversed(angle[i+1:])

        def comp3(p0, p1, p2):
            x0, y0=p0
            x1, y1=p1
            x2, y2=p2
            tmp1=ang(x1-x0, y1-y0)
            tmp2=ang(x2-x0, y2-y0)
            if tmp1<=1:
                return tmp1<=tmp2 and tmp2<=tmp1+2
            return tmp1<=tmp2 or tmp2<=tmp1-2

        ans=[trees[0]]

        for i in range(l-2):            
            p1=angle[i][2]
            p2=angle[i+1][2]
            if comp3(ans[-1], p1, p2):
                ans.append(p1)
            else:
                while len(ans)>=2 and not comp3(ans[-2], ans[-1], p2):
                    ans.pop()
        
        p1=angle[-1][2]
        if comp3(ans[-1], p1, ans[0]):
            ans.append(p1)
        else:
            while len(ans)>=2 and not comp3(ans[-2], ans[-1], ans[0]):
                ans.pop()

        return ans
