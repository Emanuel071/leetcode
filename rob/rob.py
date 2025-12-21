class Solution(object):
    class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # Edge case: no houses -> nothing to rob.
            if not nums:
                return 0

            # We use a rolling DP approach:
            # prev2 = max loot up to house i-2
            # prev1 = max loot up to house i-1
            # For each house i we decide:
            #   - skip house i -> loot = prev1
            #   - rob  house i -> loot = prev2 + nums[i]
            # current is the best of these two choices for house i.
            #
            # This uses O(1) extra space instead of O(n) by keeping only
            # the last two states required to compute the next state.
            prev2, prev1 = 0, nums[0]

            # Iterate from the second house to the last.
            # At step i we compute the best loot considering houses[0..i].
            for i in range(1, len(nums)):
                # If we rob current house, we must add nums[i] to prev2 (i-2).
                # If we don't rob it, we keep prev1 (i-1).
                current = max(prev1, prev2 + nums[i])

                # Slide the window: shift prev1 -> prev2, current -> prev1
                # so the next iteration has the correct i-1 and i-2 values.
                prev2, prev1 = prev1, current

            # After the loop prev1 holds the maximum loot possible.
            # Time complexity: O(n) because we visit each house once.
            # Space complexity: O(1) because we only keep two variables.
            return prev1

    if __name__ == "__main__":
        sol = Solution()
        print(sol.rob([1,2,3,1]))  # Output: 4
        print(sol.rob([2,7,9,3,1]))  # Output: 12

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))  # Output: 4
    print(sol.rob([2,7,9,3,1]))  # Output: 12