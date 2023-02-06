class Solution:
    def racecar(self, target: int) -> int:
        queue = [(0, 1)]
        cnt = 0
        
        while queue:
            for i in range(len(queue)):
                position, speed = queue.pop(0)
                if position == target:
                    return cnt
                queue.append((position + speed, speed*2))
                new_speed = -1 if speed > 0 else 1
                if (position + speed) < target and speed < 0 or (position + speed) > target and speed > 0:
                    queue.append((position, new_speed))
            cnt += 1