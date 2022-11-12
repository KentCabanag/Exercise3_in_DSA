#Write a python program for contact tracing:

#- Display a menu of options
	#Menu:
		# 1 -> Add an item
		# 2 -> Search
		# 3 -> Exit (y/n)
#- Allow user to select item in the menu (check if valid)
#- Perform the selected option
		#- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
				   #Use dictionary to store the info
				   #Use the full name as key
				   #The value is another dictionary of personal information
		#- Option 2: Search, ask full name then display the record
		#- Option 3: Ask the user if want to exit or retry.

#Note: 
#- Your program should be uploaded to github before 4pm
#- Record a demo presenting your program
#- Send the demo or link of demo directly to my messenger

#Example Output:

#Menu:
# 1 -> Add an item
# 2 -> Search
# 3 -> Exit (y/n)

#What do you want to do? (1-3): 1
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890
#Saved!
#What do you want to do? (1-3): 2
#Full name: Danilo Madrigalejos
#Age: 30
#Address: Eastwood
#Phone number: 1234567890 What do you want to do? (1-3): 3
#Exit? n


print("\n\033[34;4mMenu:\033[0m")
print("\033[31;1mPick A number on this\033[0m")
print("\033[34;4m1\033[0m -> Add an item")
print("\033[34;4m2\033[0m -> Search")
print("\033[34;4m3\033[0m -> Exit (y/n)")