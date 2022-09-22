class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if A[i]>B[j]:
                A[k]=A[i]
                i-=1
            else:
                A[k]=B[j]
                j-=1
            k-=1
        if j>=0:
            A[:k+1]=B[:j+1]

        
        