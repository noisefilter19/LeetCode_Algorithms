#https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [rooms[0]]
        seen = {0: True}
        while stack:
            room = stack.pop(-1)
            for key in room:
                if key not in seen:
                    stack.append(rooms[key])
                    seen[key] = True
        if len(seen) == len(rooms):
            return True
        else:
            return False
