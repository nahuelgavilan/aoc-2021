with open('input') as f:
	list = f.readlines()
	input = [text.strip() for text in list]

## PART ONE

position = 0
depth = 0

for move in input:
	if 'down' in move:
		depth += int(move.split(' ')[-1]) 
	elif 'up' in move:
		depth -= int(move.split(' ')[-1])
	else:
		position += int(move.split(' ')[-1])

res = position * depth
print (res)

## PART TWO

aim = 0
position = 0 
depth = 0

for move in input:
    if 'down' in move:
        aim += int(move.split(' ')[-1])
    elif 'up' in move:
        aim -= int(move.split(' ')[-1])
    else:
        position += int(move.split(' ')[-1])
        depth += int(move.split(' ')[-1]) * aim

res = position * depth
print (res)
