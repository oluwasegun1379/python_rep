class Student:
    """Class representing a student"""
    """
    This program belongs to the category of file management and 
    data persistence. It's designed to manage student information by 
    storing it in a file and providing functionalities to write new 
    student records to the file
    """
    def __init__(self, names, course, level):
        """Initialize a student object"""
        self.names = names
        self.course = course
        self.level = level

    def copyToFile(self):
        """Write student information to a file"""
        with open("file.txt", 'r') as f:
            for line in f:
                if self.names.lower() in line.lower():
                    print("Name already exists")
                    return  # Exit the method if the name already exists
        # If the name doesn't exist, append the student record to the file
        with open("file.txt", "a") as f:
            f.write(f"Name--> {self.names}  course--> {self.course}  level--> {self.level}\n")
            f.close()
            print(f"Student {self.names} has been added to the file")

    def removeFromFile(self):
        """Remove student information from a file"""
        with open("file.txt", "r") as f:
            lines = f.readlines()

        removed = False
        with open("file.txt", "w") as f:
            for line in lines:
                if self.names.lower() not in line.lower():
                    f.write(line)
                else:
                    removed = True
        if removed:
            print(f"Student {self.names} has been removed from the file")
        else:
            print(f"Student {self.names} not found in the file")

    @classmethod
    def readFromFile(cls):
        """Read student information from a file"""
        with open("file.txt", "r") as f:
            f_content = f.read()
            if f_content == "":
                print("File is empty")
            else:
                print(f_content)

# Create a student object
newStudent = Student("Yusuf Oluwatobi", "Mechanical Engineering", "100 Level")

# Write student information to file
newStudent.copyToFile()

# Remove student information from file
#newStudent.removeFromFile()

# Read and print student information from file
Student.readFromFile()