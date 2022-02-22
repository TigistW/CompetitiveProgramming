#User function Template for python3

class Solution:
    
    def leftChild(self,ind):
        return (2*ind) +1
    def rightChild(self,ind):
        return (2*ind) + 2
    def parent(self,ind):
        return (ind-1)//2
        
    def getMin(self,arr):
        return arr[0]
    def insert(self,arr,n,val):
        i = len(arr)
        arr.append(val)
        self.upheap(arr,n+1,i)
    def update(self,arr,n,i,val):
        arr[i] = val
        self.heapify(arr,n,i)
    def remove(self,arr,n,i):
        arr[n-1],arr[i] = arr[i],arr[n-1]
        del arr[n-1]
        self.heapify(arr,n-1,i)
    def upheap(self,arr,n,i):
        p = self.parent(i)
        while p >= 0 and arr[i] < arr[p]:
            temp = arr[p]
            arr[p] = arr[i]
            arr[i] = temp
            i = p
            p = self.parent(p)
    def downheap(self,arr,n,i):
        j = i
        left = self.leftChild(j)
        right = self.rightChild(j)
        
        if left < n and arr[left] < arr[j]:
            j = left
        if right < n and arr[right] < arr[j]:
            j = right
        if j != i:
            arr[j],arr[i] = arr[i],arr[j]
            self.downheap(arr,n,j)
 
    def heapify(self,arr, n, i):
        self.upheap(arr,n,i)
        self.downheap(arr,n,i)
            

    def buildHeap(self,arr,n):
        for i in range(n):
            self.upheap(arr, n, i)
          
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        # print(arr)
        for i in range(n-1, 0, -1):
            # print(arr)
            arr[i], arr[0] = arr[0], arr[i]  
            # print(*arr)
            self.heapify(arr, i, 0)
        arr.reverse()   
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends