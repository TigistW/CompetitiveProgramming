class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulonum = 1000000007
        result = 1
        if n % 2 == 0:
            for i in range(n//2):
                result = (20*result) % modulonum
            return result
        else:
            for i in range(n//2):
                result = (20*result) % modulonum
            return (result*5) % modulonum

#         for i in range(n//4):
#                 result=(400*result)%modulonum

#         if n%4==0:
#             return result
#         elif n%4==1:
#             return (result*5)%modulonum
#         elif n%4==2:
#             return (result*20)%modulonum
#         else:
#             return (result*100)%modulonum
