my_input = open("1.txt")
depths = my_input.readlines()
#depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
answer = 0
def sum_window(idx):
	return int(depths[idx]) + int(depths[idx+1]) + int(depths[idx+2])
for idx, depth in enumerate(depths):
	if idx + 3 >= len(depths):
		continue
	if sum_window(idx+1) > sum_window(idx):
		answer += 1
print(answer)	
