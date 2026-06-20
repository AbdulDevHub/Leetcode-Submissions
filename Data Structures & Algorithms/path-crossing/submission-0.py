class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited_nodes = {(0, 0)}
        current_node = (0, 0)
        for direction in path:
            x, y = current_node
            match direction:
                case 'N': current_node = (x, y + 1)
                case 'S': current_node = (x, y - 1)
                case 'E': current_node = (x + 1, y)
                case 'W': current_node = (x - 1, y)
                case _: print("Unknown Direction")
            if current_node in visited_nodes: return True
            visited_nodes.add(current_node)
        return False