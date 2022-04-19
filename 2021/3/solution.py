with open('input') as f:
    list = f.readlines()
    input = [num.strip() for num in list]

## PART ONE
gamma = '' 
epsilon = '' 
zero = 0
one = 0

for num in range(len(input[0])):
    for i in range(num):
        if num[i] == 0:
            zero += 1
        else:
            one += 1
        
    if zero > one:
        gamma += 0
        epsilon += 1
    else:
        gamma += 1
        epsilon += 0
    
    
	
