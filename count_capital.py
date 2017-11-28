userInput= input()
count= {"UPPER": 0}
for i in userInput:
	if i.isupper():
		count["UPPER"]+=1
	else:
		pass
print("Upper case letters count is:", count["UPPER"])

