Plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
Students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]


class Garden:
    def __init__(self, diagram, students=None):
        self.row1, self.row2 = diagram.split("\n")
        if students:
            self.students = sorted(students)
        else:
            self.students = Students

    def plants(self, student):
        position = self.students.index(student)
        return [
            Plants[self.row1[position * 2]],
            Plants[self.row1[position * 2 + 1]],
            Plants[self.row2[position * 2]],
            Plants[self.row2[position * 2 + 1]],
        ]
