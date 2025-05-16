from ortools.sat.python import cp_model

n = 8
weights = [4,2,8,3,7,5,9,6]
prices = [19,17,30,13,25,29,23,10]
carry_weight = 17
model = cp_model.CpModel()
variables = [model.NewIntVar(0,1,f"x_{i}") for i in range(n)]
bounded_linear_expression = sum([w*v for w,v in list(zip(weights,variables))]) <= carry_weight

model.Add(bounded_linear_expression)

model.Maximize(sum([v*p for v,p in zip(variables,prices)]))

solver = cp_model.CpSolver()
status = solver.Solve(model)

print(status)

# Print the total value achieved
total_value = sum(variables[i] * solver.Value(variables[i]) for i in range(len(variables)))
print(f"Total value: {total_value}")
solver.Value(variables[1]) # test
# Print the total value achieved
total_value = sum(prices[i] * solver.Value(variables[i]) for i in range(len(variables)))
print(f"Total value: {total_value}")
# Print the total weight used
total_weight = sum(weights[i] * solver.Value(variables[i]) for i in range(len(variables)))
print(f"Total weight: {total_weight}/{carry_weight}")
