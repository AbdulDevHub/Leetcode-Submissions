class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        user_history = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_history[u].append((t, w))
            
        # Global map to track: { (site1, site2, site3): unique_user_count }
        pattern_counts = defaultdict(int)
        for u in user_history:
            user_history[u].sort(key=lambda x: x[0]) # Sort user's visits by time
            sites = [web for time, web in user_history[u]]
            user_unique_patterns = set(combinations(sites, 3))
            for pattern in user_unique_patterns:
                pattern_counts[pattern] += 1
                
        # Find winner with highest score (and lexicographical tie-breaker)
        best_pattern = None
        max_score = 0
        for pattern, count in pattern_counts.items():
            if count > max_score:
                max_score = count
                best_pattern = pattern
            elif count == max_score:
                # If there's a tie, pick the lexicographically smaller pattern
                if best_pattern is None or pattern < best_pattern:
                    best_pattern = pattern
                    
        return list(best_pattern)