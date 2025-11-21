"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):    

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


    
if __name__ == "__main__":
    sol = Solution()
    # You can add test cases here to create a graph and test the cloneGraph method.
    # For example:
    node1 = Node(1)
    # node2 = Node(2)
    # node1.neighbors = [node2]
    # node2.neighbors = [node1]
    cloned_graph = sol.cloneGraph(node1)
    pass
