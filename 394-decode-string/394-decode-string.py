class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        numbers=[] 
        strings=[]
        current=[]
        for i in s:
            if i.isdigit():
                num=num*10 + ord(i) - ord("0")
                # print(ord("A"),ord("a"),ord("0"))
                # num=ord(i)-48
                # print(ord(i)-48)
            elif i.isalpha():
                current.append(i)
            elif i=="[":
                numbers.append(num)
                strings.append(current)
                num, current=0,[]
                # num=0
                # current=[]
            elif i=="]":
                strings[-1].extend(current*numbers.pop())
                current=strings.pop()
        return "".join(current)