#one line comments

'''
Doc Strings
'''

first_name = "kermit"
last_name = "De Frog"
#print first_name

#response = raw_input("Enter your name")
#print response

birth_year = 1923
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old "

budget = 90

if budget > 100:
    brand = "nike"
    print "Yea! we can buy cool " + brand + "shoes."
elif budget > 50:
    #print "We can at least get some generic sneakers."
    pass
else:
    #print "No cool shoes for me."
    pass

characters = ["leia", "luke","chewy","landos"]
characters.append("obi won")
#print characters[0]


movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}

print movies ["Star Wars"]