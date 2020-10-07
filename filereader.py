#ethan pham
#program reads from fightformyfriends.txt and displays names and ages

def main():
    #open file named fightformyfriends.txt
    infile = open('fightformyfriends.txt', 'r')

    #initialize friend count variable
    friendCount = 0

    #initialize age total variable
    ageTotal = 0

    #use while loop to read data from file
    while friendCount < 4:
        #reads a line and assigns it to name variable
        name = infile.readline()
        #strips new line break
        name = name.rstrip('\n')
        #reads next line and assigns it to age variable
        age = int(infile.readline())
        #print friend's name and age
        print("My friend", name, "is", age)
        #increment loop counter
        friendCount += 1
        #every time age updates, ageTotal variable updates with new age added
        ageTotal += age

    #calculate average age with final total
    ageAvg = ageTotal / 4.0
    print("Average age of friends is", ageAvg)
    #close file
    infile.close()

main()
