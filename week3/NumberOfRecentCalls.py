#https://leetcode.com/problems/number-of-recent-calls/
class RecentCounter:
    def __init__(self):
        self.count = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1
        while self.queue and self.queue[0] < t-3000:
            self.queue.popleft()
            self.count -= 1
        return self.count

    def __init__(self):
        self.queue = []
        self.index = 0

    def ping(self, t: int) -> int:
        (self.queue).append(t)
        for i in range(self.index, len(self.queue)):
            if self.queue[i] >= self.queue[-1] - 3000:
                self.index = i
                return len(self.queue) - self.index
