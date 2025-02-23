#Devonta Thurman
#COP2002.OM1
#Feb 16, 2025
#Exercise 3
#Using If-Statements

print("Enter the first 6 hex values of the MAC address (format as XX:XX:XX):")

Manufacturer = [f"Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

Hex_Digits = [f"00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C"]

answer = input()

if answer in Hex_Digits:
    if answer == Hex_Digits[0]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[0]}")
    if answer == Hex_Digits[1]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[1]}")
    if answer == Hex_Digits[2]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[2]}")
    if answer == Hex_Digits[3]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[3]}")
    if answer == Hex_Digits[4]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[4]}")
    if answer == Hex_Digits[5]:
        print(f"For {answer} the MAC manufacturer is {Manufacturer[5]}")
else:
    print("Unknown")