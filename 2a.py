my_input = open("2.txt")
moves = my_input.readlines()
horizontal = 0
depth = 0
for move in moves:
	(direction, spaces) = tuple(map(str, move.split(' ')))
	if direction == "forward":
		horizontal += int(spaces)
	if direction == "down":
		depth += int(spaces)
	if direction == "up":
		depth -= int(spaces)
print(horizontal)
print(depth)
print(horizontal*depth)
