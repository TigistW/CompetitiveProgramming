class Solution:
    def sortVowels(self, s: str) -> str:
        subs = []
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        for i in s:
            if i in vowels:
                subs.append(ord(i))
        subs.sort()

        ans = list(s)
        ind = 0
        for i in range(len(s)):
            if s[i] in vowels:
                ans[i] = chr(subs[ind])
                ind += 1

        return "".join(ans)
