class Solution:
  
    def reverseWords(self, s: str) -> str:

        arr = s.split(" ")
        n = len(arr)
        left = 0
        right = len(arr) - 1
        
        while left <= right:
          if arr[left] == " ":
            left += 1
          if arr[right] == " ":
            right -= 1
          
          if arr[left] != " " and arr[right] != " ":
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        ans = []
        for i in arr:
          if i:
            ans.append(i)
        return " ".join(ans)
        
          