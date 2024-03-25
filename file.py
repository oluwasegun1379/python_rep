class Student:
    """Class representing a student"""
    """
    This program belongs to the category of file management and 
    data persistence. It's designed to manage student information by 
    storing it in a file and providing functionalities to write new 
    student records to the file
    """

    numberOfStudents = 1  # Class variable

    def __init__(self, names, age, score):
        """Initialize a student object"""
        self.names = names
        self.age = age
        self.score = score

    def copyToFile(self):
        """Write student information to a file"""
        with open("file.txt", 'r') as f:
            for line in f:
                if self.names.lower() in line.lower():
                    print("Name already exists")
                    return  # Exit the method if the name already exists
                else:
                    Student.numberOfStudents += 1   # Increment numberOfStudents
        # If the name doesn't exist, append the student record to the file
        with open("file.txt", "a") as f:
            f.write(f"({Student.numberOfStudents}) Name--> {self.names}  age--> {self.age}  score--> {self.score}\n")

    @classmethod
    def readFromFile(cls):
        """Read student information from a file"""
        with open("file.txt", "r") as f:
            f_content = f.read()
            print(f_content)

# Create a student object
newStudent = Student("Yusuf Oluwatobi", 25, 90.0)

# Write student information to file
newStudent.copyToFile()

# Read and print student information from file
Student.readFromFile()