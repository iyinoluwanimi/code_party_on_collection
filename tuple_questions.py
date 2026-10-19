tuple_of_numbers = (2,4,6,8)
print(tuple_of_numbers)
tuple_of_numbers += (10,)
print(tuple_of_numbers)

numbers = (1,2,[3,4],5)
print(numbers)
numbers[2][1] = 99
print(numbers)

tuple_of_strings = ('apple','banana','cherry')
print(tuple_of_strings)
tuple_of_strings_as_list = list(tuple_of_strings)
print(tuple_of_strings_as_list)
tuple_of_strings_as_list.append('mango')
print(tuple_of_strings_as_list)
tuple_of_strings_as_list_back_to_tuple = tuple(tuple_of_strings_as_list)
print(tuple_of_strings_as_list_back_to_tuple)



tuple_to_unpack = (10,20,30,40)
print(tuple_to_unpack)
variable_a = tuple_to_unpack[0]
print(variable_a)
variable_b = tuple_to_unpack[1]
print(variable_b)
variable_c = (tuple_to_unpack[2],tuple_to_unpack[3])
print(variable_c)
