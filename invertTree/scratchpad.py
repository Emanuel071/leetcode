# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # first, return the tree
        if root is None:
            return None
        if root:
            pass
        temp = root.right
        root.right = root.left
        root.left = temp

        # print("Inverted Node:", root.val)
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        

if __name__ == "__main__":
    sol = Solution()
    # create sample trees for testing
    # Tree
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print("---- Now Inverting ----")
    inverted_root = sol.invertTree(root)
    # The inverted tree should be:
    #       4
    #      / \
    #     7   2
    #    / \ / \
    #   9  6 3  1
    print(inverted_root.val)  # Output: 4
    print(inverted_root.left.val)  # Output: 7
    print(inverted_root.right.val)  # Output: 2
    print(inverted_root.left.left.val)  # Output: 9
    print(inverted_root.left.right.val)  # Output: 6
    print(inverted_root.right.left.val)  # Output: 3
    print(inverted_root.right.right.val)  # Output: 1