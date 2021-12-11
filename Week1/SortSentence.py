#https://leetcode.com/problems/sorting-the-sentence/
class Solution:
    def sortSentence(self, s: str) -> str:
        singles=s.split()
        words= [None for _ in range(len(singles))]
        print(singles)
        for single in singles:
            num=int(single[-1])-1
            words[num]=single[:-1]
        return ' '.join(words)