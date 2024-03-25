class QuadraticEquationSolver:
    def square(self, x):
        """Compute the square of a number."""
        return x * x

    def sqrt(self, x):
        """Compute the square root of a number."""
        return x ** 0.5

    def divided(self, x, y):
        """Divide two numbers."""
        return x / y

    def solve_quadratic(self, a, b, c):
        """Solve a quadratic equation."""
        discriminant = self.square(b) - 4 * a * c
        root1 = self.divided(-b + self.sqrt(discriminant), 2 * a)
        root2 = self.divided(-b - self.sqrt(discriminant), 2 * a)
        return root1, root2

# Create an instance of the QuadraticEquationSolver class
solver = QuadraticEquationSolver()

# Coefficients of the quadratic equation
a = 1
b = -5
c = 6

# Solve the quadratic equation
root1, root2 = solver.solve_quadratic(a, b, c)

# Print the roots
print("Root 1:", root1)
print("Root 2:", root2)