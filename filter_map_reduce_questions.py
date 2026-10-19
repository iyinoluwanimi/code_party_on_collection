from functools import reduce

def sum_0f_number(numbers):
    sum_of_number_in_numbers = 0
    for number in numbers:
        sum_of_number_in_numbers = sum_of_number_in_numbers + number
    return sum_of_number_in_numbers

def numbers_greater_than_5_checker(number):
    return number > 5
    
sum_0f_number_in_tuple = list(map(sum_0f_number,[(1, 2), (3, 4), (5, 6)]))
print(sum_0f_number_in_tuple)

numbers_greater_than_5_in_sum_0f_number_in_tuple = list(filter(numbers_greater_than_5_checker,sum_0f_number_in_tuple))
print(numbers_greater_than_5_in_sum_0f_number_in_tuple)



    
def remove_non_numeric_string(string):
    return string.isdigit()
def convert_string_to_integer(string):
    return int(string)
def addition_0f_number(first_number,second_number):
    return first_number + second_number
    
numeric_string = list(filter(remove_non_numeric_string,['123', '456', '789', 'abc', 'def']))
print(numeric_string)
list_converted_to_integer = list(map(convert_string_to_integer,numeric_string))
print(list_converted_to_integer)
print(reduce(addition_0f_number,list_converted_to_integer))
