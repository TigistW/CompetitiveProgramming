#https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    
    def selectionSort(self, arr,n):
        for i in range(n):
        #finding the minimum value
            core=i
            for j in range(i+1,n):
                if arr[core]>arr[j]:
                    core=j
        #swap the current element with the one which was found to be a minimum
            arr[i],arr[core]=arr[core],arr[i]


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
