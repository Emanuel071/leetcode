class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i = 0
        # Add all intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        print("Merged so far:")
        print(merged)
        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        print("NewInterval after merging overlaps:")
        print(newInterval)
        merged.append(newInterval)
        print("Merged after adding newInterval:")
        print(merged)

        # Add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))  # Output: [[1,5],[6,9]]
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]
        