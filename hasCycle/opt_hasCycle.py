# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # move slow pointer by 1 step
            fast = fast.next.next     # move fast pointer by 2 steps
            
            if slow == fast:          # if they meet, there is a cycle
                return True
        
        return False                 # if we reach here, no cycle exists

if __name__ == "__main__":
    sol = Solution()
    # Example usage:
    # Creating a linked list with a cycle for testing
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    # Creating nodes
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # Linking nodes to form a cycle: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # creates the cycle here

    result = sol.hasCycle(node1)
    print("Has Cycle:", result)  # Output: True

    # Creating a linked list without a cycle for testing
    nodeA = ListNode(1)
    nodeB = ListNode(2)

    nodeA.next = nodeB  # no cycle

    result_no_cycle = sol.hasCycle(nodeA)
    print("Has Cycle:", result_no_cycle)  # Output: False