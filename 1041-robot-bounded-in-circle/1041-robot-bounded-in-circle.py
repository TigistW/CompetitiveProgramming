class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0, 0]
        dxn = "north"

        def orientdxn(dxn, ops):
            if dxn == "north":
                if ops == "L":
                    dxn = "west"
                else:
                    dxn = "east"
            elif dxn == "east":
                if ops == "L":
                    dxn = "north"
                else:
                    dxn = "south"
            elif dxn == "west":
                if ops == "L":
                    dxn = "south"
                else:
                    dxn = "north"
            else:
                if ops == "L":
                    dxn = "east"
                else:
                    dxn = "west"
            return dxn

        def move(dxn, pos):
            if dxn == "north":
                pos[1] += 1
            elif dxn == "west":
                pos[0] -= 1
            elif dxn == "east":
                pos[0] += 1
            else:
                pos[1] -= 1
            return pos
        
        for i in instructions:
            if i == "G":
                start = move(dxn, start)
            else:
                dxn = orientdxn(dxn, i)
            # print(start, dxn)
        return start == [0,0] or dxn != "north" 
        
        
    
                    
        