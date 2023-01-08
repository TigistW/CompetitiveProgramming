class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        ans = [0 for i in range(len(boxes))]
        for i in range(len(boxes)):
          for j in range(len(boxes)):
            if boxes[j] == "1":
              ans[i] += int(fabs(i - j))
        return ans