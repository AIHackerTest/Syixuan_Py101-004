# -*- coding: utf-8 -*-
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
    
# create a basic set  of states and some cities in them
cities = {
    'CA': 'San Franciso',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print ('-'*10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

# print some states
print ('-'*10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict

print ('-' * 10)
print ("Michigan has: ",cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print ('-' * 10)
for state, abbrev in cities.items():
    print ("%s tha is abbreviated %s" % (state, abbrev))
    
# print every city in state
print ('-' * 10)
# 返回列表，被 for 引用
for abbrev, city in states.items():
    print ("%s has city %s" % (abbrev, city))
    
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print ("Sorry, no Texas.")
    
# get a city with default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)