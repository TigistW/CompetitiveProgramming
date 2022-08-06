class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
#         ls=[]
#         ls2 = []
#         if k ==  len(num):
#             return '0'
#         for i in num:
#             ls.append(i)
#         print("ls",ls)
#         print("ls2",ls2)
#         for i in ls:
#             while ls2 and ls2[-1] > i and k >0: 
#                 ls2.pop()
#                 k-=1                
#             ls2.append(i)
#         print("ls2.. 2",ls2)
        
#         while(k >0):
#             ls2.pop()
#             k-=1
#         return str(int(''.join(ls2)))

        ls2 = []
        if k ==  len(num):
            return '0'
        for i in num:
            while ls2 and ls2[-1] > i and k >0: 
                ls2.pop()
                k-=1                
            ls2.append(i)
        while(k >0):
            ls2.pop()
            k-=1
        return str(int(''.join(ls2)))


  
#           mono_stack = []
#           # number_to_remove = k
#           for i in num:
#               while k>0 and mono_stack and mono_stack[-1]>i:
#                   mono_stack.pop()
#                   k-=1
#               mono_stack.append(i)
              
#           while(k >0):
#             mono_stack.pop()
#             k-=1
#           answer = "".join(mono_stack[0:len(num)-k]).lstrip("0")
#           print(mono_stack)
#           print(answer)
        