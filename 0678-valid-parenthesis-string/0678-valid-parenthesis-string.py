class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == "(" or i =="*":
                stk.append(i)
            elif i == ")":
                if stk:
                    if "(" in stk:
                        del stk["".join(stk).rfind("(")]
                    else:
                        stk.pop()
                else: 
                    return False
        
        cnt = 0
        if stk:
            for i in stk:
                if i == "(":
                    cnt += 1
                if i == "*" and cnt:
                    cnt -= 1
            return cnt == 0
        else:
            return True
        