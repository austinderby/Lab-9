#Austin Derby


def decoder(new_password):
    password = ""

    for i in range(len(new_password)):
        if "6" <= new_password[i] <= "9":
            if new_password[i] == "6":
                password += "3"

            elif new_password[i] == "7":
                password += "4"

            elif new_password[i] == "8":
                password += "5"

            elif new_password == "9":
                password += "6"

        elif "0" <= new_password[i] <= "6":
            if new_password[i] == "0":
                password += "7"

            elif new_password[i] == "1":
                password += "8"

            elif new_password[i] == "2":
                password += "9"

            elif new_password[i] == "3":
                password += "0"

            elif new_password[i] == "4":
                password += "1"

            elif new_password[i] == "5":
                password += "2"

            elif new_password[i] == "6":
                password += "3"
    return password