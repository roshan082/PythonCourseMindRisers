# Case Study  -- ATM CLI




# pin = 2580
# accountName = "MindRisers"
# transactionCode = 2255
# accountNumber = 1245365895546
# totalBalance = 10000
# interstRate = 12.5

# accuntDetails = {"pin": pin, "acName": "acconutName", "trancCode": transactionCode, "acNumber": accountNumber}

# print("Welcom to MindRisers ATM")
# print ("Enter your valid pin code.")
# inputPin = int(input("Enter PIN Code:"))
# if inputPin == pin:
#     print("Welcome", accountName)
#     print("Select Mode:")
#     print("1. Deposit - to deposit amonut:")
#     print("2. Show - to check balance:")
#     print("3. Interest - to check interest rate:")
#     print("4. Caculate - to calculate interest:")
#     mode = input("Enter Mode: ")
#     if mode == "1":
#         balance = float(input("Enter balance to deposit:"))
#         totalBalance += balance
#         print("Your Toatal Balance is :", totalBalance)
#     elif mode == "2":
#         print("Your current balance is: ", totalBalance)
#     elif mode == "3":
#         print("Your current interest rate is: ", interstRate)
#     elif mode == "4":
#         ir = interstRate
#         amt = totalBalance
#         ia = ir/12
#         ta = amt + ia
#         print("Your Total balance is: ", ta, "Interest Rate is: ", interstRate)
#     else:
#         print("PLease select correct mode")
# else:
#     print("Incorrect Pin")

# case stdy 2
email = str
password = str
# add mode for login and registration -- on your own
mode = input("""
Enter Mode:
1. Login
2. Register 
""")
if mode == str(1):
    email = input("Enter your email: ")
    if email == "mr@gmail.com":
        password = input("Enter your password: ")
        if password == "mind123":
            print("Logged In")
        else:
            print("Invalid Email and Password")
    else:
        print("Email not resgistered.")
elif mode == str(2):
    fullName = input("Enter your Full Name: ")
    print("Your Name is ", fullName)
    contactNumber = int(input("Enter your Mobile number."))
    print("Your Contact is", contactNumber)
    email = input("Enter your Email address: ")
    if email == "mr@gmail.com":
        print("Email is already registered. Try new one.")
        exit()  
    password = input("Enter your password: ")
    confirmPassword = input("Enter your password again: ")
    if password != confirmPassword:
        print("Password didn't match. Registration unseccessfull..")
    else:
        print("Your account is registered successfully!!!")
    

# bike engine start
# chess checkmate
# dice roll

