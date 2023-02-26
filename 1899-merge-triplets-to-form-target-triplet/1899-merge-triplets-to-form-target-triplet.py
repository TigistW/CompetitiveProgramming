class Solution:
    def mergeTriplets(self, arr: List[List[int]], target: List[int]) -> bool:
        one = []
        two = []

        for i in range(len(arr)):
            if arr[i][0] == target[0] and arr[i][1] <= target[1] and arr[i][2] <= target[2]:
                one = arr[i]

        if one:
            for i in range(len(arr)):
                if arr[i][1] == target[1] and arr[i][0] <= target[0] and arr[i][2] <= target[2]:
                        two = arr[i]
            if two:
                for i in range(len(arr)):
                    if arr[i][2] == target[2] and arr[i][0] <= target[0] and arr[i][1] <= target[1]:
                        return True

            return False
        return False
