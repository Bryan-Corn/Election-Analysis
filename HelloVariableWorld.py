# Create a variable called 'name' that holds a string
from telnetlib import theNULL

name = input('What is your name? ')

    #name = "Bob"

# Create a variable called 'country' that holds a string
country = input('In what country do you live? ')

# Create a variable called 'age' that holds an integer
age = input('Please enter your age: ')

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = int(input('How much do you make per hour? '))

work_day = int(input('How many hours per day do you work? '))

# Calculate the daily wage for the user
daily_wage = (hourly_wage * work_day)

# Create a variable called 'satisfied' that holds a boolean
satisfied = bool(input('You are satisfied with your wage. Is this True or False? '))

# Print out "Hello <name>!"
print("Hello "+ name +"!")

# Print out what country the user entered
print("You live in " + country + ".")

# Print out the user's age
print("You are " + str(age) + " years old.")

# With an f-string, print out the daily wage that was calculated
print(f'Your daily wage is {daily_wage}')


# With an f-string, print out whether the users were satisfied
    # print(f'Is the user is satisfied? {satisfied}')

if satisfied == True:
    print("This user is satisfied.")
else:
    print("This user is not satisfied!")
