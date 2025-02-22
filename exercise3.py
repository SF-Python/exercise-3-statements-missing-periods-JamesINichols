# Brianna Pinedo (briannamopi)
# COP2002.0M1
# February 11, 2025
# If Statements
# Determine who the manufacturer is for a NIC card

hexDigits= ['00:00:17', '00:07:E9', '04:27:28', '04:26:65', '04:33:89', '00:00:0C']
company=['Oracle', 'Intel Corporation', 'Microsoft Corporation', 'Apple, Inc.', 'HuaweiTechnologiesCo., Ltd', 'Cisco Systems, Inc']
#Lists of the codes and companies to keep track of which are in the system

theTitle='MAC Manufacturer Program\n------------------------'
print(theTitle)
print()
message=input('Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ')

#using data FROM the system for the if statements and prints

if message in hexDigits:
    if message == hexDigits[0]:
        print(f"For {message} the MAC manufacturer is {company[0]}.")
    elif message == hexDigits[1]:
        print(f"For {message} the MAC manufacturer is {company[1]}.")
    elif message == hexDigits[2]:
        print(f"For {message} the MAC manufacturer is {company[2]}.")
    elif message == hexDigits[3]:
        print(f"For {message} the MAC manufacturer is {company[3]}.")
    elif message == hexDigits[4]:
        print(f"For {message} the MAC manufacturer is {company[4]}.")
    elif message == hexDigits[5]:
        print(f"For {message} the MAC manufacturer is {company[5]}.")
    elif message == hexDigits[6]:
        print(f"For {message} the MAC manufacturer is {company[6]}.")
else:
    print('Unknown')

