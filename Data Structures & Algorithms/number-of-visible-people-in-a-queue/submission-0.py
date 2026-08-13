class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        visible = []
        for i in range(len(heights)):
            maximum = count = 0
            for j in range(i + 1, len(heights)):
                if min(heights[i], heights[j]) > maximum:
                    count += 1
                maximum = max(maximum, heights[j])
            visible.append(count)
        return visible