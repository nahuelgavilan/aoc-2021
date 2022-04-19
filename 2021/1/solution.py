### PART ONE

with open('input.txt') as f:
	list = f.readlines()	
	input = [int(num.strip()) for num in list] # Cast to int and iterate with a List Comprehesions "For One-liner" to remove the newline.

increases = 0

for i in range(1, len(input)):
	if input[i] > input[i-1]:
		increases += 1

print(increases)

### PART TWO 

increases = 0

for i in range(3, len(input)):
	if (input[i-2] + input[i-1] + input[i]) > (input[i-3] + input[i-2] + input[i-1]):
		increases += 1

print(increases)
