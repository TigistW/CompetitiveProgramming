
#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str):
        dictOp={"(":")","[":"]","{":"}"}
        
        li=[]
        if(len(s)%2==0):
            for tag in s:
                if tag in dictOp.keys():
                    li.append(tag)
                else: 
                    if tag in dictOp.values():
                        if len(li)==0:
                            return False
                        elif dictOp[li[-1]]==tag:
                            li.pop()
                        else: 
                            return False             
        else:
            return False
        
        return len(li) == 0 