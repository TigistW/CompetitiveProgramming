class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left,right,string):
          if left == 0 and right == 0:
            ans.append(string)
          if left > 0:
            dfs(left - 1, right, string + '(')
          if left < right:
            dfs(left, right - 1, string + ')')

        dfs(n, n, '')
        return ans
      
      
      