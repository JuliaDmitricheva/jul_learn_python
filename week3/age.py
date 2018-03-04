print ("This is age check script.")
age = input("Enter your age, please. ")

try:
	int_age = int(age)

except:
	print (" Age not integer.  Try one more time.  Exiting.")
	exit()

if int_age <= 3 :
	print (" Oh! You so young!")
elif int_age <= 6 :
	print (" You should go to the kindergarden.")
elif int_age <= 17 :
	print (" You go to school.")
elif int_age <= 22 :
	print (" You are student, pehaps.")
elif int_age <= 60:
	print (" You are worker")
else:
	print ("it's time for you to retire")