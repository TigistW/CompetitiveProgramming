class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit, ans = [], [], []
        for i in logs:
          identifier = i.split(" ")[0]
          val = i.split(" ")[1:]
          if val[-1].isdigit():
            digit.append(i)
          else:
            val = " ".join(val)
            letter.append((identifier,val))
        
        letter = sorted(letter, key = lambda x: (x[1], x[0]))
        for i in letter:
          ans.append(i[0] + " " + i[1])
        ans.extend(digit)
        return ans
            
            
          