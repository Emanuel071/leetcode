class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque

        # Build the adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Initialize the queue with nodes having in-degree of 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0

        while queue:
            course = queue.popleft()
            visited_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_courses == numCourses

if __name__ == "__main__":
    # Example usage (only runs when executed directly):
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # Output: True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # Output: False