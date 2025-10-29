class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_zero=students.count(0)
        count_one=students.count(1)
        for s in sandwiches:
            if s==0:
                if count_zero==0:
                    break
                count_zero-=1
            else:
                if count_one==0:
                    break
                count_one-=1
        return count_zero+count_one

        