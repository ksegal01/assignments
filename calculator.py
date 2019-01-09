#calculator functions
def multiply(a,b):
	return a * b
def add(a,b):
	return a + b
def subtract(a,b):
	return a - b
def divide(a,b):
	return a / b
def square(a):
	return a ** 2
def cube(a):
	return a ** 3
def square_n_times(number, n):
	return (number ** 2) * n


print("I'm going to use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

print("I'm going to use the calculator's bonus functions to cube 3")
y = cube(3)
print(y)

print("I'm also going to square the number three 5 times")
z = square_n_times(3,5)
print(z)