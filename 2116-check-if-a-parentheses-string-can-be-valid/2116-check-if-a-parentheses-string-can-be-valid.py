class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        curr_size = len(locked)
        
        match = 0
        unmatch = 0
        
#         match2 = 0
#         unmatch2 = 0
        
        
        if curr_size % 2 != 0:
            return False
        
        if s[-1] == "(" and locked[-1] == "1":
            return False
        
        if s[0] == ")" and locked[0] == "1":
            return False
        
        for i in range(curr_size):
            if s[i] == ")" and locked[i] == "1":
                match += 1
                if match > (i + 1)//2:
                    print("ggg")
                    return False
            j = len(s) - 1 - i
                
            if s[j] == "(" and locked[j] == "1":
                unmatch += 1
                if unmatch > (len(s) - j)//2:

                    return False
        return True
            
            
            
#             if s[i] == "(" or locked[i] == "0":
#                 match += 1
#             else:
#                 unmatch += 1
#             if unmatch > match:
#                 return False
#         for i in range(curr_size - 1 , 0):
#             if s[i] == ")" or locked[i] == "0":
#                 match2 += 1
#             else:
#                 unmatch2 += 1
#             if unmatch2 > match2:
#                 return False
            
#         return True
                
            
            
            
            

                
                
            