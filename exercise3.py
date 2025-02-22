#  Zion Needham (Ultimate-Shoe)
#  W25 COP2002.0M1.
#  02/06/2025
#  MAC Manufacturer Identification Program
#  Simple Python program to give a user the manufacturer name based on the MAC address they input

def main():
    # Introduction to the program and prompts user for MAC  address .
    print("MAC Manufacturer Program \n-------------------------\n")
    prompt = "Enter the first 6 hex values of the MAC address (format as XX:XX:XX): "
    user_MAC = input(prompt)

    # Basic if/elif to check the user's input MAC address with the proper manufacturer.
    if user_MAC == "00:00:17":
        manufacturer = "Oracle"

    elif user_MAC == "00:07:E9":
        manufacturer = "Intel Corporation"

    elif user_MAC == "04:27:28":
        manufacturer = "Microsoft Corporation"

    elif user_MAC == "04:26:65":
        manufacturer = "Apple, Inc."

    elif user_MAC == "04:33:89":
        manufacturer = "Huawei Technologies Co., Ltd"

    elif user_MAC == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"

    else:   # This will catch invalid values or values not found.
        manufacturer = "Unknown"

    # Output result telling the user the manufacturer name for their MAC address.
    print(f"For {user_MAC} the MAC manufacturer is {manufacturer}.")

# Calling the main function.
if __name__ == "__main__":
    main()