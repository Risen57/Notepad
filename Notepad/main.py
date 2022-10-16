from os import system

print("Welcome to notepad\n\n")

while True:
    system('clear')
    opt = int(input("What do you want to do?\n1) Read\n2) Clean and write\n3) Append\n4) Exit\n[Enter the serial number]\n:"))

    if opt == 1:
        with open("file.txt", "r") as file:
            print("\n" + file.read())
            input("\nPress Enter to continue to main menu")
    elif opt == 2:
        with open("file.txt", "w") as file:
            context = input("Enter what you want to write:\n")
            file.write("\n" + context)
            input("\nPress Enter to continue to main menu")
    elif opt == 3:
        with open("file.txt", "a") as file:
            context = input("Enter what you want to write:\n")
            file.write(context)
            input("\nPress Enter to continue to main menu")
    elif opt == 4:
        exit()
