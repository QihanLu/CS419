import pickle


try:
    userlist=pickle.load(open("users.dat","rb"))
except (FileNotFoundError, IOError):
    userlist = {"Admin": ["admin", "3"]}
    pickle.dump(userlist,open("users.dat","wb"))

def getname():
    return input("Enter your name: ")

def getpassword():
    return input("Enter your password: ")

def checkuserinfo(name,password):
    if name not in userlist:
        return False
    if userlist[name][0] != password:
        return False
    return True

def getprivilege(name):
    return userlist[name][1]

