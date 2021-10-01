from random import randint


def genarate_random_list(n, z):
	list = []
	for i in range(n):
		list.append(randint(0, z))
	return sorted(set(list))


def binary_search(list, number):
	sorted_list = sorted(set(list))
	counter = 0
	low = 0
	high = len(sorted_list) - 1
	while low <= high:
		mid = (high + low) // 2
		counter += 1
		print('#', counter, '| index =', mid, '| value =',  sorted_list[mid])
		tmp = sorted_list[mid]
		if tmp == number:
			return mid
		if (tmp > number):
			high = mid - 1
		else:
			low = mid + 1
	return None

num = 6

sorted_uniq_list = genarate_random_list(1000, 1000)
print(sorted_uniq_list, '\n')
print('Answer:', binary_search(sorted_uniq_list, num))
