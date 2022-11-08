class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bits(val):
            count = 0
            while val > 0:
                lastBit = val & 1
                if lastBit: count+=1
                val = val >> 1
            return count
        
        ans = []
        for i in range(0,12):
            for j in range(0,60):
                if (bits(i) + bits(j)) == turnedOn:
                    hr = str(i)
                    mnt = "0" + str(j)
                    
                    temp = hr + ":" + mnt[-2:]
                    ans.append(temp)
        
        return ans