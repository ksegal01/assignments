# Reads name.txt
with open ('name.txt') as f:
	my_name = f.read()

# construct greeting 

greeting = 'Hello my name is ' + my_name + '.\n'
print(greeting)

# Write that to a file
with open('hello.txt', 'w') as f:
    f.write(greeting)
   