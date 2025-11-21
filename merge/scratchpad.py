# intervals = [[1,3],[2,6],[8,10],[15,18]]

# merged = []

# temp = intervals.pop(0)


# merged.append(temp)


# temp = intervals.pop(0)

# print("Temp Interval:")
# print(temp[0], temp[1])    
# print("Last Merged Interval:")
# print(merged[0][0], merged[0][1])

# if temp[0] >=  merged[0][0] and temp[0] >= merged[0][1]:
#     print("Popped Interval:")
#     (temp)
#     merged.append(temp)
# else:
#     temp.pop(0)

# if
# if temp[0] >=  merged[0][0] and temp[0] >= merged[0][1]:
#     print("Popped Interval:")
#     (temp)

# print("Merged Intervals:")
# print(merged)
    

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        mergeds = []
        intervals.sort(key= lambda x: x[0])

        while intervals:
            first = intervals.pop(0)
            if intervals:
                nextone = intervals.pop(0)
            else:
                mergeds += [first]
                break
            if first[1] >= nextone[0]:
                intervals.insert(0, [first[0], max(first[1], nextone[1])])
            else:
                mergeds += [first]
                intervals.insert(0,nextone)
        
        return mergeds

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))  # Output: [[1,5]]
    print(sol.merge([[4,7],[1,4]])) # Output: [[1,7]]