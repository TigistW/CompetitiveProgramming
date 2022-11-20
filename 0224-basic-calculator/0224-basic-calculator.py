class Solution:
    def calculate(self, s: str) -> int:
        stacks = [[1]]
        cur_int = '0'
        for i,c in enumerate(s):
            if ord('0')<=ord(c)<=ord('9'):
                cur_int+=c
            if not (ord('0')<=ord(c)<=ord('9')) or i==len(s)-1:
                if int(cur_int)!=0:
                    stacks[-1].append(stacks[-1][0]*int(cur_int))
                cur_int = '0'
                if c =='+':
                    stacks[-1][0] = 1
                elif c=='-':
                    stacks[-1][0] = -1
                elif c=='(':
                    stacks.append([1])
                elif c==')':
                    innermost = sum(stacks.pop()[1:])
                    stacks[-1].append(stacks[-1][0]*innermost)
        return sum(stacks[0][1:])
        
        