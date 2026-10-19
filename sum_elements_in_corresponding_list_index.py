def sum_elements_in_corresponding_list_index(group_of_list):
	sum_of_element_list = []
	for index in range(len(group_of_list)):
		sum_of_element = 0;
		for inner_list in group_of_list:
			sum_of_element = sum_of_element + inner_list[index]
		sum_of_element_list.append(sum_of_element)
	return sum_of_element_list
		
print(sum_elements_in_corresponding_list_index([[2,3,4],[1,5,7],[4,6,8]
]))
		
