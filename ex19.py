# All the Code Written By Asif date 25th September 2021
# here i make function with two parameters
def chease_and_crackers(ches_count,boxes_of_crackers):
    print(f"you have{ches_count}")
    print(f"You have{boxes_of_crackers}")

print("we can just give the function numbers ") 
chease_and_crackers(10,50) # Here i add parameter as integer value

print("Or, We can use variables from our Scripts: ")

amount_of_chese = 20 # Here create a new variable 
amount_of_crackers = 50 # Here create a new variable 

chease_and_crackers(amount_of_chese,amount_of_crackers) # Here change the parameter of function

print("we can even do math inside too:")
chease_and_crackers(10+20,5+3) # Here in parameters add two integers 

print("And we can combine the two variables and math: ")
chease_and_crackers(amount_of_chese+50, amount_of_crackers+90) # Here adding varaible + integer 

