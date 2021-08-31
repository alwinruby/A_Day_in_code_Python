# Goodnight program

from time import *
from datetime import date as current_date

# Function definition
def epic_test(activity_number, happy_value):
    if activity_number > 5 and happy_value == True:
        global epic_day
        epic_day = True

full_date = current_date.today()

number_of_activities = 15
very_happy = True
epic_day = None

print("In 5 seconds, it will be time for bed.")
sleep(5)

epic_test(number_of_activities, very_happy)

if epic_day:
    print("Today, " + str(full_date) + ", was like a fairy tale!")

print("Goodnight!")
