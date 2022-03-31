class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lis_size = len(flowerbed)
        lis_count = []
        count, possible  = 1, 0
        
        
        if lis_size == 1 and flowerbed[0] == 0:
            if n <= 1:
                return True
            return False
        
        else:
            for i in range(lis_size - 1):
                slow = i
                fast = i + 1
                if flowerbed[slow] == flowerbed[fast]:
                    count += 1
                    if fast == (lis_size - 1):
                        if flowerbed[slow] == flowerbed[fast]:
                            lis_count.append((flowerbed[fast],count))
                else:
                    lis_count.append((flowerbed[slow],count))
                    count = 1
                    if fast == lis_size - 1:
                        if flowerbed[slow] != flowerbed[fast]:
                            lis_count.append((flowerbed[fast],count))
        # print(lis_count)
        
        for i in range(len(lis_count)):
            if i == 0 or i == len(lis_count) - 1:
                if len(lis_count) == 1:
                    if lis_count[i][1] >= 2:
                        if lis_count[i][1] % 2 == 0:
                            possible += lis_count[i][1] // 2
                        else:
                            possible += (lis_count[i][1] // 2) + 1 
                else:
                    if lis_count[i][1] >= 2:
                        possible += lis_count[i][1] // 2
            else: 
                if lis_count[i][1] >= 3:
                    if lis_count[i][1] % 2 == 0:
                        possible += lis_count[i][1] // 3
                    else:
                        possible += lis_count[i][1] // 2
                      
        # print(possible)
        if possible >= n:
            return True
        return False
