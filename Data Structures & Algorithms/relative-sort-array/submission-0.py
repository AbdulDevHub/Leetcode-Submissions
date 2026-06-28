class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        resultArr = []
        appendArr = []
        arr1Frequency = Counter(arr1)
        for num in arr2:
            resultArr.extend([num]*arr1Frequency[num])
        for num in arr1:
            if num not in arr2: appendArr.append(num)
        resultArr.extend(sorted(appendArr))
        return resultArr