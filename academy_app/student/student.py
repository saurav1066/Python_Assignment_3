class Student:
    def __init__(self, name, course_enrolled, deposit_submitted):
        self.name = name
        self.course_enrolled = course_enrolled
        self.deposit_submitted = deposit_submitted
        self.total_deposit = 20000
        self.deposit_remaining = self.total_deposit - deposit_submitted



