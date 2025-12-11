# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
adssd
        

if __name__ == "__main__":
    sol = Solution()
    # create sample tree for testing
    #       -10
    #       /  \
    #      9   20
    #          / \
    #         15  7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = sol.maxPathSum(root)
    print("Maximum Path Sum:", result)  # Output: 42