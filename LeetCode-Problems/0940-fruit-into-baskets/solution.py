class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1
        return len(fruits) - left

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         count = defaultdict(int)
#         l, total, res = 0, 0, 0
#         for r in range(len(fruits)):
#             count[fruits[r]] += 1
#             total += 1
#             while len(count) > 2:
#                 f = fruits[l]
#                 count[f] -= 1
#                 total -= 1
#                 l += 1
#                 if not count[f]: count.pop(f)
#             res = max(res, total)
#         return res
