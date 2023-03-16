# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 and len(postorder) == 0:
            return
        root = postorder[-1]
        inorderIdx = inorder.index(root)

        p_right_set = set(inorder[inorderIdx+1:])
        p_right = []
        for i in postorder:
            if i in p_right_set:
                p_right.append(i)

        p_left_set = set(inorder[:inorderIdx])
        p_left = []
        for i in postorder:
            if i in p_left_set:
                p_left.append(i)
        lft = self.buildTree(inorder[:inorderIdx], p_left)
        rgt = self.buildTree(inorder[inorderIdx+1:], p_right)
        cur = TreeNode(root)
        cur.left = lft
        cur.right = rgt
        return cur