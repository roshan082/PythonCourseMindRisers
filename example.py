password = str
email = str
email = input("Enter your email: ")
if email == "abc@gmail.com":
    password = input("Enter your password :")
    if password == 'mind123':
        print("login success")
    else:
        print("Invalid email or password")
else:    
    print("Not registered yet")