class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = sorted([(position[i],speed[i]) for i in range(len(speed))], key=lambda item:item[0]) 
        hd = arr[-1]
        flt = 0
        for i in range(len(arr)-1, -1, -1):
            t_av = (target-hd[0])/hd[1]
            if arr[i][1]<=hd[1]:
                hd=arr[i]
                flt+=1
                continue
            t_needed = (hd[0] - arr[i][0]) / (arr[i][1]-hd[1])
            if t_needed<=t_av:
                continue
            else:
                hd = arr[i]
                flt+=1
        return  flt