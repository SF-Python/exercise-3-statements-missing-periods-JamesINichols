# Rohan Caballero (Gigantopithecus1987)
# COP2002-0M1
# January 16, 2025
# Exercise 3
# Program that returns the MAC manufacturer based on the MAC address

#Lists for both the input and output
Ouput=["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc.", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc", "Unknown"]
Input=["00:00:17", "00:07:E9", "04:27:28", "04:26:65", "04:33:89", "00:00:0C",]

#Input measure
prompt=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

#Input/Output chain
if prompt==Input[0]:
    print("For",prompt, "the MAC manufacturer is", Ouput[0])
elif prompt==Input[1]:
    print("For",prompt, "the MAC manufacturer is", Ouput[1])
elif prompt==Input[2]:
    print("For",prompt, "the MAC manufacturer is", Ouput[2])
elif prompt==Input[3]:
    print("For",prompt, "the MAC manufacturer is", Ouput[3])
elif prompt==Input[4]:
    print("For",prompt, "the MAC manufacturer is", Ouput[4])
elif prompt==Input[5]:
    print("For",prompt, "the MAC manufacturer is", Ouput[5])
else:
    print("For",prompt, "the MAC manufacturer is", Ouput[-1])