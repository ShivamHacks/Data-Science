from scipy.optimize import linprog
def simplex(c, A_ub, b_ub, A_eq, b_eq, bounds, opposite):

	"""
	x -> vector that holds all the variables
	c -> Function to be minimized
	dot(A_ub, x) <= b_ub
	dot(A_eq, x) = b_eq
	opposite -> if function is to be maximized, opposite is true because numpy linear programming always minimizes function

	"""

	result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
	if (opposite): result.fun *= -1
	print("Function Value: " + str(result.fun) + " , x=" + str(result.x))

# Problem 1
def problem1():
	print "Problem 1"
	c = [-1.9, -1.5]
	A_ub = [[-2, 1]]
	b_ub = [0]
	x0_bounds = (0, 6400000)
	x1_bounds = (0, 3000000)
	simplex(c, A_ub, b_ub, None, None, (x0_bounds, x1_bounds), True)

def problem2():
	print "Problem 2"
	c = [2, -5]
	A_ub = [[-1, 1]]
	b_ub = [200]
	x0_bounds = (100, 200)
	x1_bounds = (80, 170)
	simplex(c, A_ub, b_ub, None, None, (x0_bounds, x1_bounds), True)

def problem3():
	print "Problem 3"
	c = [-8, -12]
	A_ub = [[6, 8], [10, 20]]
	b_ub = [72, 140]
	x0_bounds = (0, None)
	x1_bounds = (0, None)
	simplex(c, A_ub, b_ub, None, None, (x0_bounds, x1_bounds), True)

def problem4():
	print "Problem 4"
	c = [0.2, 0.3]
	A_ub = [[1, 1], [-8, -12], [-12, -12], [-2, -1]]
	b_ub = [5, -24, -36, -4]
	x0_bounds = (0, None)
	x1_bounds = (0, None)
	simplex(c, A_ub, b_ub, None, None, (x0_bounds, x1_bounds), False)

def problem5():
	print "Problem 5"
	c = [0.5, 0.4, 0.6, 0.55]
	A_ub = [[1, 0, 1, 0], [0, 1, 0, 1]]
	b_ub = [80, 45]
	A_eq = [[1, 1, 0, 0], [0, 0, 1, 1]]
	b_eq = [50, 70]
	x0_bounds = (0, 50)
	x1_bounds = (0, 50)
	x2_bounds = (0, 70)
	x3_bounds = (0, 70)
	simplex(c, A_ub, b_ub, A_eq, b_eq, (x0_bounds, x1_bounds, x2_bounds, x3_bounds), False)

problem1()
problem2()
problem3()
problem4()
problem5()