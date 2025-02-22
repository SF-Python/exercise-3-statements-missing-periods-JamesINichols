# Michael Harrison
# COP2002.OM1
# Exercise 3 - MAC Manufacturer Program

print (" Mac Manufacturer Program")
print (" -----------------------\n")



mac = input ("Enter the first six Hex digits seperated by colons in the format XX:XX:XX:  ")
if mac == "00:00:17":
    print ("Oracle")

elif mac == "00:07:E9":
    print ("Intel Corporation")

elif mac == "04:27:28":
    print ("Microsoft Corporation")

elif mac == "04:26:65":
    print ("Apple, Inc.")

elif mac == "04:33:89":
    print ("Huawei Technologies Co.,Ltd")

elif mac == "00:00:0C":
    print ("Cisco Systems, Inc")

else:
    print ("unknown")

#End Program