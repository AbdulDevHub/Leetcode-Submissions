class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            studentsInThisRound = len(students)
            for _ in range(studentsInThisRound):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    studentPreference = students.pop(0)
                    students.append(studentPreference)
            if studentsInThisRound == len(students): break
        return len(students)