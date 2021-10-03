# All the Code Written By Asif date 26th September 2021
#Use List In This Code 
ten_things ="Apple Orange crows telephone light Sugar"

print("Wait there are not 10 things in that list. let's fix that")

stuff =  ten_things.split(' ')

more_stuff = ["day","night","song","Frisbee","corn","Banana","Girl"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now. ")

print("there we go: ", stuff) 

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print(' '.join(stuff))
print('#'.join(stuff[3:5]))