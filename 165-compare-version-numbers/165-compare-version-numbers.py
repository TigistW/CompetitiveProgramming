class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        size = min(len(version1),len(version2))
        size2 = max(len(version1),len(version2))
        
        if len(version1) < len(version2):
            for i in range(size2 - size):
                version1.append('0')
        if len(version1) > len(version2):
            for i in range(size2 - size):
                version2.append('0')
        i = 0
        while True:
            one = version1[i] 
            two = version2[i]
            if int(one) == int(two): 
                if i + 1 == len(version2): 
                    break
                else:
                    i += 1
            elif int(one) > int(two):
                return 1
            else:
                return -1
        return 0
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            