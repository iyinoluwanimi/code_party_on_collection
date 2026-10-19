def even_number_checker(number):
	if number % 2 == 0:
	    return True
	else:
	    return False
	    
	    
even_number_list = list(filter(even_number_checker,range(1,21)))

print (even_number_list)

def words_longer_than_5_checker(word):
    return len(word) > 5
        
list_of_words_with_more_than_5_characters = list( filter(words_longer_than_5_checker,['cat','elephant','tiger','lion']))

print(list_of_words_with_more_than_5_characters)


def tuple_in_list_first_value_checker(collection):
    return collection[0] > 2
           
            
tuple_with_first_value_greater_than_2 = list(filter(tuple_in_list_first_value_checker,[(1,'A'),(4,'B'),(2,'C')]))
print(tuple_with_first_value_greater_than_2)


def number_divisible_by_3_and_5_checker(number):
    return number% 3 == 0 and number% 5 == 0
    
number_divisible_by_3_and_5 = list(filter(number_divisible_by_3_and_5_checker,range(1,51)))
print(number_divisible_by_3_and_5)



def palindrome_checker(word):
    return word == word[::-1]
    
palindrome = list(filter(palindrome_checker,['level','world','madam','python']))
print(palindrome)
    
