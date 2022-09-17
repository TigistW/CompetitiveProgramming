class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0]* 38
        arr[0],arr[1],arr[2] = 0,1,1
        
        for i in range(n - 2):
          arr[i + 3] = arr[i] + arr[i + 1] + arr[i + 2]
          
        # print(arr)
        return arr[n]