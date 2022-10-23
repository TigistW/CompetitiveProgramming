class Solution:
    def minWindow(self, s: str, t: str) -> str:
        checker=set(list(t))
        left,right=0,0
        ans=[float("inf"),None]
        extra=defaultdict(int)
        tot=dict(Counter(t))
        
        while right<len(s):
            if len(tot)==0:
                # print(left,right)
                if ans[0]>=right-left:
                    ans[1]=(left,right)
                    ans[0]=(right-left)
                    
                if s[left] in extra and s[left] in checker:
                    extra[s[left]]-=1
                    if extra[s[left]]==0: del extra[s[left]]
                elif s[left] not in extra and s[left] in checker:
                    tot[s[left]]=1
                left+=1
            else:
                if s[right] in checker and s[right] in tot:
                    tot[s[right]]-=1
                    if tot[s[right]]==0: del tot[s[right]]
                elif s[right] in checker and s[right] not in tot:
                    extra[s[right]]+=1
                right+=1
        if len(tot)==0:
            while len(tot)==0 and left<right:
                if ans[0]>=right-left:
                    ans[1]=(left,right)
                    ans[0]=(right-left)
                if s[left] in extra and s[left] in checker:
                    extra[s[left]]-=1
                    if extra[s[left]]==0: del extra[s[left]]
                elif s[left] not in extra and s[left] in checker:
                    tot[s[left]]=1
                left+=1
        if ans[0]<float("inf"):
            return s[ans[1][0]:ans[1][1]]
        else:
            return ""