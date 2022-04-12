
ordered_product_list = []
cart_items = []
users = ["ram", "hari", "sita", "radha", "holika"]
passwords = ["ram123", "hari123", "sita123", "radha123", "holika123"]

def stockProducts():
    stock_product_list = ["Pen", "Book", "Geomentry Box", "Copy", "Guess Papers", "Note Book"]

    # add_product = input("Enter a product name: ")
    # format = add_product.capitalize()
    # stock_product_list.append(format)
    # print(stock_product_list)
    return stock_product_list

def addToCart():
    print(stockProducts())
    add_product = input("Enter a product name: ")
    if add_product in stockProducts():
        cart_items.append(add_product)
        print(f"{add_product} is added to your cart.")
    else:
        print("No product found.")

def showCart():
    if len(cart_items) == 0:
        print("There are no product in your cart.")
    else:
        print("Your Cart Items: ")
        return cart_items

def orderProduct():
    ordered_product = input("Enter a product name: ")
    if ordered_product in stockProducts():
        confirm_order = input("Confirm your order: Yes or No: ")
        if confirm_order == "Yes":
            ordered_product_list.append(ordered_product)
            print(f"{ordered_product} ordered successfully.")
            userDashboard()
        elif confirm_order == "No":
            print("Order denied.")
            orderProduct()
    else:
        print("No product found.")
        orderProduct()

def showOrderedItems():
    if len(ordered_product_list) == 0:
        print("There are no order's..")
    else:
        print("Your Ordered List: ")
        return ordered_product_list
    
def mode(select_mode): 
    return select_mode

def userDashboard():
    print("")
    print("Welcome to User Dasboard.")
    input("Press Enter to continue...")
    print("""Select Mode: 
    1. View Stock Products
    2. Order Product
    3. View Ordered Product
    4. Add to Cart
    5. View Cart""")
    select_mode = int(input("Select mode: "))
    if mode(select_mode) == 1:
        print(stockProducts())
        print("")
        userDashboard()
    elif mode(select_mode) == 2:
        print(stockProducts())
        print("")
        orderProduct()
    elif mode(select_mode) == 3:
        print(showOrderedItems())
        print("")
        userDashboard()
    elif mode(select_mode) == 4:
        addToCart()
        print("")
        userDashboard()
    elif mode(select_mode) == 5:
        print(showCart())
        print("")
        userDashboard()
    else:
        print("Enter a valid number...")
        userDashboard() 

def loginHandle():
    print("")
    email = input("Enter Email Address: ")
    if email in users:
        print("")
        password = input("Enter Password: ")
        if password in passwords:
            print("")
            print("Logged IN .... as", email)
            userDashboard()
        else:
            print("Incorrect Password, Please Try again..")
            loginHandle()
    else:
        print("Incorrect Email, Please Try again...")
        loginHandle()



# stockProducts()
# addToCart()
# orderProduct()
# userDashboard()

loginHandle()

