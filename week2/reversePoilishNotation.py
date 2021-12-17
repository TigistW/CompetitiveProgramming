#https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        li = []
        for i in tokens:
            if i not in operators:
                li.append(int(i))
            else:
                if i == '+':
                    val = li[-2]+li[-1]
                    li = li[:-2]
                    li.append(val)
                elif i == '-':
                    val = li[-2]-li[-1]
                    li = li[:-2]
                    li.append(val)
                elif i == '/':
                    val = int(li[-2]/li[-1])
                    li= li[:-2]
                    li.append(val)
                elif i == '*':
                    val = li[-2]*li[-1]
                    li = li[:-2]
                    li.append(val)
        return li[0]