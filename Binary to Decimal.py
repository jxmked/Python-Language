from math import pow

def bin2Dec(bin, baseOf):
	#Formula: dn-1 ... d3 d2 d1
	power = len(bin)
	sum = 0
	
	#Each binary digits will calculate
	for index in range(0,len(bin)):
		char = int(bin[index]) 
		
		power -= 1 #Decrease Power By 1
		
		ans = char * pow(int(baseOf), power)
		sum += int(ans)
		
		print(char, "*",baseOf,"^ (",power,") =", int(ans))
		#End For Loop
		
	print("Decimal:", sum, "\n")
#End Of bin2Dec Function

#Base Number Set Up
print("Base Number. Default is 2")
BaseOf = 2
x = str(input())	
if x != "":
	BaseOf = x
print("Base Number set to", BaseOf, "\n")
#End Base Number Set Up

#Loop Function For Multiple Translation
while 1:
	s = str(input("Binary Digit :  "))
	
	if s == "":
		break #Stop the Execution
	bin2Dec(s, BaseOf)
