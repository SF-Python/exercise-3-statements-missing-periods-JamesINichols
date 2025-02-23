# Logan Cole ljcole93
# COP2002.0M1
# 14Feb25
# exercise 3
# A program demonstrating the use of conditions, if statements, and other concepts from chapter 3.

def pull_manu(mac_ID):
    if mac_ID == "00:00:0C":
        return "Cisco Systems, Inc"
    elif mac_ID == "04:33:89":
        return "Huawei Technologies Co.,Ltd"
    elif mac_ID == "04:26:65":
        return "Apple, Inc"
    elif mac_ID == "04:27:28":
        return "Microsoft Corporation"
    elif mac_ID == "00:07:E9":
        return "Intel Corporation"
    elif mac_ID == "00:00:17":
        return "Oracle"
    else:
        return "Unknown"

def main():
    mac_ID = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX):")
    manufacturer = pull_manu(mac_ID)
    print(f"MAC Address first 6: {mac_ID}")
    print(f"Manufacturer: {manufacturer}")

if __name__ == "__main__":
    main()