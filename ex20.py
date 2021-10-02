# All the Code Written By Asif date 25th September 2021
#import argv from sys module
from sys import argv
#assign command line argumens to variables
script,input_file=argv

def print_all(f):
     print(f.read())

def rewind(f):
     f.seek(0)

def print_a_line(line_count,f):
     print(line_count,f.readline())

current_file = open(input_file)

print("first let's print whole file\n")

print_all(current_file)

print("Now let's rewind kind of like a tape: ")
rewind(current_file)

print("LET'S PRINT THREE LINES:")

current_line=1

print_a_line(current_line,current_file)

current_line = current_line + 1

print_a_line(current_line,current_file)

current_line = current_line + 1

print_a_line(current_line,current_file)