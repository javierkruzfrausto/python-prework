# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("javierkruzfrausto")
               
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for j in range(1, 101, 2):
        print(j)
               
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    for i in a_list:
        print(max(a_list))

list = [1,2,3,4,5,6,7,8,9]
max_num_in_list(list)
               
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    return (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0
               
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

a_list = [1,2,3,4,5,6,7]

def is_consecutive(a_list):
    consecutive: False
    for n in range(1, len(a_list)):
        if (a_list[n]) != a_list[n-1]:
            consecutive = True
        else:
            consecutive = False
        return consecutive

print(is_consecutive(a_list))
