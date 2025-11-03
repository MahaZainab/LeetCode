class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # DFS
        n = len(rooms)
        visited = set()
        stack = [0]             # start from room 0

        while stack:
            room = stack.pop()  # DFS style
            if room in visited:
                continue
            visited.add(room)
        # add any new rooms we have keys for
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == n
        