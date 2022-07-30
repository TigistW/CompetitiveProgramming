class Solution:
    def reverseParentheses(self, s: str) -> str:
        # def reverseParentheses( s ):
        stack = []
        for i in range(len(s)):
          
            if (s[i] == "("):
                stack.append(s[i])
            elif (s[i] >= "a" and s[i] <= "z"):
                stack.append(s[i])
            else:
                s1 = ""
                while len(stack) > 0:
                    a = stack.pop()
                    if (a == "("):
                        break
                    s1 = a + s1
                    
                s1 = s1[::-1]
                for i in s1:
                    stack.append(i)
        s1 = ""
        for i in stack:
            s1 = s1 + i

        return s1