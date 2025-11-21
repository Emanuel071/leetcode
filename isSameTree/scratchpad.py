# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.p_list = []
        self.q_list = []
    
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return 0
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)
        
        print(p.val)
        self.p_list.append(p.val)
        self.q_list.append(q.val)
        return self.p_list == self.q_list

if __name__ == "__main__":
    sol = Solution()
    # create two sample trees for testing
    # Tree 1
    #       1
    #      / \
    #     2   3
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    # Tree 2
    #       1
    #      / \
    #     2   3
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(sol.isSameTree(p, q))  # Output: True
    # print(sol.isSameTree(p, q))  # Output: True

    # Modify Tree 2
    #       1
    #      / \
    #     2   4
    q.right.val = 4
    print(sol.isSameTree(p, q))  # Output: False