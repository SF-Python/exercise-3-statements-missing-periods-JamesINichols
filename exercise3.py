# Kyler Cole
# COP2002.0M1
# 12 February 2025
# MAC Manufacturer Resolution to Developer Company
# This program will run to allow the end user to input the first six MAC Address Hexadecimal digits of their NIC to resolve it to the manufacturer company.

# Program name
print('MAC Manufacturer Program')
print('------------------------')

# Dialogue for user to read and type a response to
nicMAC = input("\nEnter the first 6 hex values of the MAC address of your NIC (format as XX:XX:XX): ")

# Block of code that will give the user an answer based on their input
if nicMAC == '00:00:17':
    manufacturer = 'Oracle'
elif nicMAC == '00:07:E9':
    manufacturer = 'Intel Corporation'
elif nicMAC == '04:27:28':
    manufacturer = 'Microsoft Corporation'
elif nicMAC == '04:26:65':
    manufacturer = 'Apple, Inc.'
elif nicMAC == '04:33:89':
    manufacturer = 'Huawei Technologies Co.,Ltd'
elif nicMAC == '00:00:0C':
    manufacturer = 'Cisco Systems, Inc.'
else:
    manufacturer = 'Unknown'

# End of program statement
print(f'\nFor {nicMAC} the MAC manufacturer is {manufacturer}.')