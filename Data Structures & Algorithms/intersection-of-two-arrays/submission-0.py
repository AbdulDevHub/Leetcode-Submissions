class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        finalArr = []
        for nums1 in nums1Set:
            if nums1 in nums2Set: finalArr.append(nums1)
        return finalArr