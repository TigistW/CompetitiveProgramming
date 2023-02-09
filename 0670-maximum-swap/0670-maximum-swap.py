class Solution:
    def maximumSwap(self, num: int) -> int:
        def max_finder(num):
            biggest, idx = -1, 0
            for i,val in enumerate(num):
                if int(val) >= biggest:
                    biggest = int(val)
                    idx = i
            return idx 
        
        
        num = list(str(num))
        for i in range(len(num)):
            if num[i] != "9":
                maxx = max_finder(num[i:])
                maxx += i
                if int(num[maxx]) > int(num[i]):
                    num[i], num[maxx] = num[maxx], num[i]
                    break
        return int("".join(num))

                
                
                
                
                