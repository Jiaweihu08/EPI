"""
Given an array of object with many repetitions, return the array with
same target field appearing one after another
"""
import collections


Person = collections.namedtuple('Person', ('name', 'age'))


# def group_by_age_naive(people):
	# people.sort(key=lambda person: person.age)
	# return people

	# age_to_person = collections.defaultdict(list)
	# for person in people:
	# 	age_to_person[person.age].append(person)
	# return list(age_to_person.values())


def group_by_age(people):
	age_to_count = collections.Counter([person.age for person in people])
	age_to_offset, offset = {}, 0
	for age, count in age_to_count.items():
		age_to_offset[age] = offset
		offset += count

	while age_to_offset:
		from_age = next(iter(age_to_offset))
		from_idx = age_to_offset[from_age]
		to_age = people[from_idx].age
		to_idx = age_to_offset[to_age]
		people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
		age_to_count[to_age] -= 1
		if age_to_count[to_age]:
			age_to_offset[to_age] = to_idx + 1
		else:
			del age_to_offset[to_age]



people = [Person('George', 14), Person('John', 12), Person('Andy', 11),
		Person('Jim', 13), Person('Phil', 12), Person('Bob', 13),
		Person('Chip', 13), Person('Tim', 14)]

group_by_age(people)
print(people)