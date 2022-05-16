class Solution:
    def fizzBuzz(self,n):
        List=[]
        for i in range(1,n+1):
            if (i % 3 == 0 and i % 5 == 0):
                List.append("FizzBuzz")
                continue
            elif (i % 3 == 0):
                List.append("Fizz")
                continue
            elif (i % 5 == 0):
                List.append("Buzz")
                continue
            else:
                List.append(str(i))
        return List

        