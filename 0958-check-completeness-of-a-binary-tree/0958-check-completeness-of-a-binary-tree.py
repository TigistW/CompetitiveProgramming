# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def valid_level(self, level_numbers, level):
        total_nodes = 2 ** level
        return total_nodes == level_numbers

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels_map = defaultdict(int)

        none_map = defaultdict(bool)

        queue = [(root, 0)]
        previous_level = 0
        while queue:
            node, level = queue.pop(0)
            if not node:
                none_map[level] = True
            else:
                if none_map[level]:
                    return False
                if previous_level == level:
                    levels_map[level] += 1
                elif previous_level != level and self.valid_level(levels_map[previous_level], previous_level):
                    levels_map[level] += 1
                    previous_level = level
                else:
                    return False
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return True