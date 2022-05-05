class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        accumulate = 0
        count = [0] * (n + 1)

        for citation in citations:
            count[min(citation, n)] += 1

        for i, c in reversed(list(enumerate(count))):
            accumulate += c
            if accumulate >= i:
                return i
