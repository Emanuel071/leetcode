class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dp = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        for course in range(len[dp]):
            for prereq in prerequisites:
                if prereq[0] == course:
                    dp[prereq[1]] += 1


if __name__ == "__main__":
    # Example usage (only runs when executed directly):
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # Output: True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # Output: False