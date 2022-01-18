class Student:
    def __init__(self, first, last, courses=None):
        self.first_name =first
        self.last_name = last
        if courses== None:
            self.courses=[]
        else:
            self.courses= courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("that class is already added")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print("cannot be removed since not enrolled")

    def __str__(self):
        return "First name: {self.first_name.capitalize()} \n Last name: {self.last_name.capitalize()}\n Courses: {', '.join(self.courses)}"

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        pass

    def __eq__(self, other):
         return self.last_name == other.last_name and self.first_name == other.first_name

    def find_in_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                first_name, last_name, courses=Student.prep_record(line.strip())
                student_read_in=Student(first_name, last_name, courses)
                if self==student_read_in:
                    return True
            return False

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name=first_name+' '+last_name
        courses=','.join(courses)
        return full_name+':'+courses

    def add_to_file(self, file_name):
        if self.find_in_file(file_name):
            return "Record alrady exists"
        else:
            record_to_add= Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(file_name, 'a+') as to_write:
                to_write.write(record_to_add+ '\n')
            return 'record added'

    @staticmethod
    def prep_record(line):
        line= line.split(":")
        first_name, last_name= line[0].split(',')
        courses=line[1].rstrip().split(',')
        return first_name, last_name, courses



class StudentAtleate(Student):

    def __init__ (self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)
        self.sport=sport


courses=['c', 'phyton']
file_name= 'data-2.txt'
susan= StudentAtleate('susan', 'heffley', courses, 'rowing')
print(susan.sport)
print(isinstance(jane, Student))
