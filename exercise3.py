# Chris Fillyaw (ChrisFilyaw1)
# COP2002-OM1
# February ,2025
# Exercise 3
# A program that determines who the manufacturer is for a NIC card using the first 6 hex digits

def main():
    print("MAC Manufacturer Program\n------------------------\n") # Print the title
    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ") # Get user input

   # Define the manufacturer based on the user input
    if user_input == "00:00:17": 
        manufacturer = "Oracle"
    elif user_input == "00:07:E9":
        manufacturer = "Intel Corporation"
    elif user_input == "04:27:28":
        manufacturer = "Microsoft Corporation"
    elif user_input == "04:26:65":
        manufacturer = "Apple, Inc"
    elif user_input == "04:33:89":
        manufacturer = "Huawei Technologies Co.,Ltd"
    elif user_input == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"
    else:
        manufacturer = "<Not valid value or not found> Unknown"
    
    
    print(f"For {user_input} the MAC manufacturer is {manufacturer}.") # Print the manufacturer

if __name__ == "__main__": # Run the main function
    main()