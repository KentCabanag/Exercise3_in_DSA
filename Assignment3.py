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
#Phone number: 1234567890What do you want to do? (1-3): 3
#Exit? n


print("\n\033[34;4mMenu:\033[0m")
print("\033[31;1mPick A number on this\033[0m")
print("\033[34;4m1\033[0m -> Add an item")
print("\033[34;4m2\033[0m -> Search")
print("\033[34;4m3\033[0m -> Exit (yes/no)\n")


while True:
    pick = int(input("\n\033[33;1mSelect a Number on the Menu\033[0m: "))
    if pick == 1:
        print(">> \033[34;4m\033[0mAdd your Information on this\033[0m <<")
        name = input("Full name: ")
        age = int(input("Age: "))
        add = input("Address: ")
        phone = int(input("Phone number: "))
        gender = input("Gender: ")
        Rel = input("Religion: ")
        Nal = input("Nationality: ")
        Info = {
        "Name": name,
        "Age": age,
        "Address": add,
        "Phone": phone,
        "Gender": gender,
        "Religion": Rel,
        "Nationality": Nal,
    }
    elif pick == 2:
        print("\n>> Search an Item <<")
        print("\n\033[34;4mMenu:\033[0m")
        print("\033[31;1mPick an Item you want to search on this\033[0m")
        print("\033[32;1mName, Age, Address, Phone, Gender, Religion, Nationality\033[0m")
        search = input("\nType the Item you want to search: ")
        if search == "Name":
            print("\033[32;1mYour Name is\033[0m:")
            print(Info["Name"] )
        elif search == "Age":
            print("\033[32;1mYour Age is\033[0m: ")
            print(Info["Age"] )
        elif search == "Address":
            print("\033[32;1mYour Address is\033[0m:")
            print(Info["Address"] )
        elif search == "Phone":
            print("\033[32;1mYour Phone Number is\033[0m:")
            print(Info["Phone"] )
        elif search == "Gender":
            print("\033[32;1mYour Gender is\033[0m:")
            print(Info["Gender"] )
        elif search == "Religion":
            print("\033[32;1mYour Religion is\033[0m:")
            print(Info["Religion"] )
        elif search == "Nationality":
            print("\033[32;1mYour Nationality is\033[0m:")
            print(Info["Nationality"] )
            
            
    elif pick == 3:
        y_or_no = input("Do you want to exit?\n Type yes/no: ")
        if y_or_no == "yes":
            break

