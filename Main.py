import pickle
import login
import edit

def main():

    while True:
        name= login.getname()
        password= login.getpassword()
        print('\n')
        b=login.checkuserinfo(name,password)
        if b==False:
            print("Incorrect username or password")
            continue
        pri=login.getprivilege(name)
        edit.listuserfunction(name)





if __name__ == '__main__':
    main()