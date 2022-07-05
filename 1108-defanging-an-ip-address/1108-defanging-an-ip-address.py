class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        value = ""
        for i in address:
          if i.isdigit():
            value += i  
          else:
            value += "[.]"
        return value
            
          