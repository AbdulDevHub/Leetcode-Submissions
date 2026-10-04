class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build adjacency list representation for the undirected tree
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur: int, par: int) -> int:
            time = 0
            for child in adj[cur]:
                # Skip the parent edge to prevent infinite recursion
                if child == par: continue
                # Recursively calculate total round-trip time needed for subtree
                child_time = dfs(child, cur)

                # Traversal cost is 2 seconds (1 down, 1 back up).
                # Only traverse to 'child' if its subtree contains an apple 
                # (child_time > 0) or the child node itself holds an apple.
                if child_time > 0 or hasApple[child]: time += 2 + child_time
            return time

        # Start DFS from root node 0 with dummy parent -1
        return dfs(0, -1)