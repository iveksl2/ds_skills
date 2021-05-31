#   https://www.youtube.com/watch?v=qa4trkLfvwQ
#   PuLP Tutorial
#   Mohammad T. Irfan
#   Bowdoin College
from pulp import *

#Elementary features:
lp = LpProblem("Bakery_Problem", LpMaximize)

#Define variables
x1 = LpVariable(name="Bowdoin_log", lowBound=0, cat="Integer")
x2 = LpVariable(name="Chocolate_cake", lowBound=0, cat="Integer")

#Add the objective function
lp += 10 * x1 + 5 * x2
print(lp.objective)

# Add the constraints - #optional to put custom name
lp += (5 * x1 + x2 <= 90, "oven_constraint")
lp += (x1 + 10 * x2 <= 300, "food_processor_constraint")
lp += (4 * x1 + 6 * x2 <= 125, "boiler_constraint")
print(lp.constraints)

# Solve the LP
status = lp.solve(PULP_CBC_CMD(msg=False)) #supress messages
print("Status:", status) #1:optimal, 2:not solved, 3:infeasible, 4:unbounded, 5:undef

#Print solution
for var in lp.variables():
    print(var, "=", value(var)) # Value is overwritten method in PulP
print("OPT =", value(lp.objective))

# ------------ Advanced features - Larger scale ------------ 

lp = LpProblem("Bakery_Problem", LpMaximize)

#Define a dictionary of variables keyed by "indices"
var_keys = [1,2] 
x = LpVariable.dicts("Bakery_item", var_keys, lowBound=0, cat="Integer")
print(x)

#Add the objective function
lp += 10* x[1] + 5 * x[2] # notice the bracket notation

# Add the constraints
# lp += (5 * x[1] + x[2] <= 90, "oven_constraint")
# lp += ( lpSum( [5*x[1], x[2]] ) <= 90  ) # Same thing as above with succint notation

lp += (x[1] + 10 * x[2] <= 300, "food_processor_constraint")
lp += (4 * x[1] + 6 * x[2] <= 125, "boiler_constraint")

#Rewrite the first constraint:
coeff = [5, 1] #may come from a file in real world
coeff_dict = dict( zip(var_keys,coeff) )
lp += ( lpSum(coeff_dict[i] * x[i] for i in var_keys) <= 90) # 1st constraint

# Solve the LP
status = lp.solve(PULP_CBC_CMD(msg=0))
print("Status:", status)

#Print solution
for var in lp.variables():
    print(var, "=", value(var))
print("OPT =", value(lp.objective))
