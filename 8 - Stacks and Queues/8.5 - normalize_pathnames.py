"""
Given a pathname which can be either an absolute or relative path,
return the shortest equivalent pathname
"""
def shortest_equivalent_pathname(path):
	if not path:
		raise ValueError('Empty string is not a valid pathname.')

	path_names = []
	if path[0] == '/':
		path_names.append('/')

	for token in (token for token in path.split('/')
				if token not in ['.', '']):
		if token == '..':
			if not path_names or path_names[-1] == '..':
				path_names.append(token)
			else:
				if path_names[-1] == '/':
					raise ValueError('Path error')
				path_names.pop()
		else:
			path_names.append(token)
	result = '/'.join(path_names)
	return result[result.startswith('//'):]


dir1 = '/src/bin/./../lib/gcc'
# dir2 = 'scripts//./../scripts/awkscripts/././'
print(shortest_equivalent_pathname(dir1))

