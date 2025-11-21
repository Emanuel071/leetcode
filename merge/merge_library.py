class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:  # Overlap
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))  # Output: [[1,5]]
    print(sol.merge([[4,7],[1,4]])) # Output: [[1,7]]