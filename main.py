# This is for practice, using the Learn Python The Hard Way book.

#Exercise 4: Variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "available.")
print("There are only", drivers, "available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Exercise 5: More Variables
my_age = 28
print(f"I am {my_age} years old.")

#Exercise 6: Strings and Text
hilarious = False
joke_evaluation = "Isn't the joke so funny?! {}"
print(joke_evaluation.format(hilarious))

#Exercise 7: More Printing
print("The sheep's fleece was as white as {}.".format('snow'))
print("." * 10)

#Exercise 8: Printing, Printing
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("printing", "hello", "world", "in Python"))

#Exercise 9: Printing, Printing, Printing
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec" #the \n seems to make new lines
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
Triple quotation marks
We can type as much as we like with it
""") #any number of lines, to make a new line, just type it like you want it to show

#Exercise 10: What Was That?
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("I am 6'2\" tall.") #escape double-quotes within string,
# tells Python that the specific double-quote isn't end of the string
print('I am 6\'2" tall.') #escape single-quotes within string

#Exercise 11: Asking Questions - input() makes you type in values before proceeding, the end=' ' tells print
# to not end the line with a newline character and go to the next line.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")

#Exercise 12: Prompting People - doing the same thing as Exercise 11 but in a different way
age1 = input("How old are you? ")
height1 = input("How tall are you? ")
weight1 = input("How much do you weigh? ")
print(f"So you're {age1} old, {height1} tall and {weight1} heavy.")