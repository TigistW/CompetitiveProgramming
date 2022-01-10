class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        k = len(arr)
        result = []

        while k > 1:
            maxVal = 0
            for i in range(k):
                if arr[i] > arr[maxx]:
                    maxx = i
            reverse = arr[maxVal::-1]
            arr[:maxVal + 1] = reverse
            rev = arr[0:k]
            rev = rev[:: -1]
            arr[0: k] = rev

            result.append(maxVal + 1) if maxVal > 0 else None
            result.append(k) if k > 0 else None
            k -= 1
        return result
