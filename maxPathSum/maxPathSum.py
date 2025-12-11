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
        # maximum path sum found so far
        self.max_sum = float('-inf')
        def helper(node):
            if not node:
                return 0
            
            # compute the maximum path sum of left and right subtrees
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            
            # current path sum including the current node
            current_path_sum = node.val + left_gain + right_gain
            
            # update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # return the maximum gain if continuing the same path
            return node.val + max(left_gain, right_gain)
        helper(root)
        return self.max_sum

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