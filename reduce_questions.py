from functools import reduce

def sum_0f_number(first_number,second_number):
    return first_number + second_number
    
print(reduce(sum_0f_number,range(1,51)))


def maximum_number(first_number,second_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number
    
print(reduce(maximum_number,[3, 5, 9, 2, 8]))

def concatenate_string(first_string,second_string):
    return first_string + " " + second_string
    
print(reduce(concatenate_string,['I', 'love', 'Python']))

def square_number(number):
    return number ** 2
    
def product_0f_number(first_number,second_number):
    return first_number * second_number
    
square_list = list(map(square_number,[1, 2, 3, 4]))
print(square_list)
print(reduce(product_0f_number,square_list))
