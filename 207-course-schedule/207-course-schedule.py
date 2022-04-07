class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inE = [0] * numCourses
        queue = deque()
        count = 0
        outE = defaultdict(set)
        
        for i,j  in prerequisites:
            outE[j].add(i)  
            inE[i] += 1
            
        for i in range(numCourses):
            if inE[i] == 0:
                queue.append(i)
        
        while queue:
            c = queue.popleft()
            count += 1
            # print("c = ", c)
            
            for i in outE[c]:
                inE[i] -= 1
                if inE[i] == 0:
                    queue.append(i) 
        return count == numCourses
                    