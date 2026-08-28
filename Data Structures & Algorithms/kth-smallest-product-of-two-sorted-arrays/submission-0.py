class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        prod = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                prod.append(nums1[i] * nums2[j])
        prod.sort()
        return prod[k - 1]