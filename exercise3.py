print("Hello, World!")
def main():
    # Display the title of the program
    print("MAC Manufacturer Program")
    print("------------------------")
   
    # Prompt the user for input in the specified format
    mac_address = input("\nEnter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Determine the manufacturer based on the input
    if mac_address == "00:00:17":
        manufacturer = "Oracle"
    elif mac_address == "00:07:E9":
        manufacturer = "Intel Corporation"
    elif mac_address == "04:27:28":
        manufacturer = "Microsoft Corporation"
    elif mac_address == "04:26:65":
        manufacturer = "Apple, Inc."
    elif mac_address == "04:33:89":
        manufacturer = "Huawei Technologies Co.,Ltd"
    elif mac_address == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"
    else:
        manufacturer = "Unknown"
   
    # Output the result
    print(f"\nFor {mac_address} the MAC manufacturer is {manufacturer}.\n")

# Call the main function
if __name__ == "__main__":
    main()
