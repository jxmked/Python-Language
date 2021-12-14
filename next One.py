from math import pow

def nextOne(arr, min, max):
    for index in range(0, len(arr)):
    		if len(arr) <= index + 1:
    			return arr
    		
    		if arr[index] >= max + 1:
    			arr[index + 1] += 1
    			arr[index] = min
    		else:
    			#Break the iteration when next array is 
    			#not reach the max value. Save Time
    			return arr

def stopWhen(arr, w):
	for i in arr:
		if not i >= w:
			#Break iteration if a single value of an array
			#is not reach the max value. Save time
			return False
	return True

################
def addZero(i, x):
	txt = ""
	i = str(i)
	for j in range(0, len(str(int(x))) - len(i)):
		txt += "0"
	return txt + i
	
def replace(arr, rep):
	tmp = []
	for index in arr:
		tmp.append(rep[index])
	return tmp




#Array length. 
arrLen = 4

min = 0
max = 3

rep ={0  : " a ",
1  : " b ",
2  : " c ",
3  : " d ",
4  : " e ",
5  : " f ",
6  : " g ",
7  : " h ",
8  : " i ",
9  : " j ",
10  : " k ",
11  : " l ",
12  : " m ",
13  : " n ",
14  : " o ",
15  : " p ",
16  : " q ",
17  : " r ",
18  : " s ",
19  : " t ",
20  : " u ",
21  : " v ",
22  : " w ",
23  : " x ",
24  : " y ",
25  : " z "
}

#Replace output with corresponding letters
repFlag = False

#Print output array in reverse. Best for Binary look
outputRev = True

arr = []
for x in range(0, arrLen):
	arr.append(min)

#Get the length of last count of integer. 
#For adding a "0" at the begging of line number
calc = pow((1 + max) - min, arrLen)

i = 1

while 1:
	#join() method in use
	tmp = arr
	if outputRev:
		tmp = arr[::-1] #Don't make any changes on lrocessing array'
	
	if repFlag:
		arr2 = " ".join(replace(tmp, rep))
	else:
		arr2 = " ".join([str(val) for val in tmp])
		
	print(addZero(i,calc), "—", arr2)
	
	if arr[len(arr) - 1] >= max:
			if stopWhen(arr, max):
			     #Stop when all Value in array reaches the max value
			     break
	
	arr[0] += 1
	i += 1
	if arr[0] >= max:
	   nextOne(arr, min, max) #Increase the next value in an array 
