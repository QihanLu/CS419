import pickle
import login
import function

def listuserfunction(name):
    while True:
        # employee
        pri=login.userlist[name][1]
        if pri == "1":
            print("Userlist operation: Listuser,Changepassword,Exit")
            print('|')
            print("file operation: Read,Savetxt,Showtxt,Downloadtxt")
        # manager
        if pri == "2":
            print("Userlist operation: Listuser,Changepassword,Deleteuser,Exit")
            print('|')
            print("file operation: Read,Savetxt,Deletetxt,Showtxt,Downloadtxt")
        # admin
        if pri == "3":
            print("Userlist operation: Listuser,Changepassword,Delete,Add,Promote,Demote,Sync,Restore,Exit")
            print('|')
            print("file operation: Read,Savetxt,Deletetxt,Showtxt,Downloadtxt,Syncfile,Restorefile")
        do = input("Please enter the next operation: ")
        do = do.upper()

        if do == "LISTUSER":
            listuserinfo()
        elif do=="CHANGEPASSWORD":
            changepassword(name)
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
        # manager
        elif pri == "2":
            if do == "DELETE":
                delete(2)
            elif do=="DELETETXT":
                function.deletetxt(2)
            else:
                print("incorrect input")
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


# list the name of every one
def listuserinfo():
    for l in login.userlist:
        print(l)

def changepassword(name):
    oldpassword=input("Please input old password: ")
    if oldpassword==login.userlist[name][0]:
        login.userlist[name][0]=input("Please input new password: ")
        print("Succeed to change password")
        return
    print("Incorrect password")

# add a person with his username and password
def add():
    name = input("Enter the username: ")
    if name in login.userlist:
        print("Name is taken")
        return
    password = "111111"
    print("Your default password is 111111")
    privilege = input("Enter the privilege(1,2): ")
    if privilege != "2" and privilege != "1":
        print("Privilege is incorrect")
        return
    login.userlist[name] = [password, privilege]
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to add user")


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
    else:
        print("Sorry, you need higher privilege")


# promote an employee to manager
def promote():
    n = input("Enter the name to promote: ")
    if n not in login.userlist:
        print("Sorry, the username is not correct")
        return
    if login.userlist[n][1] == "2":
        print("You can not promote a manager")
        return
    elif login.userlist[n][1] == "3":
        print("You can not promote yourself")
        return
    login.userlist[n][1] = "2"
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to promote user")


# demote a manager to employee
def demote():
    n = input("Enter the name to demote: ")
    if n not in login.userlist:
        print("Sorry, the username is not correct")
        return
    if login.userlist[n][1] == "1":
        print("You can not demote a user")
        return
    elif login.userlist[n][1] == "3":
        print("You can not demote yourself")
        return
    login.userlist[n][1] = "1"
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to demote user")


# copy the userlist into backup file
def sync():
    pickle.dump(login.userlist, open("backup.dat", "wb"))
    print("succeed to sync")


# restore the backup file to userlist and mainfile
def restore():
    try:
        login.userlist = pickle.load(open("backup.dat", "rb"))
    except (FileNotFoundError, IOError):
        print("No backup file found")
        return
    pickle.dump(login.userlist, open("users.dat", "wb"))
    print("succeed to restore")
