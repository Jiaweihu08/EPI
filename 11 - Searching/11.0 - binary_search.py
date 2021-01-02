import collections
import bisect


def binary_search(arr, x):
	l, r = 0, len(arr)
	while l < r:
		m = (l + r) // 2
		if arr[m] == x:
			return m
		elif arr[m] < x:
			l = m + 1
		else:
			r = m
	return -1


Student = collections.namedtuple('Student', ['name', 'grade_point_average'])


def comp_gpa(student):
	# to perform binary search, the array of elements the search is performed
	# on has to be sorted in ascending order
	return (-student.grade_point_average, student.name)


def search_student(students, target, comp_gpa):
	i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
	return 0 <= i < len(students) and students[i] == target


