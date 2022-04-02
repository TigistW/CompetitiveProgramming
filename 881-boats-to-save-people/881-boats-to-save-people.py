class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        size = len(people)
        people.sort()
        slow = 0
        fast = size - 1
        for i in range(size):
            # print(slow,fast)
            if slow == fast:
                return count+1
            if slow > fast:
                return count
            if people[slow] + people[fast] <= limit:
                count+=1
                slow = slow + 1
                fast = fast - 1

            else:
                count += 1
                fast = fast - 1
                
                


            
        
