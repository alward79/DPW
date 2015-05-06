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

#print movies ["Star Wars"]


#while loop
'''
i = 0
while i <9:
    print "The count is", i
    i = i+1
'''
#for Loop
'''
for i in range (0,10):
    print "The count is", i
    i = i+i
'''
#foreach loop
rappers = ["Tupac", "Nas","Biggis Smalls"]
for r in rappers:
    #print "One of the best rappers is " + r
    pass

#functions
x = 2
def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40);
#print "My area is "+  str(a) + "sqft"
print a

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<DOCTYPE HTML>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message = message.format(**locals())
print message