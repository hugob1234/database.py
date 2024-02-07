def remove_record(name, age, address):
    with open("data.txt", "r") as file:
        lines = file.readlines()
    with open("data.txt", "w") as file:
        for line in lines:
            if f"full name: {name}   age: {age}   address: {address}\n" not in line:
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
option = input("Enter option (1 for adding record, 2 for removing record): ")

if option == "1":
    qu = str(input("Enter your full name: "))
    age = int(input("Enter age: "))
    last = str(input("Enter postcode: "))
    with open("data.txt", "a") as file:
        file.write(f"full name: {qu}   age: {age}   address: {last}\n")
elif option == "2":
    qu = str(input("Enter your full name: "))
    age = int(input("Enter age: "))
    last = str(input("Enter postcode: "))
    remove_record(qu, age, last)
elif option == "3":
    qu = str(input("Enter your full name: "))
    age = int(input("Enter age: "))
    last = str(input("Enter postcode: "))
    check(qu, age, last)
else:
    print("EERRRRRRRROOOOORRRRRRR")
    
