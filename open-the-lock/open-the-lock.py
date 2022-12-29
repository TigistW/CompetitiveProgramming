class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append("0000")
        
        visited = set()
        ans = 0
        level_step = 0
        while queue:
          level_size = len(queue)
          for i in range(level_size):
            curr = queue.popleft()
            
            if curr == target:
              return level_step

            if curr not in visited and curr not in deadends:
              for i in range(len(curr)):
                curr1 = list(curr)
                curr2 = list(curr)

                if curr1[i] == "9":
                  curr1[i] = "0"
                else:
                  curr1[i] = str(int(curr1[i]) + 1)

                if curr2[i] == "0":
                  curr2[i] = "9"
                else:
                  curr2[i] = str(int(curr2[i]) - 1)

                val = "".join(curr1)
                val2 = "".join(curr2)
                
                if val not in visited and val not in deadends:
                  queue.append(val)
                if val2 not in visited and val2 not in deadends:
                  queue.append(val2)
                  
              visited.add(curr)
          level_step += 1
          
        return -1
          
          
          