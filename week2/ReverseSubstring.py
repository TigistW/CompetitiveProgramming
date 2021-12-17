#https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        li = []
        
        for i in s:
            if i == ')':
                temp = ""
        
                while ((x:=li.pop()) != '('):
                    temp += x
                for j in temp:
                    li.append(j)
            else:
                li.append(i)
        
        return "".join(li)
    
    