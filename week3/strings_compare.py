str1 = str(input("Please, enter first string "))
str2 = str(input("Please, enter second string "))

def compare_str(str1, str2):
	if str1 == str2 :
		return 1
	elif len(str1) > len(str2) :
		return 2
	elif str2 == 'learn':
		return 3
	else :
		print ("Nothing to print")


print (compare_str(str1, str2))
