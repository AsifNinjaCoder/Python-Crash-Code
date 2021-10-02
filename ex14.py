# All the Code Written By Asif date 24th September 2021
# Communicate With people(Prompting and passing)
from sys import argv

script,user_name= argv
promt = '>'

print(f"Hi{user_name}.I;m good{script}")
print(f"You Know my name!{user_name}")

tags = input(promt)

print("which type laptop do yo have")
laptop = input(promt)
print("Where your Hometown?")
hometown = input(promt)

print(f'''okay, you said {tags} knowabout me, 
currently yo hava {laptop} laptop 
and you said me your hometown is {hometown}.
thanks to talking me Great Day''')