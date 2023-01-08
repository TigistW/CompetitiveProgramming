class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        a, b, c, d= int(num1[0]), int(num2[0]), int(num1[1][:-1]), int(num2[1][:-1])
        val =  (a * b) - (c * d)
        val_i = (a * d) + (b * c)
        return str(val) + "+" + str(val_i) + "i"
        