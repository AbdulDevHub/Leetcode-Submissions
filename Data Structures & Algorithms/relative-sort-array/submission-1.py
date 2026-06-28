class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        resultArr = []
        arr1Frequency = Counter(arr1)
        for num in arr2:
            resultArr.extend([num]*arr1Frequency[num])
            del arr1Frequency[num]
        for num in sorted(arr1Frequency.keys()):
            resultArr.extend([num] * arr1Frequency[num])   
        return resultArr