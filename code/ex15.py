# All the Code Written By Asif date 24th September 2021
#  import argv from the sysodue 
from sys import argv
#  get argv command line argv
print("enter your file namme fo read: " )
filename = input("Enter:")
# open th efile using file name to a variable
txt = open(filename)

print(f"Here's your life{filename}: ")
print(txt.read())
txt.close()
print("type the filenam again: ")
# again open new file
file_again = input(">")
# here about your new file
txt_again=open(file_again)
print(txt_again.read())