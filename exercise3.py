# Elo Ilechukwu (El0TN)
# COP2002-0M1
# February 11 2025
# Exercise 3
#  If statements

def main():
    # List of known manufacturers, indexed by their OUI
    manufacturers = (
        "00:00:00 - Xerox",
        "00:00:01 - Xerox",
        "00:00:02 - Xerox",
        "00:00:03 - Cisco",
        "00:00:04 - IBM",
        "00:00:05 - Apple",
        "00:00:06 - Microsoft",
        "00:00:07 - Intel",
        "00:00:08 - HP",
        "00:00:09 - Dell",
        "00:00:0A - Netgear",
        "00:00:0B - Linksys",
        "00:00:0C - Brocade",
        "00:00:0D - Avaya",
        "00:00:0E - Epson",
        "00:00:0F - Sony",
        # Add more manufacturers as necessary
    )
    
    # Ask for user input
    user_input = input("Enter the first 6 hex digits (formatted as XX:XX:XX): ")
    
    # Validate input format
    if len(user_input) != 17 or user_input(2) != ':' or user_input(5) != ':' or not all(c in '0123456789ABCDEF' for c in user_input if c != ':'):
        print("Invalid format. Please enter as XX:XX:XX.")
        return
    
    # Extract the manufacturer code
    manufacturer_code = user_input.upper()(:8)  # Get the first 8 characters (including colons)
    
    # Find the manufacturer
    manufacturer_found = False
    for manufacturer in manufacturers:
        if manufacturer.startswith(manufacturer_code):
            print(f"The manufacturer for {manufacturer_code} is: {manufacturer(9:)}")
            manufacturer_found = True
            break
    
    if not manufacturer_found:
        print(f"No manufacturer found for {manufacturer_code}.")

if __name__ == "__main__":
    main()