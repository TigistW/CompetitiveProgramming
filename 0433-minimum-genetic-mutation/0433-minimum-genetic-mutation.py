class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque()
        queue.append(start)
        components = ["A", "T", "G", "C"]
        ops = 0
        visited = set()
        while queue:
          for i in range(len(queue)):
            cur = queue.popleft()
            if cur == end:
                return ops
            else:
              for idx in range(len(start)):
                for i in components:
                  cur_changed = cur[:idx] + i + cur[idx + 1:]
                  if cur_changed in bank and cur_changed not in visited:
                    queue.append(cur_changed)
                    visited.add(cur_changed)
          ops += 1
        return -1        