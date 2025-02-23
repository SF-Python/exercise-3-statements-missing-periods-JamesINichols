#Dominic Lee
#02/16/2025
#COP2002 0M1
#Exercise 3: If statements


print("MAC Manufacturer Program")

print("---------------------")

print() #Blank line


def main():


# List of hex codes and manufacturers
    manufacturers =[
        ("00:00:17", "Oracle"),
        ("00:07:E9", "Intel Corporation"),
        ("04:27:28", "Microsoft Corporation"),
        ("04:26:65", "Apple, Inc."),
        ("04:33:89", "Huawei Technologies Co., Ltd"),
        ("00:00:0C", "Cisco Systems, Inc")]
    
# Ask for input
    hex_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    manufacturer = "Unknown"

# Loop through the list to find a match
    for match, MAC in manufacturers:
        if hex_input.upper() == match:
            manufacturer = MAC


        # Output the result
    print(f"For {hex_input} the MAC manufacturer is {manufacturer}.")

if __name__ == "__main__":
    main()
  
