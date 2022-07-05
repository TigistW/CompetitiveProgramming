class Solution:
    def interpret(self, command: str) -> str:
        cmd = ""
        ans = ""
        sets = ("G","()","(al)")
        
        for i in command:
          cmd += i
          if cmd not in sets:
            continue
          else:
            if cmd == "G":
              ans+= "G"
            elif cmd == "()":
              ans += "o"
            else:
              ans += "al"
              
            cmd = ""
        return ans
              
          
            
            
            
          