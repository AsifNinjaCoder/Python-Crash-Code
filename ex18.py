# All the Code Written By Asif date 25th September 2021
# in this code use Function,variable
def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1}, arg2: {arg2}")

def print_two_again(arg1,arg2):
     print(f"arg1:{arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("nothing print")

print_two("Asif","Anowar")
print_two_again("Asif","Anowar")
print_one("First")
print_none()    