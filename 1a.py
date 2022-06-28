my_input = open("1.txt")
depths = my_input.readlines()
#depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
answer = 0
for idx, depth in enumerate(depths):
	if idx == 0:
		continue
	if int(depths[idx]) > int(depths[idx-1]):
		answer += 1
print(answer)	
