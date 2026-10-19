def uppercase_converter(word):
    return word.upper()
    
uppercase = list(map(uppercase_converter,['python', 'java', 'c++']))
print(uppercase)

def square_number(number):
    return number ** 2
    
square_list = list(map(square_number,range(1,11)))
print(square_list)

def capitalize_first_letter(word):
    return word.capitalize()
    
capitalized_first_letter_list = list(map(capitalize_first_letter,['john', 'mary', 
'steve']))
print(capitalized_first_letter_list)


def tax_of_10_percent_inclusion(amount):
    return amount + (0.1 * amount)
    
price_with_tax_list = list(map(tax_of_10_percent_inclusion,[100, 200, 300]))
print(price_with_tax_list)
