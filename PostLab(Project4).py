userpin = input("Please make a 4 digit pin:")
def verify_pin(pin):
    if pin == userpin:
        return True
    else:
        return False

def log_in():
    print("NOTE:The police will be called if you had three successive failures ")
    tries = 0
    while tries < 3:
        pin = input('Please Enter Your 4 Digit Pin:')
        if verify_pin(pin):
            print("Pin accepted!")

            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Calling the police. Disabling login button")
    return False

def start_menu():
    print("Welcome to the atm!")
    if log_in():
        print("Login Successful!")
start_menu()