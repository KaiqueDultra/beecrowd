def main():
    pacients = []
    
    while True:
        print("----------------------WELCOME TO THE HEALTH CENTER----------------------")
        name = input("\nPlease, enter the name of the pacient: ")
        plan = input("Please, enter the health plan of the pacient: ")
        password = int(input("Please, enter the pacient code: "))
        pacients.append({"name": name, "health plan": plan, "password": password})
        
        print(f"---------------------------------------------------")
        print(f"\nThe next pacient is: {password + 1}")
        
        answer = input("Do you want to continue? (Y/N) ")
        if answer == "Y":
            continue
        elif answer != "N" and answer != "Y":
            answer2 = input("Ivalid option. Please type Y or N to continue.")
            if answer2 == "Y":
                continue
            elif answer2 == "N":
                break
        else:
            break
    
    register = input("\nDo you want to see the pacients registered? (Y/N)")
    if register == "Y":
        code = int(input("Please, enter the pacient code: "))
        for pacient in pacients:
            if pacient['password'] == code:
                print(f"------------------Pacient Information---------------------------------")
                print(f" | - Pacient name: " + pacient['name'] + " |")
                print(f" | - Health Plan: " + pacient['health plan'] + " |")
                print(f" | - Pacient code: " + (str(pacient['password'])) + " |")
                print(f"----------------------------------------------------------------------")
                break
        else:
            print("Pacient not found.")
    else:
        print("Goodbye!")
        
if __name__ == "__main__":
    main()