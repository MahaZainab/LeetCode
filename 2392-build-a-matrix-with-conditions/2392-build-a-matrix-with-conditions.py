from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(n, conditions):
            graph = defaultdict(list)
            in_degree = {i: 0 for i in range(1, n + 1)}

            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1

            queue = deque([node for node in range(1, n + 1) if in_degree[node] == 0])
            topo_order = []

            while queue:
                node = queue.popleft()
                topo_order.append(node)

                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return topo_order if len(topo_order) == n else []

        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_position = {num: i for i, num in enumerate(row_order)}
        col_position = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            matrix[row_position[num]][col_position[num]] = num

        return matrix
