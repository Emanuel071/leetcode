# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    sol = Solution()
    # Create a sample linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reverse the list
    reversed_head = sol.reverseList(head)
    print(reversed_head)  # Output the head of the reversed list
    # Print the reversed list (for verification)
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    pass
        