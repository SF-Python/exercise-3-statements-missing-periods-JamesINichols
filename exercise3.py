# John Pfeilsticker (GitHub: ingannilo)
# COP2002 Section 0M1
# 2025-02-07
# Exercise 3: If Statements
# MAC address to manufacturer program 

def main():

# print program title
    print("MAC Manufacturer Progam")
    print("-"*23, "\n")


# initializing boolean to be used in while loop allowing program 
# to restart if invalid input is given from the user
    restartFlag = True

# while loop to restart program as described in previous comment
    while(restartFlag == True):

# prompting user for input
        userIn = input("Type the first six hex digits of the MAC address (format as XX:XX:XX): ")


# each if/elif statement below returns the manufacturer from known values
# if any branch prior to the else statement is entered, restart flag is flipped
        if(userIn == "00:00:17"):
            print("For 00:00:17 the manufacurer is Oracle.")
            restartFlag = False

        elif(userIn == "00:07:E9"):
             print("For 00:07:E9 the manufacturer is Intel Coprporation.")
             restartFlag = False

        elif(userIn == "04:27:28"):
             print("For 04:27:28 the manufacturer is Microsoft Coroporation.")
             restartFlag = False

        elif(userIn == "04:26:65"):
             print("For 04:26:65 the manufacturer is Apple Inc.")
             restartFlag = False

        elif(userIn == "04:33:89"):
             print("For 04:33:89 the manufacturer is Huawei Technologies Co.,Ltd")
             restartFlag = False

        elif(userIn == "00:00:0C"):
             print("For 00:00:0C the manufacturer is Cisco Systems, Inc.")
             restartFlag = False

# else statement below tells user thier input is no good;
# re-assigning restartFlag just for clarity that entering 
# this branch indicates failure to find manufacturer from input
        else:
             print("Input not recognized/unknown manufacturer.  Plase try again.", "\n")
             restartFlag = True
        
if(__name__=="__main__"):
    main()
