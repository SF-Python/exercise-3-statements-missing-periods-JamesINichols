#Morgan Ray (morgan-rayCOP2002)
#COP2002.0M1
#February 6,2025
#Exercise 3
#If Statements
#
#This Program will take user input for a MAC address and which Tech Organization that it identifies
 
#Get user input

oui=input("What are the first 6 hexadecimal digits of your MAC address? ")

#Process input and give an answer

if oui == "00:00:17":
    print("This is the OUI for Oracle")
elif oui == "00:07:E9":
    print("This is the OUI for Intel Corporation")
elif oui == "04:27:28":
    print("This is the OUI for Microsoft Corporation")
elif oui == "04:26:65":
    print("This is the OUI for Apple, Inc.")
elif oui == "04:33:89":
    print("This is the OUI for Huawei Technologies Co.,Ltd")   
elif oui == "00:00:0C":
    print("This is the OUI for Cisco Systems, Inc")
else: print("Invalid OUI")