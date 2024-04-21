
class Family:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother

    def greet(self):
        if not self.father or not self.mother:
            return f"Pls enter the father and mother's names"
        else:
            return f"Good morning {self.father} and {self.mother}"

        
class Children(Family):
    def __init__(self, father, mother, num_children, child_names=None):
        super().__init__(father, mother)
        self.num_children = num_children
        self.child_names = []

    def how_many(self):
        if not self.num_children:
            return f"Pls enter the number of children in the family!"
        else:
            return f"{self.father} and {self.mother} has {self.num_children} children"
        
    def add_child(self):
        with open("file2.txt", "w") as f:
            f.write(f"")
            f.write(f"Father's name: {self.father}\nMother's name: {self.mother}\n")
        j = 1
        print(f"Please enter the names of {self.father} and {self.mother}'s children:")
        for i in range(self.num_children):
            child_ = input(f"Enter {j} name: ")
            self.child_names.append(child_)
            with open("file2.txt", "a") as f:
                f.write(f"{j} child: {child_} \n")
                j += 1

        print("Children added successfully.\n")

    def print_children(self):
        i = 1
        for child in self.child_names:
            print(f"{i} child: {child}")
            i += 1


children = Children("John Doe", "Kate Doe", 4)
print(children.greet())
print(children.how_many())

children.add_child()
children.print_children()