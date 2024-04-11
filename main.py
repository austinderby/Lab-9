#Austin Derby


def encoder(password):
    new_password = ""


    for i in range(len(password)):
        if len(password) != 8:
            print("Invalid password length")
            continue

        elif password.isdigit():
            if "7" <= password[i] <= "9":
                if password[i] == "7":
                    new_password += "0"

                elif password[i] == "8":
                    new_password += "1"

                elif password[i] == "9":
                    new_password += "2"

            elif "0" <= password[i] <= "6":
                if password[i] == "0":
                    new_password += "3"

                elif password[i] == "1":
                    new_password += "4"

                elif password[i] == "2":
                    new_password += "5"

                elif password[i] == "3":
                    new_password += "6"

                elif password[i] == "4":
                    new_password += "7"
                elif password[i] == "5":
                    new_password += "8"

                elif password[i] == "6":
                    new_password += "9"
    return new_password



if __name__ == "__main__":

    while True:
        print("Menu")
        print()
        print("-------------")
        print()
        print("1. Encode")
        print("2. Decode")
        print("3. Quite")
        print()
        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            new_password = encoder(password)
            print("Your password has been encoded and stored!")
            print()

        elif choice == 2:
            decoded_password = decoder(new_password)
            print(f"The encoded password is {new_password}, and the original password is {decoded_password}")
            print()

        elif choice == 3:
            break








