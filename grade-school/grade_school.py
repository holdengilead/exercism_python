class School:
    def __init__(self):
        self.school = {}

    def add_student(self, name, grade):
        if grade in self.school:
            self.school[grade].append(name)
        else:
            self.school[grade] = [name]

    def roster(self):
        roster = []
        for g in sorted(self.school.keys()):
            roster += sorted(self.school[g])
        return roster

    def grade(self, grade_number):
        return sorted(self.school.get(grade_number, []))
