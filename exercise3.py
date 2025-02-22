# Gianna Walter
# Course ID: COP2002 and section #0M1
# 2/05/2025
# Exercise 3
# If Statements

# Created main function
def main():
    # created list of manufacturer codes
    manfact_codes = [("00:00:17","Oracle"), ("00:07:E9","Intel Corporation"),("04:27:28","Microsoft Corporation"),("04:26:65","Apple, Inc."),("04:33:89","Huawei Technologies Co. Ltd"),("00:00:0C","Cisco Systems, Inc")]

    # Asked for user input
    user_input = input("Enter the first 6 hex digits of the MAC address (XX:XX:XX): ")

    # defining found variable
    found=False
    # looping through the list
    for hex_dig, maufact in manfact_codes:
        # checking if user input is in the list
        if user_input==hex_dig:
            # printing the manufacturer if found in the list
            print(f"The manufacturer is {maufact}")
            # setting found to true
            found = True
            break
    # printing unknown if not found
    if not found:
        print("Manufacturer: Unknown")
        
# Calling main function
if __name__=="__main__":
    main()