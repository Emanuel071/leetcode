class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 1. Build the adjacency list and in-degree count
        graph = [[] for _ in range(numCourses)]  # Adjacency list (list of lists)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # 2. Initialize the queue (list) with nodes having in-degree of 0
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        visited_courses = 0

        # 3. Process the queue
        while queue:
            course = queue.pop(0)  # Simulate deque.popleft() using list.pop(0)
            visited_courses += 1

            # Iterate through neighbors using the adjacency list
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. Check if all courses were visited
        return visited_courses == numCourses

if __name__ == "__main__":
    # Example usage (only runs when executed directly):
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # Output: True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # Output: False