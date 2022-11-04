#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, N):
    	arr = [False for i in range(N + 1)]
    	for i in range(2, int(math.sqrt(N + 1)) + 1):
    	    if arr[i] == False:
    	        j = 0
    	        while i *(i + j) <= N:
    	            arr[i *(i + j)] = True
    	            j += 1
    	count = []
        for i in range(2, N + 1):
            if not arr[i]:
                count.append(i)
        return count
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends