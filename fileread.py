def contents(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            result.append(line)

    return result

source_path = input()
file_contents = contents(source_path)

max_len = [0] * 6
line_cnt = len(file_contents)

for line in file_contents:
	seperated_values = line.split(',')
	for i in range(len(seperated_values)):
		max_len[i] = max(max_len[i], len(seperated_values[i]))

full_len = 0

for i in range(6):
	full_len += max_len[i]

for line in file_contents:
	print('+', end = '')
	for j in range(full_len):
		print('-', end = '')
	print('+')
	seperated_values = line.split(',')
	for i in range(len(seperated_values)):
		print('|', end = '')
		print(seperated_values[i], end = '')
		for j in range(max_len[i] - len(seperated_values[i])):
			print(' ', end='')
	print('|')

print('+', end = '')
for i in range(full_len):
	print('-', end = '')
print('+', end = '')

