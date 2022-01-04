import math


"""def digitize(n):
	convert_string = str(n)
	number_list = []
	for i in convert_string:
		number_list.append(i)
	number_list.reverse()
	result = []
	for i in number_list:
		result.append(int(i))
	return result
	
digitize(123456789) """



"""def pipe_fix(nums):
	max_num = max(nums)
	min_num = min(nums)
	output_list = []

	output_list.append(min_num)

	counter = min_num
	while counter != max_num:
		counter += 1
		output_list.append(counter)

	return output_list


output = pipe_fix([-1, 4])
print(output) """

"""def pattern(n):
	result = ""
	stars = 0
	second_number = 1

	for i in range(n):
		if stars == 0:
			result += "1\n"
		elif i == n - 1:
			result += "1" + "*" * stars + str(second_number)
		else:
			result += "1" + "*" * stars + str(second_number) + "\n"
		second_number += 1
		stars += 1	

	print(result)
	return result


pattern(10) """
# "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")"


"""def sum_average(arr):
    result = 0
    for i in range(len(arr)):

        sum_array = 0

        for element in arr[i]:
            sum_array += element
        result += sum_array / len(arr[i]) 
    return  math.floor(result)"""
			
# sum_average([[1, 2, 2, 1], [2, 2, 2, 1]])

"""def monkey_count(n):
	result = []
	count = 1

	while count != n + 1:
		result.append(count)
		count += 1
	print(result)
	return result

monkey_count(10) """








"""ef max_tri_sum(numbers):
	no_duplicate = []
	for number in numbers:
		if number not in no_duplicate:
			no_duplicate.append(number)
	no_duplicate.sort()
	no_duplicate.reverse()
	
	count = 0
	sum_numbers = 0
	while count != 3:
		sum_numbers += no_duplicate[count]
		count += 1
	
	return sum_numbers
	





max_tri_sum([3,2,6,8,2,3])"""




"""def reverse_list(l):
	l.reverse()
	return l

reverse_list([1,2,3,4])"""



"""def add_length(str_):
	result = []
	splitted_words = str_.split(" ")

	for word in splitted_words:
		result.append(word + " " + str(len(word)))
	
	print(result)
	return result


add_length('you will win')"""

"""def sort_by_length(arr):
	result_list = []
	min_list = []
	count = 0
	while count != len(arr):
		min_list.append(len(arr[count]))
		count += 1

	counter = 0
	while len(arr) != 0:
		if len(arr[counter]) == min(min_list):
			result_list.append(arr[counter])
			arr.remove(arr[counter])
			min_list.remove(min(min_list))
			counter = 0
		else:
			counter += 1
	
	print(result_list)	
	return result_list

#sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"])
sort_by_length(["beg", "life", "i", "to"]) """



"""def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

print(array_plus_array([1, 2, 3], [4, 5, 6]))"""


"""def get_age(age):
    return int(age[0])


get_age("5 years old")"""



"""def minimum(arr):
	return min(arr)

def maximum(arr):
	return max(arr)"""


# !!!!!!!!!!!!!!!!
def nth_even(n):
	result = 2 * n - 2
	return result

res = nth_even(100) # 0 2 4 6
#print(res)

# !!!!!!!!!!!!!!!!



"""def alphabetic(s):
    sorted_list = sorted(s)
    splitted_list = []
    for letter in s:
        splitted_list.append(letter)
    
    print(sorted_list)
    print(splitted_list)
    if splitted_list == sorted_list:
        return True
    return False


result = alphabetic("kata")
print(result)"""



"""def is_sorted_and_how(arr):
	result = ""
	if arr == sorted(arr):
		result = "yes, ascending"
	elif arr == sorted(arr)[::-1]:
		result = "yes, descending"
	else:
		result = "no"
	print(result)
	return result


is_sorted_and_how([15, 7, 3, -8])
is_sorted_and_how([1,2])
is_sorted_and_how([4, 2, 30]) """
