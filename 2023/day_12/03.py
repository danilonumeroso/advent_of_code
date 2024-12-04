import asyncio
from minizinc import Instance, Model, Solver

# Load the model from the file
model = Model("./aoc.mzn")

# Create a solver configuration
solver = Solver.lookup("gecode")

# Create an instance of the model
instance = Instance(solver, model)

# Set the instance parameters
instance["length"] = 16
instance["groups"] = [2, 1, 2, 3]

# Solve the problem and count the solutions
sols = instance.solve(all_solutions=True)
print("Number of solutions:", len(sols))