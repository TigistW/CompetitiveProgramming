
class Solution:
  def countGoodNumbers(self, n: int) -> int:
    modulonum = 1000000007

    def recur(x: int, n: int) -> int:
      if n == 0:
        return 1
      if n & 1:
        return x * recur(x, n - 1) % modulonum
      return recur(x * x % modulonum, n // 2)

    return recur(4 * 5, n // 2) * (5 if n & 1 else 1) % modulonum

            