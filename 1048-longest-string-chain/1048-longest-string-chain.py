class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        maps = defaultdict()
        for word in sorted(words, key=len):
            length = 1
            for i in range(len(word)):
                sub_word = word[:i] + word[i + 1:]
                if sub_word in maps:
                    length = max(length, maps[sub_word]+1)
            maps[word] = length
        return max(maps.values())