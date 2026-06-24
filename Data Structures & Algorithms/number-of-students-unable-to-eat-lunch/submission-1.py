class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)
        for sandwich in sandwiches:
            if studentCount[sandwich] > 0: studentCount[sandwich] -= 1
            else: break
        return studentCount[0] + studentCount[1]