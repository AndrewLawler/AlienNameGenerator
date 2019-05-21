#11/18 Python v3.7.1
#Caluclating alien names using given name and family name and apply rules to it such as deleting alien names that do not contain vowels

#initializing list names
listactor = [] #actor
listalien = [] #alien
listvowels = [] #vowels
listextension = [] #extension
directorlist = [] #director
listactors = [] #extralist
listdeleted = [] #overall deleted list

#main menu
def main():
    print()
    print("\tMain Menu")
    print()
    option = input("A: Aliens \nE: Extend \nX: Exit \n \nEnter Option: ")
    option = option.upper()
    if option == "A":
        inputs()
    elif option == "E":
        #sending paramater to function e
        e(listvowels)
    elif option == "X":
        close()
    else:
        print()
        print("Please Try Again")
        main()

#close function
def close():
    print()
    closing = input("Would you like to close? Y or N: ")
    print()
    if closing == "Y":
        print("Goodbye!")
        exit()
    elif closing == "N":
        main()
    else:
        print()
        print("Enter Valid Input")
        main()

def inputs():
    print()
    print("\tAlien Generator")
    print()
    client_name = input("Enter your first and last name: ")
    #.split simply splits after the space to give two inputs easily
    given_name, family_name = client_name.split()
    #creating full name using + and adding to actor list
    fullname = given_name+" "+family_name
    listactor.append(fullname)
    #sending values to next function
    calc(given_name,family_name,listactor,fullname)

#taking in values
def calc(given_name,family_name,listactor,fullname):
    for a in listactor:
        #taking the first letter and second letter and swapping them
        given_name_2 = given_name[1:2] + given_name[0:1]
        given_name_2 = given_name_2.lower()
        name = family_name[0:3] + given_name_2
        #converting to lower case
        name = name.lower()
        #adding name to name list
        listalien.append(name)
        #sending parameters
        vowels(name,listalien,listactor,listvowels,fullname)
        output(listalien,listactor,name,listvowels,fullname)

def vowels(name,listalien,listactor,listvowels,fullname):
    #checking if letter is in alien name and assigning it to either 1 or 0
    if "a" in name:
        a = 1
    elif "a" not in name:
        a = 0
    if "e" in name:
        e = 1
    elif "e" not in name:
        e = 0
    if "i" in name:
        i = 1
    elif "i" not in name:
        i = 0
    if "o" in name:
        o = 1
    elif "o" not in name:
        o = 0
    if "u" in name:
        u = 1
    elif "u" not in name:
        u = 0
    #if any number = 0 the input fails
    
    if a == 0 and e == 0 and i == 0 and o == 0 and u == 0:
        print()
        #removing name from list and adding to deleted list
        listvowels.append(name)
        listdeleted.append(name)
        listalien.remove(name)
        #reassigning fullname and name value before sending it back
        fullname = "Name Removed"
        name = "Alien Name Invalid"
        output(listalien,listactor,name,listvowels,fullname)
    else:
        return

def output(listalien,listactor,name,listvowels,fullname):
    print()
    print("\tInput")
    print()
    print("Name:",fullname)
    print()
    print("\tOutput")
    print()
    print("Alien Name:",name)
    print()
    print("\tLists")
    print()
    #prints lists
    print("Alien Names",listalien)
    print("Vowel Deleted Names",listvowels)
    print("Overall Deleted Names",listdeleted)
    delete(listalien,listactor,name,fullname)
    again(listalien)
    
def delete(listalien,listactor,name,fullname):
    #if alien list empty, dont ask to delete alien since there isnt any
    if listalien == []:
        again(listalien)
    print()
    print("\tDelete")
    print()
    deletes = input("Delete Alien Name? Y or N: ")
    if deletes == "Y":
        print()
        #deleting actor and alien that user specifies
        print("\tValues To Delete")
        print()
        alien = input("Name Of Alien: ")
        #converting alien to lower case
        alien = alien.lower()
        listdeleted.append(alien)
        listalien.remove(alien)
        #once deleted the fullname and name section is clear as its been deleted not added
        fullname = "CLEAR"
        name = "CLEAR"
        #sending more parameters
        output(listalien,listactor,name,listvowels,fullname)
        again(listalien)
    elif deletes == "N":
        again(listalien)
        inputs()
    else:
        main()

#asking user if they would like to repeat the process
def again(listalien):
    print()
    print("\tAdd")
    print()
    add  = input("Add Another? Y or N: ")
    if add == "Y":
        inputs()
    elif add == "N":
        print()
        print("\tFinished?")
        print()
        finish = input("Exit or Final Outcome? E or F: ")
        #nested if
        if finish == "F":
            end(listalien)
        elif finish == "E":
            main()
        else:
            main()
    else:
        print()
        close()

def end(listalien):
    print()
    print("\tFinal Output")
    #for x in some list, take x and take three letters then append to list, complete for all values in list
    for x in listalien:
        x = x[0:3]
        directorlist.append(x)

    #creating new lists to use
    listactors = listactor[:]
    listaliens = listalien[:]

    #joining director list
    director = "".join(directorlist)
    #converting to upper case because STEVEN looks better than steven
    director = director.upper()
    #putting a space inbetween steven and speilberg
    name = director[0:6]+" "+director[6:15]
    
    #actor = '-'.join(listactors)
    alien = " ".join(listaliens)
    print()
    print("Director:",name)
    print()
    print(name+" "+"PRESENTS")
    print()
    print("\tFinal Cast")
    print()
    print("Actors:",listactors)
    print("Aliens:",listaliens)
    print()
    menuoption = input("Would you like to go the main menu? Y or N: ")
    if menuoption == "Y":
        main()
    elif menuoption == "N":
        close()
    

def e(listvowels):
    #if vowel remove list is empty, dont run extension since there isnt anything to run
    if listvowels == []:
        print()
        print("Extension")
        print()
        print("List currently empty, please use the Alien function to generate some false names")
        main()
    else:
        #when run, create new list
        new_list = []
        print()
        print("Extension")
        print()
        #creating a copy of listvowels to use in this function called listextension
        listextension = listvowels[:]
        #for x in some list, take x and print it, then take x and add to new variables a,e,i,o,u and put a letter after the third letter
        for x in listextension:
            print("Input:",x)
            print()
            a = [x[0:3]+"a"+x[3:5]]
            e = [x[0:3]+"e"+x[3:5]]
            i = [x[0:3]+"i"+x[3:5]]
            o = [x[0:3]+"o"+x[3:5]]
            u = [x[0:3]+"u"+x[3:5]]
            #convert to string
            a = str(a)
            e = str(e)
            i = str(i)
            o = str(o)
            u = str(u)
            #print 2:8 to get out of brackets
            print(a[2:8])
            print(e[2:8])
            print(i[2:8])
            print(o[2:8])
            print(u[2:8])
            print()
        menu_option = input("Would you like to go the main menu? Y or N: ")
        if menu_option == "Y":
            main()
        elif menu_option == "N":
            print()
            print("Bye!")
            exit()

main()
