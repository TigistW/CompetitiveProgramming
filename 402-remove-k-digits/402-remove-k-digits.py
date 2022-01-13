class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ls=[]
        ls2 = []
        if k ==  len(num):
            return '0'
        for i in num:
            ls.append(i)
        print(ls)
        print(ls2)
        for i in ls:
            while ls2 and ls2[-1] > i and k >0: 
                ls2.pop()
                k-=1                
            ls2.append(i)
        while(k >0):
            ls2.pop()
            k-=1
        return str(int(''.join(ls2)))
        