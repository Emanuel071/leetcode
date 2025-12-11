# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify the merging process
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and append the smaller value to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts from the next of dummy node
        return dummy.next
    
if __name__ == "__main__":
    sol = Solution()
    # Example usage:

    # Creating first sorted linked list: 1 -> 3 -> 5
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    # Creating second sorted linked list: 2 -> 4 -> 6
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    merged_list = sol.mergeTwoLists(list1, list2)

    # Print merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None