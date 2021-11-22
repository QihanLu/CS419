import pickle
import login
import function

def listuserfunction(name):
    while True:
        # employee
        pri=login.userlist[name][1]
        if pri == "1":
            print("Userlist operation: Listuser,Exit")
            print("file operation: Read,Savetxt,Showtxt,Downloadtxt")
            print('\n')
        # manager
        if pri == "2":
            print("Userlist operation: Listuser,Deleteuser,Exit")
            print("file operation: Read,Savetxt,Deletetxt,Showtxt,Downloadtxt")
            print('\n')
        # admin
        if pri == "3":
            print("Userlist operation: Listuser,Delete,Add,Promote,Demote,Sync,Restore,Exit")
            print("file operation: Read,Savetxt,Deletetxt,Showtxt,Downloadtxt,Syncfile,Restorefile")
            print('\n')
        do = input("Please enter the next operation: ")
        do = do.upper()

        if do == "LISTUSER":
            listuserinfo()
        elif do == "EXIT":
            return
        elif do=="READ":
            function.read(pri)
        elif do=="SAVETXT":
            function.savetxt(pri)
        elif do=="SHOWTXT":
            function.showtxt(pri)
        elif do=="DOWNLOADTXT":
            function.downloadtxt(pri)
        # employee
        elif pri == "1":
            print("incorrect input")
            print('\n')
        # manager
        elif pri == "2":
            if do == "DELETE":
                delete(2)
            elif do=="DELETETXT":
                function.deletetxt(2)
            else:
                print("incorrect input")
                print('\n')
        # admin
        elif pri == "3":
            if do == "DELETE":
                delete(3)
            elif do == "ADD":
                add()
            elif do == "PROMOTE":
                promote()
            elif do == "DEMOTE":
                demote()
            elif do == "SYNC":
                sync()
            elif do == "RESTORE":
                restore()
            elif do=="DELETETXT":
                function.deletetxt(pri)
            elif do=="SYNCFILE":
                function.syncfile()
            elif do=="RESTOREFILE":
                function.restorefile()
            else:
                print("incorrect input")
                print('\n')


# list the name of every one
def listuserinfo():
    for l in login.userlist:
        print(l)
    print('\n')
        


# add a person with his username and password
def add():
    name = input("Enter the username: ")
    if name in login.userlist:
        print("Name is taken")
        print('\n')
        return
    password = input("Enter the password: ")
    privilege = input("Enter the privilege(1,2): ")
    if privilege != "2" and privilege != "1":
        print("Privilege is incorrect")
        print('\n')
        return
    login.userlist[name] = [password, privilege]
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to add user")
    print('\n')


# delete a person while p is the privilege of the operator
def delete(p):
    n = input("Enter the name to delete: ")
    if n not in login.userlist:
        print("Sorry, the username is not correct")
        return
    # the operator should have higher privilege than the person to delete
    if int(login.userlist[n][1]) < p:
        del login.userlist[n]
        pickle.dump(login.userlist, open("users.dat", "wb"))
        print("succeed to delete user")
        print('\n')
    else:
        print("Sorry, you need higher privilege")
        print('\n')


# promote an employee to manager
def promote():
    n = input("Enter the name to promote: ")
    if n not in login.userlist:
        print("Sorry, the username is not correct")
        print('\n')
        return
    if login.userlist[n][1] == "2":
        print("You can not promote a manager")
        print('\n')
        return
    elif login.userlist[n][1] == "3":
        print("You can not promote yourself")
        print('\n')
        return
    login.userlist[n][1] = "2"
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to promote user")
    print('\n')


# demote a manager to employee
def demote():
    n = input("Enter the name to demote: ")
    if n not in login.userlist:
        print("Sorry, the username is not correct")
        print('\n')
        return
    if login.userlist[n][1] == "1":
        print("You can not demote a user")
        print('\n')
        return
    elif login.userlist[n][1] == "3":
        print("You can not demote yourself")
        print('\n')
        return
    login.userlist[n][1] = "1"
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to demote user")
    print('\n')


# copy the userlist into backup file
def sync():
    pickle.dump(login.userlist, open("backup.dat", "wb"))
    print("succeed to sync")
    print('\n')


# restore the backup file to userlist and mainfile
def restore():
    try:
        login.userlist = pickle.load(open("backup.dat", "rb"))
    except (FileNotFoundError, IOError):
        print("No backup file found")
        print('\n')
        return
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to restore")
    print('\n')
