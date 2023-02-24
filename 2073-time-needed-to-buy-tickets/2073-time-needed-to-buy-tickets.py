class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        n = len(tickets)
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i] != 0 and tickets[k] != 0:
                    tickets[i] -= 1
                    total += 1
                else:
                    continue
        return total