#https://leetcode.com/problems/powx-n/
# class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     poww=1
    #     if n==0:
    #         return 1
    #     if n>0:
    #         for i in range(n):
    #             poww*=x
    #         return poww
    #     else:
    #         for i in range(n*-1):
    #             poww*=x
    #         return 1/poww

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==-1:
            return 1/x
        if n==1:
            return x
        if n%2!=0:
            odd = x 
        else:
            odd=1
        return self.myPow(x*x,n//2) * odd