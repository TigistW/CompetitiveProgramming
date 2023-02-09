class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(begin):
            if len(variant) == 4 and begin == len(s):
                ans.append('.'.join(variant))
                return
            for i in range(1, 4):
                var = s[begin:begin + i]
                if len(var) > 1 and (var[0] == '0' or int(var) > 255):
                    continue
                if len(variant) < 4:
                    variant.append(var)
                    backtrack(begin + i)
                    variant.pop()
        variant = []
        ans = []
        backtrack(0)
        return ans