class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        val = s.split(' ')
        minn = 0
        for i in val:
            if i.isdigit(): 
              i = int(i)
              if i > minn: 
                minn = i
              else:
                  return False
        return True