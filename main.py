def remove_record(name, age, address):
    with open("data.txt", "r") as file:
        lines = file.readlines()
    with open("data.txt", "w") as file:
        for line in lines:
            if (f"full name: {name}   age: {age}   address: {address}\n") not in line:
                file.write(line)

def check(name, age, address):
    with open("data.txt", "r") as file:
        for line in file:
            if (f"full name: {name}   age: {age}   address: {address}\n") in line:
                print("Record found")
                break
        else:
            print("Record not found")
print("File manager")
while True:
    option = input("Enter option add for adding record, remove for removing record, check for checking if your record is in database, or exit to quit :")
    if option == "exit":
        break
    n = int(input(f"How many pieces of data would you like to {option}: "))
    while ((option != "add") and (option != "remove") and (option != "check")):
        option = input("Option picked not valid , Enter option (add for adding record, remove for removing record, check for checking if your record is in database, or exit to quit): ")
        n = int(input(f"Enter how many pieces of data would you like to {option}: "))
    if option == "add":
        for i in range(n):
            qu = str(input("Enter your full name: "))
            age = int(input("Enter age: "))
            last = str(input("Enter address: "))
            with open("data.txt", "a") as file:
                file.write(f"full name: {qu}   age: {age}   address: {last}\n")
        print("successfully added data.")
    elif option == "remove":
        for i in range(n):
            qu = str(input("Enter your full name: "))
            age = int(input("Enter age: "))
            last = str(input("Enter address: "))
            remove_record(qu, age, last)
    elif option == "check":
        for i in range(n):
            qu = str(input("Enter your full name: "))
            age = int(input("Enter age: "))
            last = str(input("Enter address: "))
            check(qu, age, last)
            print("check completed")
    else:
        print("Error")    
