# All the Code Written By Asif date 26th September 2021
#more Use Dictionaries 
tates = {
    'Andhra Pradesh':'AP',
    'Anuranchal Pradesh':'ANP',
    'Assam':'AM',
    'Bihar':'BR',
    'West Bengal':'WB'
}
#BAsic set of States and Cities
cities= {
    'AP':'Amaravati',
    'ANP':'Itangar',
    'AM':'Dispur',
    'BR':'Patna',
    'WB':'Kolkata'

}
# add more cities

cities['MH']='Mumbai'

print('-'*10)
print('MH States Has : ',cities['WB'])

print('-'*10)
print('MH States Has : ',cities['WB'])


print('---'*5)
for state, abbrev in list(states.items()):
    print(f"{states} is abbreviation {abbrev}")

print('---'*5)
for abbrev, city in list(cities.items()):
    print(f"{city} is abbreviation {abbrev}")

print('---'*5)
for city, abbrev in list(cities.items()):
    print(f"{state} state is abbreviated{abbrev}")
    print(f"and has city {cities[abbrev]}")

print('---'*5)

states=states.get('Texas')

if not state:
    print("Sorry no texas")

city = cities.get('WB','Does Not Exist')
print(f"The City For The States 'WB' is:{city}")  
