def sum_elements_in_2d_list(group_of_list):
	sum_of_element_list = []
	for elements in group_of_list:
		sum_of_element = 0
		for element in elements:
			sum_of_element = sum_of_element + element
		sum_of_element_list.append(sum_of_element)
	return sum_of_element_list
		

print(sum_elements_in_2d_list([[2, 3, 4], [1, 5, 7], [4, 6, 8]]))		
