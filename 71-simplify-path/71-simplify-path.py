class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        
        for i in path.split('/'):
            if i == "" or i == ".":
                continue
            if i == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(i)
            
        return "/" + "/".join(stk)