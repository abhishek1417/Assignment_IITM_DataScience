import re
from getpass import getpass

email_regex = "(\w+@[a-zA-A_]+?\.[a-zA-Z]{2,6})"
passwd_regex = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{5,16}$"

def registration():
    username = input('Username: ')
    passwd = getpass('Password: ')
    if re.fullmatch(email_regex, username) and re.fullmatch(passwd_regex, passwd):
        file = open("user_detail.txt","a")
        file.write("\n"+username+","+passwd)
        print('You have registered successfully!')
        return False
    else:
        print("Wrong format of username or password ! please try again !!")
    return True

def login():
    username = input('Username: ')
    passwd = getpass('Password: ')
    file = open("user_detail.txt","r")
    flag=0
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if(a==username and b==passwd):
            print('You have login successfully!')
            flag=1
    if(flag==0):
        print("Wrong username or password ! please try again !!")
        return False
    else:
        return True

def forgetpasswd():
    username = input('Username: ')
    file = open("user_detail.txt","r")
    flag=0
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if(a==username):
            print('Your password is : ',b)
            flag=1
    if(flag==0):
        print("Wrong username or password ! please try again !!")
        return False
    else:
        return True

if __name__ == '__main__':
    window = True
    while window:
        initial_choice = int(input('Select one option : \n1 for registration or \n2 for login\n3 for forget password\n'))
        if initial_choice == 1:
            window = registration()
        elif initial_choice==2:
            window = login()
        elif initial_choice==3:
            window = forgetpasswd()
        else:
            print("Wrong Input ! Try Again !! ")
            window =True

        
