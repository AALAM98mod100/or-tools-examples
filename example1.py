from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Variables
# x = model.new_int_var(0, 100, "x")
# y = model.new_int_var(0, 100, "y")
x = model.NewIntVar(0, 100, "x")
y = model.NewIntVar(0, 100, "y")

# Constraints
model.Add(x + y <= 30)

# Objective
model.Maximize(30 * x + 50 * y)

# Solve
solver = cp_model.CpSolver()
status_code = solver.Solve(model)
status_name = solver.StatusName(status_code)

# Print the solver status and the optimal solution.
print(f"{status_name} ({status_code})")
print(f"x={solver.Value(x)},  y={solver.Value(y)}")
