class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
      return []

    res = ['']
    letters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for i in digits:
      lis = []
      for j in res:
        for k in letters[ord(i) - ord('0')]:
          lis.append(j + k)
      res = lis
    return res

                    
            
            
        
        