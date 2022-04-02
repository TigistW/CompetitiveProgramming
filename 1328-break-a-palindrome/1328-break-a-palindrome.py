class Solution:
    def breakPalindrome(self, palindrom: str) -> str:
        lis_pali  = []
        
        if len(palindrom) == 1:
            return ""
        for i in palindrom:
            lis_pali.append(i)
        
        for i in range(len(lis_pali)):
            
            if lis_pali[i] != "a":
                    if i != len(lis_pali) - 1:
                        if i != (len(lis_pali) // 2):
                            lis_pali[i] = "a"
                            break
                        
            elif lis_pali[i] == "a" and i == len(lis_pali) - 1:
                lis_pali[i] = chr(ord(lis_pali[i]) + 1)
                break
                
                
        return ''.join (lis_pali)
                 