def main():
    manufacturers = [
        ("00:00:17", "Oracle"),
        ("00:07:E9", "Intel Corporation"),
        ("04:27:28", "Microsoft Corporation"),
        ("04:26:65", "Apple, Inc."),
        ("04:33:89", "Huawei Technologies Co.,Ltd"),
        ("00:00:0C", "Cisco Systems, Inc")
    ]

    print("           MAC Manufacturer Program")
    print("------------------------")
    print()

    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    manufacturer_name = "Unknown"
    for code, name in manufacturers:
        if user_input.upper() == code:
            manufacturer_name = name
            break

    print(f"For {user_input} the MAC manufacturer is {manufacturer_name}.")

if __name__ == "__main__":
    main()
