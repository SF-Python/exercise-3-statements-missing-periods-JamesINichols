# Collin Barnes (Coin117)
# COP2002.0M1
# 2-16-2025
# Exercise 3
# Program to lookup MAC Manufacturers

def get_manufacturer(mac_prefixes, manufacturers, mac_input):
    for i in range(len(mac_prefixes)):
        if mac_input.upper() == mac_prefixes[i]:
            return manufacturers[i]
    return "Unknown"

def main():
    print("           MAC Manufacturer Lookup")
    print("------------------------")
    print()
    
    mac_prefixes = [
        "00:00:17",
        "00:07:E9",
        "04:27:28",
        "04:26:65",
        "04:33:89",
        "00:00:0C"
    ]
    
    manufacturers = [
        "Oracle",
        "Intel Corporation",
        "Microsoft Corporation",
        "Apple, Inc.",
        "Huawei Technologies Co.,Ltd",
        "Cisco Systems, Inc"
    ]
    
    mac_input = input("Enter the first 6 hex values of the MAC address you wish to find (format as XX:XX:XX): ")
    manufacturer = get_manufacturer(mac_prefixes, manufacturers, mac_input)
    
    print(f"For {mac_input} the MAC manufacturer is {manufacturer}.")

if __name__ == "__main__":
    main()