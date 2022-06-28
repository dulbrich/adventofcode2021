my_input = open("2.txt")
moves = my_input.readlines()
aim = 0
horizontal = 0
depth = 0
for move in moves:
	(direction, spaces) = tuple(map(str, move.split(' ')))
	if direction == "forward":
		horizontal += int(spaces)
		depth += aim * int(spaces)
	if direction == "down":
		aim += int(spaces)
	if direction == "up":
		aim -= int(spaces)
print(horizontal)
print(depth)
print(horizontal*depth)
