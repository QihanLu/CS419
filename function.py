import pickle
import base64

class text():
    level = 1
    name = ""
    content = ""


try:
    list = pickle.load(open("readlist.dat", "rb"))
except (FileNotFoundError, IOError):
    list = []
    pickle.dump(list, open("readlist.dat", "wb"))


def read(level):
    global list
    file = input("Type in the name of file you want to read: ")
    print('\n')
    for x in list:
        if x.name == file:
            if x.level <= level:
                tt = x.content
                ttt = base64.b64decode(tt).decode('utf-8')
                print(ttt)
                print("Succeed to show text")
                print('\n')
                return
            else:
                print("You dont have permission to view this")
                print('\n')
                return
    print("File not found")


def savetxt(level):
    global list
    print(list)
    file = input("Type in the name of file you want to save: ")
    print('\n')
    try:
        f = open(file+".txt", "r")
    except (FileNotFoundError, IOError):
        print("file not found")
        return

    tt = f.read()
    aaa = text()
    aaa.level = level
    aaa.name = file
    aaa.content = base64.b64encode(tt.encode('utf-8'))
    list.append(aaa)
    pickle.dump(list, open("readlist.dat", "wb"))
    print("succeed to save text")
    print('\n')
    return


def deletetxt(level):
    file = input("Type in the name of file you want to delete: ")
    print('\n')
    global list
    if int(level) >= 2:
        for i in range(len(list)):
            if list[i].name == file:
                list.pop(i)
                pickle.dump(list, open("readlist.dat", "wb"))
                print("Succeed to delete text")
                print('\n')
                return
        print("File not found")
        print('\n')
        return
    print("You need higher privilege to delete")
    print('\n')
    return


def showtxt(level):
    for i in list:
        if i.level <= level:
            print(i.name + '\n' + '|' + '\n')
    print("succeed to show text")
    print('\n')
    return


def downloadtxt(level):
    file = input("Type in the name of file you want to download: ")
    print('\n')
    for i in list:
        if i.name == file:
            if i.level <= level:
                f = open(file + ".txt", "w")
                ei = base64.b64decode(i.content).decode('utf-8')
                f.write(ei)
                f.close
                print("succeed to download text")
                print('\n')
                return
            else:
                print("You dont have the permission to download the document")
                print('\n')
                return
    print("File not found")


def syncfile():
    pickle.dump(list, open("readlistbackup.dat", "wb"))
    print("succeed to sync")
    print('\n')


def restorefile():
    global list
    try:
        list = pickle.load(open("readlistbackup.dat", "rb"))
    except (FileNotFoundError, IOError):
        print("No backup file found")
        print('\n')
        return
    pickle.dump(list, open("readlist.dat", "wb"))
    print("succeed to restore")
    print('\n')
