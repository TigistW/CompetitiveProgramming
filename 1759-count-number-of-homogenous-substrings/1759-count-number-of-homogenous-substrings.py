class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        cur = ""
        ind = 0
        for i in s:
            if cur == "" or i == cur:
                ind += 1
                cur = i
                # print(cur, ind, i)
                
            else:
               
                count += int((ind / 2) * (ind + 1))
                count = count % 1000000007
                cur = i
                ind = 1
        
        count += int((ind / 2) * (ind + 1))
        count = count % 1000000007
        
        
        return count 
    
    
                
                
                
            
                
                