class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(("+","-","/","*"))
        stack = []
        for i in tokens:
          # print(stack)
          if i not in ops:
            stack.append(i)
          else:
            if stack and i in ops:
              one = stack.pop()
              two = stack.pop()
              val = 0
              if i == "+":
                val = int(one) + int(two)
              elif i == "*":
                val = int(one) * int(two)
              elif i == "-":
                val = int(two) - int(one)
              else:
                val = int(two) / int(one)
            stack.append(val)
            
        # print(type(stack[-1]))
        return int(stack[-1])
              