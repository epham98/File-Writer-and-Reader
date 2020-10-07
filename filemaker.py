#ethan pham id 2384312
#stores first name and age of friends in text file
#each entry is written to its own line in text file

def main():
    #open file for writing
    myfile = open('fightformyfriends.txt', 'w')

    #initialize friend count variable
    friendCount = 0
    
    #use while loop to have maximum of four friends to write data to
    while friendCount < 4:
        #prompt for name
        name = input("Enter name of friend (<Enter> to quit): ")
        #prompt for age
        age = int(input("Enter age (integer) of friend: "))
        #write name and print new line for age
        myfile.write(name + '\n')
        #write age and print new line for next name
        myfile.write(str(age) + '\n')
        #increments count variable
        friendCount += 1

    #close file
    myfile.close()
    print("File created.")

#call main function
main()
    
