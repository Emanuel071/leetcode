class Solution(object):

    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low-1

        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                self.swap(arr,i,j)
        
        self.swap(arr,i+1,high)
        return i+1

    def swap(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]

    def quickSort(self,arr,low,high):
        if low<high:

            p = self.partition(arr,low,high)

            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.intervals = self.quickSort(intervals,0,len(intervals)-1)
        prev = intervals[0]

        for i in range(1,len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev[1] = max(prev[1],intervals[i][1])
            else:
                res.append(prev)
                prev = intervals[i]
        
        res.append(prev)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))  # Output: [[1,5]]
    print(sol.merge([[4,7],[1,4]])) # Output: [[1,7]]