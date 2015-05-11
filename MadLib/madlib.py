'''
Name: Angelena Ward
Date: May 6, 2015
'''

#array to hold input from user answers from numbers.append.
numbers = []

#variables with raw_input for the user to answer.
female = raw_input("Enter a female name. ")
male = raw_input("Enter a male name. ")
name = raw_input("Enter your name. ")
state = raw_input("Enter your state. ")
color = raw_input("Enter your favorite color. ")
animal = raw_input("Name an animal. ")
food = raw_input("Enter your favorite food. ")
liquid = raw_input("Enter a liquid. ")
verb = raw_input("Enter any verb ending in ing! ")
verb1 = raw_input("Enter another verb ending in ing! ")
noun = raw_input("Enter any noun! (plural) ")
year = raw_input("Enter the year you were born. ")

#numbers.append will add the raw_input to the numbers array
numbers.append(raw_input("Enter a number from 1 to 15. "))
numbers.append(raw_input("Enter any number. "))
numbers.append(raw_input("Enter any number. "))

#dictionary to associate fun with road trip and boring with jogging?
activity = dict()
activity = {"fun": "road trip", "boring": "jogging"}

print "We decided it might be more fun to go on a " + activity["fun"] + " than it would be to go " + activity["boring"]

message = '''\nMy name is {name} and my friends {male}, {female} and I went on a road trip to {state}. "You will love {state}" said {male} and I did. "It's famous for its wild {animal}", the {color} buildings downtown, and it's {verb} hills." I packed plenty of {food} for the ride, it will probably take {numbers[0]} hours to get there. On the car ride down we sang {numbers[1]} bottles of {liquid} on the wall, then we counted the number of {noun} we saw {verb1} on the side of the road, and we counted {numbers[2]} {noun} {verb1}. This was a great trip.'''
message = message.format(**locals())
print message

#if statement will run as long as numbers[0} is 15 otherwise it will go to the else statement.
if int(numbers[0]) <= 15:
    print "\n" + numbers[0] + " hour trip. Not bad."
elif numbers[0] > 15:
    print "\nWow! " + numbers[0] +" hours, that was long trip "
#conditonal and loop. The while loop will run as long as numbers[1] is less than 20 otherwise it will print the else statement.
if int(numbers[1]) <= 20:
    i=0
    x = int(numbers[1])
    while i < x:
        print "\n" +str(x) + " bottles of "+ liquid + " on the wall"
        x = x-1
else:
    print "\nWow! That must have been a long trip, you guys sang " +numbers[1]+ " bottles of " +liquid+ " on the wall."

#function to calculate age from year(raw_input)-current year(2015)
def calc_age(born, now):
    age = now - born
    return age
yourAge = calc_age(int(year), 2015)

print "\nMy name is " + name + " and I'm " +str(yourAge)
