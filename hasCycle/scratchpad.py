# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        for i in range(10): #limit to 10^4 nodes to avoid infinite loop in case of cycle
    
            if head is None:
                return False
            if head:
                print(f"index {i} value:{head.val}")
                head = head.next
            else:
                return True
            count += 1
            if count == 10**4:
                return True
        
        print(count)

if __name__ == "__main__":
    sol = Solution()

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

    # result_no_cycle = sol.hasCycle(nodeA)
    # print("Has Cycle:", result_no_cycle)  # Output: False