import csv
from academy_app.student.student import Student
import pandas as pd


class Academy:
    courses_offered = ['Python',
                       'Java',
                       'DotNet',
                       'JavaScript',
                       'Node']

    def view_courses(self):
        for i in range(len(self.courses_offered)):
            print(f'{i + 1}. {self.courses_offered[i]}')

    def main_menu(self):
        print("Welcome to our academy")
        print('''
            1. Inquiry about courses..
            2. Register for Course..
            3. Display enrolled students..
            4. Update the student Info
            5. Release Student
            6. Exit
        ''')
        choice = int(input("Please Enter Your Choice:"))
        try:
            if choice == 1:
                print("Our Courses")
                self.view_courses()
                choice = int(input("Enter a choice that you want to learn about:"))
                self.inquiry(choice)
            elif choice == 2:
                print("Register for Course")
                self.view_courses()
                choice = int(input("Enter a choice that you want to register for:"))
                self.register(choice)
            elif choice == 3:
                print("Student info")
                self.display()
                self.main_menu()

            elif choice == 4:
                print("Update Portal")
                call = 'Update'
                self.update(call)

            elif choice == 5:
                print("Release Student..")
                call = "Delete"
                self.update(call)

            elif choice == 6:
                print("Thank You For your visit..")
                return
            else:
                print("Please Enter valid choice")
                self.main_menu()
        except ValueError:
            print("Please Enter a valid number as choice..")
            self.main_menu()

    def inquiry(self, choice_value):
        while choice_value <= len(self.courses_offered):
            if choice_value in range(len(self.courses_offered) + 1):
                print(
                    f'You will learn everything about {self.courses_offered[choice_value - 1]} with a deposit of '
                    f'20000 that you can pay in two installments if you like. It will all be refunded at last')
                self.view_courses()
                choice_value = int(input("Enter a choice that you want to learn about:"))
            else:
                print("Please enter valid choice..")
                self.view_courses()
                choice_value = int(input("Enter a choice that you want to learn about:"))

    def register(self, choice_value):
        if choice_value in range(len(self.courses_offered) + 1):
            course_name = self.courses_offered[choice_value - 1]
            student_name = input("Enter Your Name:")
            deposit = int(input("Enter the deposit you want to submit:"))
            student = Student(student_name, course_name, deposit)
            self.student_data_repository(student)
            print("Student registered Successfully")
            self.main_menu()

        else:
            print("Please enter valid choice..")
            self.main_menu()

    def display(self):
        file = "student.csv"
        df = pd.read_csv(file)
        pd.options.display.max_columns = len(df.columns)
        print(df)

    def update(self, call):
        self.display()
        inp = input("Enter the row you want to update/Delete:")
        lis = []
        with open('student.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                lis += [row]

            for i in lis:
                if i[0] == inp:
                    if call == "Update":
                        name = input("Enter new name:")
                        course = input("Enter new Course:")
                        deposit = int(input("Enter new Deposit:"))
                        remaining = 20000 - deposit
                        i[0] = name
                        i[1] = course
                        i[2] = deposit
                        i[3] = remaining
                        print("Update Successful")
                    elif call == "Delete":
                        lis.remove(i)
                        print("Student released Successfully and refunded...")

            with open('student.csv', 'w', newline='') as new_file:
                writer = csv.writer(new_file, dialect='excel')
                writer.writerow(header)
                writer.writerows(lis)

            self.main_menu()

    def student_data_repository(self, student):
        header = ["Name", "Course", "Deposit_Submitted", "Deposit_Remaining"]
        with open('student.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            if header is False:
                writer.writeheader()
            writer.writerow({'Name': f'{student.name}', 'Course': f'{student.course_enrolled}',
                             'Deposit_Submitted': f'{student.deposit_submitted}',
                             'Deposit_Remaining': f'{student.deposit_remaining}'})


a = Academy()
a.main_menu()
