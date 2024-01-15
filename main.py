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