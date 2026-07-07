class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = set(nums1)
        answer1Final = []
        answer2 = set(nums2)

        for num in answer1:
            if num in answer2:
                answer2.remove(num)
            else: answer1Final.append(num)

        return [answer1Final, list(answer2)]